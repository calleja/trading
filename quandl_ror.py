# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:58:10 2016

@author: CallejaL
"""
import pandas as pd
import numpy as np
import datetime as dt

class RateReturn(object):
    def __init__(self,theArray):
        self.arrays=theArray
        self.numRows=len(self.arrays)
    def cycleReturn(self,no,fromDate):
        #'fromDate' must be a string of format "MM/DD/YYYY"
    #'no' is the number of days over which to calculate the r.o.r.
        ma=dt.datetime.strptime(fromDate,"%m/%d/%Y")
        pos=self.arrays.index.get_loc(ma)
        #compile a list of indexes (of position) to which we calculate a r.o.r.       
        ror_indexes=np.arange(pos,numRows,step=no)
        #cycle through each day range interval and calculate ror
    def oneTimeReturn(self,no,fromDate):
        #'fromDate' must be a string of format "MM/DD/YYYY"
    #'no' is the number of days over which to calculate the r.o.r.
        ma=dt.datetime.strptime(fromDate,"%m/%d/%Y")
        pos=self.arrays.index.get_loc(ma)
        #compile a list of indexes (of position) to which we calculate a r.o.r.       
        terminal=pos+no
        assert terminal<=self.numRows, "You are at the bottom of the historical data table"
        
        ror=self.arrays.iloc[terminal]/self.arrays.iloc[pos]-1
        return ror
            
        
       
'''testing       
ma=dt.datetime.strptime('01/06/2014',"%m/%d/%Y")
maaa.index.get_indexer_for(maaa.ix[ma].index)
maaa.ix[ma]
maaa[maaa.index==ma]
maaa.index.get_loc(ma) #reproduces the row number
maaa[:5]


maaa.index[2]
type(maaa.index[2])
type(maaa) 
'''