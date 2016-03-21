# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:42:18 2016

@author: lechuza
"""

import sys
import Quandl
#sys.path.append('G:/Property/Luis_C/statsLearning')
import numpy as np
import pandas as pd

sys.path.append('/home/lechuza/Documents/economicAnalysis/trading')

maaa = Quandl.get("MOODY/DAAAYLD", returns="pandas", trim_start="2014-01-02", trim_end="2016-02-20")

#should track closely with the US AA-rated Bond Index OAS:
ml_aaoas = Quandl.get("ML/AAOAS", returns="pandas", trim_start="2015-01-02")

#appears to be an index based on daily total returns
# S&P U.S. Issued AA Investment Grade Corporate Bond Index
spaaa = Quandl.get("SPDJ/SPUSG2AT", trim_start="2014-01-02", trim_end="2016-02-20")

#moody's?
baa = Quandl.get("MOODY/DBAAYLD", returns="pandas", trim_start="2014-01-02", trim_end="2016-02-17")

'''
Merrill Lynch CCC-rated Bond Index Yield
ML offers:
- CCC-rated Bond Index Yield
- CCC Bond Total Return Index
- US High Yield BB Corporate Index Yield
'''
mlccc=Quandl.get("ML/CCCY",returns="pandas",trim_start="2012-01-02")

mlhyoas = Quandl.get("ML/HYOAS", trim_start="2012-01-02")


scorr=MeasureAutoCorr(mlccc)
scorr.timeFrame() #should return a list of p-values from running 5-day serial correlation tests
