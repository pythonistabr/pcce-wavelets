#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pythonistabr
"""
import numpy as np
from scipy import signal


def butter_filter(
        TimeSerie: np.ndarray,
        FilterOrder: int,
        CutoffPeriod: float,
        btype="") -> np.ndarray:
    
    btype = btype.lower()   
    #Length = len(TimeSerie)
    CutoffFrequency = 1/CutoffPeriod
    Data = np.array(TimeSerie)
    
    if btype not in ["low", "high"]:
        raise ValueError("Select filter type")

    if btype == "low":   #apply low-pass filter   
        B, A = signal.butter(
            FilterOrder, CutoffFrequency, 
            output='ba', analog=False,
            btype="low"
            )
    if btype == "high": #apply high-pass filter
            B, A = signal.butter(
            FilterOrder, CutoffFrequency, 
            output='ba', analog=False,
            btype="high"
            )

    FilteredData = signal.filtfilt(B, A, Data)
    return FilteredData
    

def main():
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    
    def low_pass_test():
        data = pd.read_csv(
            '../data/adcp_formatado/series_unificadas/meridional_total.csv',
            delimiter=';'
            )
        x = data.iloc[0:4392, 25]
        x.interpolate(method="linear",limit=12, inplace=True)
        y = butter_filter(x, 2, 25, btype="low")
        plt.plot(x)
        plt.plot(y)
    
    def high_pass_test():
        data = pd.read_csv(
            '../data/adcp_formatado/series_unificadas/meridional_total.csv',
            delimiter=';'
            )
        x = data.iloc[0:4392, 25]
        x.interpolate(method="linear",limit=12, inplace=True)
        y = butter_filter(x, 2, 25, btype="high")
        plt.plot(x)
        plt.plot(y)
    
#    def no_btype_test():
#        data = pd.read_csv(
#            '../data/adcp_formatado/series_unificadas/meridional_total.csv',
#            delimiter=';'
#            )
#        x = data.iloc[0:4392, 25]
#        x.interpolate(method="linear",limit=12, inplace=True)
#        y = butter_filter(x, 2, 25)
#        plt.plot(x)
#        plt.plot(y)
#        plt.show()
    
    return low_pass_test(), high_pass_test()
    '"""
if __name__ == "__main__":
    main()