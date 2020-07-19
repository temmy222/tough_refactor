import csv
import os
import pytough.t2listing as toughreact
import utils.utilitiestoughreact as fileprocessor
import utils.utilities as processor

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
        return time_data

    def convert_times_year(self):
        intermediate = self.get_times()
        firstusage = processor.Utilities()
        timeyear = firstusage.convert_times_year(intermediate)
        return timeyear

    def get_timeseries_data(self, param, gridblocknumber):
        grid = self.get_elements()[gridblocknumber]
        mf = self.data.history([(grid, param)])
        timeseries = mf[1]
        return timeseries
