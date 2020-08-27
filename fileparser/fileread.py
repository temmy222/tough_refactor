import os

from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough


class FileRead(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        """

        :type simulatortype: object
        """
        self.filelocation = filelocation
        if isinstance(self.filelocation, str):
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

    def plot_time(self, param, gridblocknumber, labels=[], style='horizontal', width=12, height=8):
        if isinstance(param, str):
            plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
            plottest.plotParamWithTime(param, gridblocknumber)
        elif isinstance(param, list) and isinstance(self.filelocation, str):
            print('yes')
            plottest = PlotMultiTough(self.simulatortype, self.filelocation, self.filetitle)
            plottest.multi_time_plot(param, gridblocknumber, style)
        elif isinstance(param, list) and isinstance(self.filelocation, list):
            plottest = PlotMultiTough(self.simulatortype, self.filelocation, self.filetitle)
            plottest.multi_param_multi_file_plot(param, gridblocknumber, labels, style, width, height)

    def plot_param_with_param(self, param1, param2, gridblocknumber):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithParam(param1, param2, gridblocknumber)

    def plot2D(self, direction1, direction2, param, timer, type='plain'):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        if type == 'plain':
            plottest.plot2D_one(direction1, direction2, param, timer)
        elif type == 'grid':
            plottest.plot2D_withgrid(direction1, direction2, param, timer)
        else:
            print('Type can either be plain or gridded')


class FileReadMultiple(object):
    def __init__(self, simulator_type, file_location, file_title):
        assert isinstance(file_location, list)
        assert isinstance(file_title, list)
        self.file_location = file_location
        self.file_title = file_title
        self.simulator_type = simulator_type
