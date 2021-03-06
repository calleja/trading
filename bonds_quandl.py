# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:21:37 2016
@author: CallejaL

bonds_quandl.py
"""

import Quandl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import numpy as np
import pylab as pl
import sys
#sys.path.append('G:/Property/Luis_C/statsLearning')
sys.path.append('/home/lechuza/Documents/economicAnalysis/trading')
import quandl_ror as ror
'''
Moodys Aaa
bonds having as close to 30 years maturity as possible
IRAAAD.US = Moody's seasoned corporate bonds rated Aaa
The "corporate" yields are unweighted averages of the more specific "industrial" and "utility" categories.  These are "long-term" bonds, with minimum and average maturities of 20 and 28 years, respectively.  The dataset adds Aa and A ratings but nothing lower, as its focus is investment-grade bonds
'''
#moody's simple yield of investment grade bonds
maaa = Quandl.get("MOODY/DAAAYLD", returns="pandas", trim_start="2014-01-02", trim_end="2016-02-20")

#should track closely with the US AA-rated Bond Index OAS:
ml_aaoas = Quandl.get("ML/AAOAS", returns="pandas", trim_start="2015-01-02")

#appears to be an index based on daily total returns
# S&P U.S. Issued AA Investment Grade Corporate Bond Index
spaaa = Quandl.get("SPDJ/SPUSG2AT", trim_start="2014-01-02", trim_end="2016-02-20")

maaa[-10:]

#moody's?
baa = Quandl.get("MOODY/DBAAYLD", returns="pandas", trim_start="2014-01-02", trim_end="2016-02-17")

baa[-10:]

fig=plt.figure()
plt.plot_date(aaa.index,aaa,'b-')
plt.plot_date(aaa.index,baa,'g-')
plt.show()

'''
Merrill Lynch CCC-rated Bond Index Yield
ML offers:
- CCC-rated Bond Index Yield
- CCC Bond Total Return Index
- US High Yield BB Corporate Index Yield
'''
mlccc=Quandl.get("ML/CCCY",returns="pandas",trim_start="2012-01-02")

mlhyoas = Quandl.get("ML/HYOAS", trim_start="2012-01-02")

mlhyoas[-5:]
mlccc[-5:]

'''
Let's see how CCC yield and HY OAS move together... we should try to explain why they will vary. First off, they will vary depending on the volatility of Investment Grade corporates, or whatever is the benchmark/risk-free rate
'''
fig=plt.figure()
plt.plot_date(mlccc.index,mlccc,'b-')
plt.plot_date(mlccc.index,mlhyoas,'g-')
fig.autofmt_xdate()
plt.ylabel('Yield and OAS')
plt.legend(['ML CCC YTM', 'HY OAS'],loc='best')
plt.show()

#that plot looks good... now will try to rotate the x-axis labels... the below didn't work... xticks() function (the one w/arguments) may need to be redone

#first, let's only consider rates/yields of the last 6 months
s="01/01/2015"
fif=dt.datetime.strptime(s,"%m/%d/%Y")
fif_1=pd.to_datetime(s) # we convert datetime to datetime64 (a pandas convention)
ml15=mlccc[mlccc.index>fif_1]
mlhyoas15=mlhyoas[mlhyoas.index>fif_1]

fig,ax=plt.subplots()
plt.xticks(mlccc.index)
locs,labels=plt.xticks()
#plt.setp(labels,rotation=45)
plt.plot_date(ml15.index,ml15,'b-')
plt.plot_date(ml15.index,mlhyoas15,'g-')
mdiz=mdates.drange(min(ml15.index),max(ml15.index),dt.timedelta(weeks=6)) #the dates are now floats... want to convert to a matplotlib date
mdiz1=pl.num2date(mdiz).strftime('%Y-%m-%d') #didn't work
#try using mdates.DateFormatter() and ax.axis.set_major_formatter()
plt.legend(['ML CCC YTM', 'HY OAS'],loc='best')
plt.xticks(mdiz1,rotation='vertical')
plt.show()

type(mdiz[1])

#scatterplot of these two datasets reveals a strong positive correlation:
plt.scatter(mlccc,mlhyoas)

'''
SPY continuos contract
'''
spy = Quandl.get("CHRIS/CME_SP1", trim_start="2015-01-02", trim_end="2016-02-20")

#test creation of a rate of return table
test1=ror.RateReturn(spy['Last'])
test1.oneTimeReturn(3,'1/6/2015')

'''
JPY/USD continuous contract
'''
jy1 = Quandl.get("CHRIS/CME_JY1", trim_start="2012-01-02", trim_end="2016-02-20")


'''First we'll run a simple correlation study of several of the indices... starting with AAA rated bonds'''
#concatenate two time series into a dataframe
con=pd.concat([maaa,spaaa],join='inner',axis=1)

con.columns=['moodys','sp']
con.head()

plt.figure();con.plot(); plt.legend(loc='best')

#plot each series on a different axis
plt.figure();con.plot(subplots=True, figsize=(8,8));plt.legend(loc='best')

'''
Determine a linear relationship between AA OAS from ML with the yield provided by Moody's - this is testing the OAS to the yield to maturity of Moody's basket of AAA investment bonds.
'''
#scatterplot of AA OAS from ML with the yield provided by Moody's
aaa_df=pd.concat([ml_aaoas,maaa],join='inner',axis=1)
aaa_df.columns=['ml','moodys']
aaa_df.head()
aaa_df['ml'][:5]
#scatter plot
plt.scatter(aaa_df['ml'],aaa_df['moodys'])
#another way to run a scatterplot
aaa_df.plot(x='ml',y='moodys',kind='scatter')

np.corrcoef(aaa_df['ml'],aaa_df['moodys'])
'''finito'''

'''
Look at correlations and linear relationships between 'spaaa' (# S&P U.S. Issued AA Investment Grade Corporate Bond Index) and 'maaa' (Moodys Index Aaa Bonds)
'''
fig=plt.figure()
'''
plt.xticks(mlccc.index)
locs,labels=plt.xticks()
plt.setp(labels,rotation=45)
'''
plt.plot_date(spaaa.index,spaaa,'b-')
plt.plot_date(spaaa.index,maaa,'g-')
plt.show()

#that graph is terrible... run a scatterplot
#first create a df of the two... will do this via a concatenate function - different from a merge
higrade=pd.concat([spaaa,maaa],axis=1,join='inner') #for some reason this yields values of arrays
higrade.columns=['sp','moodys']
plt.scatter(higrade['sp'],higrade['moodys']) #a nice consistent negative correlation
''' finito'''

'''
Try to explain spaaa and AA-rated Bond Index OAS (ml_aaoas) and Treasury yields... but this will only work if the average maturity/duration of the SPAA matches that of the OAS

some sources:
a) http://www.coffeeandcharts.com/wp/2015/10/06/credit-spreads-update-october-2015-part-12/
b) google: "merrill lynch aa rated oas methodology"
c) grab from ML site: http://www.mlindex.ml.com/gispublic/bin/MLIndex.asp
'''

'''finito'''

'''junk/high yield bonds'''

junk=pd.concat([mlccc,mlhyoas],join='inner',axis=1)
junk.columns=['ccc','hyoas']
plt.figure();junk.plot(); plt.legend(loc='best')

