# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:30:38 2016
Program that systematically tests for autocorrelation in time series data
Study the distribution of serial correlation
@author: lechuza
"""
from statsmodels.tsa.stattools import adfuller

class MeasureAutoCorr(object):
    def __init__(self,ts):
        self.si=len(ts)
        self.ts=ts
    def timeFrame(self):
        tf=[5,10,20,30,45]#timeframes on which we check p-levels of serial correlation
        start=0
        end=0
        pList=[]
        end=end+(self.tf[0]-1)
        while end<self.si:
        #for i in tf - work on this later... this is looping through all the different timeframes and constructing independent distributions on each
        
            slic=self.ts[start:end]
        #create a slice of the series/df on which to test
            _, pvalue, _, _, _, _=adfuller(slic)
        
        #container for all the p-values... a list should be fine
            pList.append(pvalue)
            start=end
            end=end+tf[0]
        return pList
            
        #def plotDistribution(self):
            
        
