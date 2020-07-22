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
import utils.utilities as processor
import fileparser.fileread as fileDetails
import fileparser.tough3 as tough3
import fileparser.toughreact as toughreact


class PlotTough(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        welcome = "welcome to plotting routines"
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype

    def read_file(self):
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            fileReader = tough3.Tough3(self.simulatortype, self.filelocation, self.filetitle)
        else:
            fileReader = toughreact.Toughreact(self.simulatortype, self.filelocation, self.filetitle)
        return fileReader

    def plotParamWithTime(self, param, gridblocknumber):

        fileReader = self.read_file()

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
        time_year = fileReader.convert_times_year()
        result_array = fileReader.get_timeseries_data(param, gridblocknumber)
        fig, axs = plt.subplots(1, 1)
        axs.plot(time_year, result_array, marker='^')
        axs.set_xlabel('Time (year)')
        parameters = processor.Utilities()
        axs.set_ylabel(parameters.param_label_full(param.upper()))
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        CONFIG_PATH = os.path.join(ROOT_DIR, 'mystyle.mplstyle')
        print(CONFIG_PATH)
        plt.style.use(CONFIG_PATH)
        # plt.style.use('./plotting/mystyle.mplstyle')
        # axs.spines['bottom'].set_linewidth(1.5)
        # axs.spines['left'].set_linewidth(1.5)
        # axs.spines['top'].set_linewidth(0)
        # axs.spines['right'].set_linewidth(0)
        # axs.legend(loc='upper right', borderpad=0.1)
        plt.tight_layout()
        plt.show()

    def plotParamWithParam(self, param1, param2, gridblocknumber):

        fileReader = self.read_file()
        result_array_x = fileReader.get_timeseries_data(param1, gridblocknumber)
        result_array_y = fileReader.get_timeseries_data(param2, gridblocknumber)
        fig, axs = plt.subplots(1, 1)
        axs.plot(result_array_x, result_array_y, marker='^')
        axs.set_xlabel('Time (year)')
        parameters = processor.Utilities()
        axs.set_ylabel(parameters.param_label_full(param2.upper()))
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        CONFIG_PATH = os.path.join(ROOT_DIR, 'mystyle.mplstyle')
        print(CONFIG_PATH)
        plt.style.use(CONFIG_PATH)
        plt.tight_layout()
        plt.show()

    def plotstyle(self):
        axs.spines['bottom'].set_linewidth(1.5)
        axs.spines['left'].set_linewidth(1.5)
        axs.spines['top'].set_linewidth(0)
        axs.spines['right'].set_linewidth(0)
        axs.legend(loc='upper right', borderpad=0.1)
