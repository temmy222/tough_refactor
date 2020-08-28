import os

from plotting.plotmultifiles import PlotMultiFiles
from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough


class FileReadSingle(object):
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

    def validateFile(self):
        if type(self.filelocation) != type(self.filetitle):
            print('Values can either be strings or lists')

    def getSimulatorType(self):
        return self.simulatortype

    def plotTime(self, param, gridblocknumber, labels=[], style='horizontal', width=12, height=8):
        if isinstance(param, str):
            plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
            plottest.plotParamWithTime(param, gridblocknumber)
        elif isinstance(param, list) and isinstance(self.filelocation, str):
            plottest = PlotMultiTough(self.simulatortype, self.filelocation, self.filetitle)
            plottest.multi_time_plot(param, gridblocknumber, style)

    def plotParamWithParam(self, param1, param2, gridblocknumber):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithParam(param1, param2, gridblocknumber)

    def plotParamWithLayer(self, directionXAxis, directionYAxis, param, layer_num, time):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithLayer(directionXAxis, directionYAxis, param, layer_num, time)

    def plot2D(self, direction1, direction2, param, timer, type='plain'):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        if type == 'plain':
            plottest.plot2D_one(direction1, direction2, param, timer)
        elif type == 'grid':
            plottest.plot2D_withgrid(direction1, direction2, param, timer)
        else:
            print('Type can either be plain or gridded')


class FileReadMultiple(object):
    def __init__(self, simulator_type, file_locations, file_titles, props):
        assert isinstance(file_locations, list)
        assert isinstance(file_titles, list)
        self.file_locations = file_locations
        self.file_titles = file_titles
        self.simulator_type = simulator_type
        self.props = props

    def plotTime(self, grid_block_number, legend, plot_kind='property'):
        plottest = PlotMultiFiles(self.simulator_type, self.file_locations, self.file_titles, self.props)
        if len(self.props) == 1:
            plottest.multiFileSinglePlot(grid_block_number, legend)
        else:
            plottest.plotMultiElementMultiFile(grid_block_number, legend, plot_kind)
