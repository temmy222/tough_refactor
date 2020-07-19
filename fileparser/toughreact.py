import csv
import os
import pytough.t2listing as toughreact
import utils.utilities as fileprocessor

class Toughreact(object):
    def __init__(self, simulatortype, filelocation, filetitle,blocks):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle +  ' for ' + self.simulatortype

    def get_blocks(self):
        tre1 = fileprocessor.Utilities(self.filelocation, 'CONNE')
        tre1.findword()
        tre1.sliceoffline()
        tre1.sliceofffile()
        tre1.writetofile()
        with open('test.txt') as f:
            grid_blocks = f.read().splitlines()
        return grid_blocks

    def get_times(self):
        data = toughreact.toughreact_tecplot(self.filetitle, self.get_blocks())
        time_data = data.get_time()
        return time_data