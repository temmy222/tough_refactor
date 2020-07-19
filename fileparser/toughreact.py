import csv
import os
import pytough.t2listing as toughreact
import utils.utilitiestoughreact as fileprocessor
import utils.utilities as processor
import plotting.plottough as plot
from collections import OrderedDict

class Toughreact(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.data = toughreact.toughreact_tecplot(self.filetitle, self.get_elements())

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle +  ' for ' + self.simulatortype

    def get_elements(self):
        tre1 = fileprocessor.UtilitiesToughreact(self.filelocation, 'CONNE')
        tre1.findword()
        tre1.sliceoffline()
        tre1.writetofile()
        with open('test.txt') as f:
            grid_blocks = f.read().splitlines()
        return grid_blocks


    def get_times(self):
        time_data = self.data.times
        time_data= list(time_data)
        value = processor.Utilities()
        time_data=value.choplist(time_data, 40)
        return time_data

    def convert_times_year(self):
        intermediate = self.get_times()
        firstusage = processor.Utilities()
        timeyear = firstusage.convert_times_year(intermediate)
        print('test')
        return timeyear

    def get_timeseries_data(self, param, gridblocknumber):
        grid = self.get_elements()[gridblocknumber]
        mf = self.data.history([(grid, param)])
        timeseries = mf[1]
        timeseries = list(timeseries)
        value = processor.Utilities()
        timeseries=value.choplist(timeseries, 40)
        return timeseries

    def plot_time(self, param, gridblocknumber):
        result_array = self.get_timeseries_data(param, gridblocknumber)
        time_year = self.convert_times_year()
        plotting = plot.PlotTough()
        plotting.plot_time(param, gridblocknumber, time_year, result_array)
