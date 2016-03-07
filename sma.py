# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:37:32 2016

@author: CallejaL

Simple moving average
"""
import numpy as np, pandas as pd

import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

class SMA(object):
    def __init__(self,prices):
        self.precios=prices #an array of prices
        self.today=self.precios[-1:]        
        self.todayPrice=self.today.values[0][0]
        self.toDate=str(self.today.index.values[0])
    def status(self):
     #create a rolling day-day moving average
        #roll=pd.rolling_mean(self.precios,days)
        three=np.mean(self.precios.ix[-3:,0])
        three_above=self.todayPrice>three
        fi=np.mean(self.precios.ix[-5:,0])
        fi_above=self.todayPrice>fi
        te=np.mean(self.precios.ix[-10:,0])
        te_above=self.todayPrice>te
        thirty=np.mean(self.precios.ix[-30:,0])
        thirty_above=self.todayPrice>thirty

        #convert to dictionary        
        d={'three': [three,three_above],'five':[fi,fi_above],'ten':[te,te_above]}
        df=pd.DataFrame.from_dict(data=d,orient='index')
        df.columns=['SMA','Current is above']
        
        return df
    def testy(self):
        return self.precios.ix[-3:,0]
        # np.mean(self.precios.ix[-3:,0])
        '''
        self.precios[-days:]/days #rolling average
        vec=1/days
        np.convolve()

        #not exactly working properly
        maaa.shape
        test=maaa.iloc[:,0]
        test1=np.convolve(test,np.ones(3,)/3,mode='valid')[2:]
        test.head()
        test1[0:5]
        type(test1)
        
        np.cumsum(test[:3])/3
        roll=pd.rolling_mean(test,3)
        roll1=pd.rolling_mean(maaa,3)
        
        test[:3]
        test[0:1]
        roll1[0:5]
        '''