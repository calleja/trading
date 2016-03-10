# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:37:32 2016
@author: CallejaL
Simple moving average

sma.py
"""
import numpy as np, pandas as pd

import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

class SMA(object):
    def __init__(self,prices,dtype):
        #dtype=whether dataframe or numpy series
        self.precios=prices #a df of prices
        self.today=self.precios[-1:]        
        self.todayPrice=self.today.values[0][0]
        self.toDate=str(self.today.index.values[0])
        self.dtype=dtype #pandas or numpy array
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
    def sma2sma(self):
        three=np.mean(self.precios.ix[-3:,0])
        five=np.mean(self.precios.ix[-5:,0])
        ten=np.mean(self.precios.ix[-10:,0])
        thirty=np.mean(self.precios.ix[-30:,0])
        
        thre_fiv=three>five
        thre_ten=three>ten
        fi_ten=five>ten
        ten_thirty=ten>thirty
        
        d={'thre_fiv':['three-day SMA > five-day SMA',thre_fiv],'thre_ten':['three-day SMA > ten-day',thre_ten], 'fi_ten':['five-day SMA > ten-day',fi_ten],'ten_thirty':['ten-day SMA > thirty-day',ten_thirty]}
        
        df=pd.DataFrame.from_dict(data=d,orient='index')
        df.columns=['SMA Comparison','Is Short term Above LT']
        
        return df
        
''' next steps: level of difference between SMAs... average length of time before crosses'''