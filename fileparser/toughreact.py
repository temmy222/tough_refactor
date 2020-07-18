import csv
import os
import pytough.t2listing as toughreact

class Toughreact(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.file_as_list = []

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle +  ' for ' + self.simulatortype

    def get_times(self):
        data = toughreact.toughreact_tecplot()
        time_data = data.get_time()
        return time_data