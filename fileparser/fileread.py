import os

# import fileparser.tough3 as tough3
# import fileparser.toughreact as toughreact
import plotting.plottough as plot


class FileRead(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        """

        :type simulatortype: object
        """
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle + ' for ' + self.simulatortype


    def get_simulatortype(self):
        return self.simulatortype

    def plot_time(self, param, gridblocknumber):
        plottest = plot.PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        print(plottest.plotParamWithTime(param, gridblocknumber))

    def plot_param_with_param(self, param1, param2, gridblocknumber):
        plottest = plot.PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        print(plottest.plotParamWithParam(param1, param2, gridblocknumber))
