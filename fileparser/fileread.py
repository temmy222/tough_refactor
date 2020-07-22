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

    def validatefile(self):
        if type(self.filelocation) != type(self.filetitle):
            print('Values can either be strings or lists')

    def get_simulatortype(self):
        return self.simulatortype

    def plot_time(self, param, gridblocknumber):
        plottest = plot.PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithTime(param, gridblocknumber)

    def plot_param_with_param(self, param1, param2, gridblocknumber):
        plottest = plot.PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithParam(param1, param2, gridblocknumber)

    def plot2D(self, direction1, direction2, param, timer, type='plain'):
        plottest = plot.PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        if type == 'plain':
            plottest.plot2D_one(direction1, direction2, param, timer)
        elif type == 'grid':
            plottest.plot2D_withgrid(direction1, direction2, param, timer)
        else:
            print('Type can either be plain or gridded')
