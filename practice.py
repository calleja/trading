# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:44:40 2016
@author: CallejaL

practice.py
"""

import sys
import Quandl
sys.path.append('G:/Property/Luis_C/statsLearning')
sys.path.append('/home/lechuza/Documents/economicAnalysis/trading')
import sma as sma 
import testOut as to
import numpy as np
import imp
import pandas as pd
from datetime import datetime

maaa = Quandl.get("MOODY/DAAAYLD", returns="pandas", trim_start="2014-01-02", trim_end="2016-02-20")
maaa[-1:].values[0][0]
moodys=sma.SMA(maaa)
aaoas=sma.SMA(ml_aaoas)
ml_aaoas.ix[-1:,0]
aaoas.status()

str(maaa.index[-1:].values[0])
str(maaa[-1:].index.values[0])
maaa.index[-1:].values[0]
pd.Series(maaa.index)[-1:]

moodys.dayChoose(5)

imp.reload(sma)
mlhyoas = Quandl.get("ML/HYOAS", trim_start="2015-01-02")
ml=sma.SMA(mlhyoas,'d')
ml.sma2sma() #unhashable type: 'slice'
meet=to.sma2sma(mlhyoas)

np.mean(maaa.ix[-5:,0])

#list all attributes
dir(sma)

df=to.dayChoose(maaa,5)
#test=to.dayTime(maaa)
type(df)
df.columns=['SMA']
print(df)

del(to) #run this if you wish to reimport with amended code
del(ml)
imp.reload(to)
imp.reload(sma)
