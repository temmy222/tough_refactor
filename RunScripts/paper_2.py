import collections
import itertools
import os

from fileparser import tough3
from fileparser.fileread import FileReadSingle
import numpy as np

loca1 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\flow through brine only"
loca2 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\Second numerical paper\Python Run\Shale-Sand-Shale-Limestone"

filetype_toughreact = 'kdd_conc.tec'

testcodetoughreact = FileReadSingle("toughreact", loca2, filetype_toughreact)

# testcodetoughreact.plot2D('x', 'z', 'pH', 2.592e+10, 'grid')


loca3 = r"C:\Users\tajayi3\Desktop\Research\Coding Practice\write_to_TOUGH\RunScripts"
loca3 = r"C:\Users\tajayi3\OneDrive - Louisiana State University\tmvoc\mymodels\Auto Simulations\AllComponents"
filetype_tmvoc = "OUTPUT_ELEME.csv"

fileReader = tough3.Tough3('tmvoc', loca3, filetype_tmvoc)

# time_year = fileReader.convert_times('day')
# result_array = fileReader.get_timeseries_data('X_Toluen_L', 0)
a = [1, 2, 3, 3, 3, 4, 5, 6, 6]
b = [3, 4, 5, 6, 7, 8, 9, 10,11]


def monotonic(x):
    dx = np.diff(x)
    return np.all(dx > 0)

def del_index(my_list, indexes):
    for index in sorted(indexes, reverse=True):
        del my_list[index]
    return my_list

def f7(seqA, seqB):
    # seen = set()
    # seen_add = seen.add
    # manny = [x for x in seqA if not (x in seen or seen_add(x))]
    # manny2 = [x for x in seqB if not (x in seen or seen_add(x))]
    monotone = monotonic(seqA)
    if not monotone:
        index = dups(seqA)
        seqA= del_index(seqA, index)
        seqB= del_index(seqB, index)
    return seqA, seqB


def dups(sequence):
    dicta = {}
    indexes = []
    dups = collections.defaultdict(list)
    for i, e in enumerate(sequence):
        dups[e].append(i)
    for k, v in sorted(dups.items()):
        if len(v) >= 2:
            dicta[k] = v
    for k,v in dicta.items():
        indexes.append(v[1:])
    return list(itertools.chain.from_iterable(indexes))


manny, manny2 = f7(a, b)
tama = dups(a)
# mon = monotonic(result_array)

print('yes')
