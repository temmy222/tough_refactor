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
        time_data = list(time_data)
        value = processor.Utilities()
        time_data = value.choplist(time_data, 40)
        return time_data

    def convert_times_year(self):
        intermediate = self.get_times()
        firstUsage = processor.Utilities()
        timeyear = firstUsage.convert_times_year(intermediate)
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

    def get_element_data(self, time, param):
        self.data.set_time(time)
        final_data = self.data.element[param]
        return final_data

    def get_X_data(self, time):
        return self.get_element_data(time, 'X(m)')

    def get_Y_data(self, time):
        return self.get_element_data(time, 'Y(m)')

    def get_Z_data(self, time):
        return self.get_element_data(time, 'Z(m)')

    def get_coord_data(self, direction, timer):
        if direction.lower() == 'x':
            value = self.get_X_data(timer)
        elif direction.lower() == 'y':
            value = self.get_Y_data(timer)
        elif direction.lower() == 'z':
            value = self.get_Z_data(timer)
        else:
            print("coordinates can either be X, Y or Z")
        return value

