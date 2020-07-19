import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.ticker as ticker
from random import randrange
import random
from scipy import interpolate
from scipy.interpolate import griddata
import fileparser.fileread as input


class PlotTough(object):
    def __init__(self):
        welcome = "welcome to plotting routines"

    def plot_time(self, param, gridblocknumber, time_year, result_array):
        fig = plt.figure()
        fig, axs = plt.subplots(1, 1)
        # result_array = self.choplist(result_array)
        # time_year = self.choplist(time_year)
        # plt.plot(time_year,result_array)
        # plt.xlabel('Time (year)')
        # plt.ylabel(self.param_label_full(param.upper()))
        # plt.spines['bottom'].set_linewidth(1.5)
        # plt.spines['left'].set_linewidth(1.5)
        # plt.spines['top'].set_linewidth(0.2)
        # plt.spines['right'].set_linewidth(0.2)
        # axs.plot(time_year, result_array, marker='^', label=self.param_label_full(param.upper()))
        axs.plot(time_year, result_array, marker='^')
        axs.set_xlabel('Time (year)')
        # axs.set_ylabel(self.param_label_full(param.upper()))
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        CONFIG_PATH = os.path.join(ROOT_DIR, 'mystyle.mplstyle')
        plt.style.use(CONFIG_PATH)
        # axs.spines['bottom'].set_linewidth(1.5)
        # axs.spines['left'].set_linewidth(1.5)
        # axs.spines['top'].set_linewidth(0)
        # axs.spines['right'].set_linewidth(0)
        # axs.legend(loc='upper right', borderpad=0.1)
        plt.show()

    def plotstyle(self):
        axs.spines['bottom'].set_linewidth(1.5)
        axs.spines['left'].set_linewidth(1.5)
        axs.spines['top'].set_linewidth(0)
        axs.spines['right'].set_linewidth(0)
        axs.legend(loc='upper right', borderpad=0.1)

