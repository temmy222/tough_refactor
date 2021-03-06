import collections
import itertools
import os

from fileparser import tough3
from fileparser.fileread import FileReadSingle
import numpy as np

loca1 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\flow through brine only"
loca2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\Python Run\Shale-Sand-Shale-Limestone"
loca3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\Python Run\Limestone-Dolomite-Limestone-Limestone"
loca4 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\Python Run\An-Gy-Hal-Hal"

filetype_toughreact = 'kdd_conc.tec'

testcodetoughreact = FileReadSingle("toughreact", loca4, filetype_toughreact)

testcodetoughreact.plot2D('x', 'z', 'pH', 2.592e+2, 'grid')


loca3 = r"C:\Users\tajayi3\Desktop\Research\Coding Practice\write_to_TOUGH\RunScripts"
#loca3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Auto Simulations\AllComponents"
filetype_tmvoc = "OUTPUT_ELEME.csv"

# fileReader = tough3.Tough3('tmvoc', loca3, filetype_tmvoc)
#
# time_year = fileReader.convert_times('day')
# result_array = fileReader.get_timeseries_data('X_Toluen_L', 0)
