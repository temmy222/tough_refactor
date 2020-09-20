import os

from plotting.plotmultifiles import PlotMultiFiles
from plotting.plotmultitough import PlotMultiTough
from plotting.plottough import PlotTough


class FileReadSingle(object):
    def __init__(self, simulatortype, filelocation, filetitle, *args):
        """
        Class for processing single file results
        :type simulatortype: object
        """
        self.filelocation = filelocation
        if isinstance(self.filelocation, str):
            os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.args = args
        print(len(self.args))

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle + ' for ' + self.simulatortype

    def validateFile(self):
        if type(self.filelocation) != type(self.filetitle):
            print('Values can either be strings or lists')

    def getSimulatorType(self):
        return self.simulatortype

    def plotTime(self, param, gridblocknumber, format_of_date='year', labels=[], style='horizontal', width=12, height=8):
        if isinstance(param, str):
            plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle, self.args)
            if len(self.args) == 0:
                plottest.plotParamWithTime(param, gridblocknumber, format_of_date)
            else:
                plottest.plotParamWithTimeRestart(param, gridblocknumber, format_of_date)
        elif isinstance(param, list) and isinstance(self.filelocation, str):
            plottest = PlotMultiTough(self.simulatortype, self.filelocation, self.filetitle)
            plottest.multi_time_plot(param, gridblocknumber, format_of_date, style)

    def plotParamWithParam(self, param1, param2, gridblocknumber):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithParam(param1, param2, gridblocknumber)

    def plotParamWithLayer(self, directionXAxis, directionYAxis, param, layer_num, time):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        plottest.plotParamWithLayer(directionXAxis, directionYAxis, param, layer_num, time)

    def plot2D(self, direction1, direction2, param, timer, grid_type='plain'):
        plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle)
        if grid_type == 'plain':
            plottest.plot2D_one(direction1, direction2, param, timer)
        elif grid_type == 'grid':
            plottest.plot2D_withgrid(direction1, direction2, param, timer)
        else:
            print('Type can either be plain or grid')


class FileReadMultiple(object):
    """
    Class for processing multiple file results
    """
    def __init__(self, simulator_type, file_locations, file_titles, props):
        assert isinstance(file_locations, list)
        assert isinstance(file_titles, list)
        self.file_locations = file_locations
        self.file_titles = file_titles
        self.simulator_type = simulator_type
        self.props = props

    def plotTime(self, grid_block_number, legend, plot_kind='property'):
        """

        :param grid_block_number:
        :type grid_block_number: int
        :param legend:
        :type legend: list
        :param plot_kind:
        :type plot_kind: string
        """
        plottest = PlotMultiFiles(self.simulator_type, self.file_locations, self.file_titles, self.props)
        if len(self.props) == 1:
            plottest.multiFileSinglePlot(grid_block_number, legend)
        else:
            plottest.plotMultiElementMultiFile(grid_block_number, legend, plot_kind)
