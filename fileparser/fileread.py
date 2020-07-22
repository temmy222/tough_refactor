import os

import fileparser.tough3 as tough3
import fileparser.toughreact as toughreact


class FileRead(object):

    @classmethod
    def __init__(self, simulatortype, filelocation, filetitle):
        """

        :type simulatortype: object
        """
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            self.filereader = tough3.Tough3(self.simulatortype, self.filelocation, self.filetitle)
        else:
            self.filereader = toughreact.Toughreact(self.simulatortype, self.filelocation, self.filetitle)

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle + ' for ' + self.simulatortype

    def read_file(self):
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            filereader = tough3.Tough3(self.simulatortype, self.filelocation, self.filetitle)
        else:
            filereader = toughreact.Toughreact(self.simulatortype, self.filelocation, self.filetitle)

    def get_simulatortype(self):
        return self.simulatortype

    def plot_time(self, param, gridblocknumber):
        self.filereader.plot_time(param, gridblocknumber)
