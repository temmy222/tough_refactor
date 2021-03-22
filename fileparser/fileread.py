import os

from tough_refactor.plotting.plotmultifiles import PlotMultiFiles
from tough_refactor.plotting.plotmultitough import PlotMultiTough
from tough_refactor.plotting.plottough import PlotTough


class FileReadSingle(object):
    def __init__(self, simulatortype, filelocation, filetitle, **kwargs):
        """
        Class for processing single file results
        :type simulatortype: object
        """
        self.filelocation = filelocation
        if isinstance(self.filelocation, str):
            os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.generation = kwargs.get('generation')
        self.full_args = kwargs.get('restart_files')
        self.expt = kwargs.get('experiment')
        self.x_slice_value = kwargs.get('x_slice_value')

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle + ' for ' + self.simulatortype

    def validateFile(self):
        if type(self.filelocation) != type(self.filetitle):
            print('Values can either be strings or lists')

    def getSimulatorType(self):
        return self.simulatortype

    def plotTime(self, param, gridblocknumber, format_of_date='year', labels=None, singlePlot=False, style='horizontal',
                 width=12,
                 height=8):
        if isinstance(param, str):
            plottest = PlotTough(self.simulatortype, self.filelocation, self.filetitle, generation=self.generation,
                                 restart_files=self.full_args,
                                 experiment=self.expt)
            if self.full_args is None:
                plottest.plotParamWithTime(param, gridblocknumber, format_of_date)
            else:
                plottest.plotParamWithTimeRestart(param, gridblocknumber, format_of_date)
        elif isinstance(param, list) and isinstance(self.filelocation, str) and singlePlot is False:
            plottest = PlotMultiTough(self.simulatortype, self.filelocation, self.filetitle, generation=self.generation,
                                      restart_files=self.full_args,
                                      experiment=self.expt)
            if self.full_args is None:
                plottest.multi_time_plot(param, gridblocknumber, format_of_date, style)
            else:
                plottest.multi_time_plot_restart(param, gridblocknumber, format_of_date, style)
        elif isinstance(param, list) and isinstance(self.filelocation, str) and singlePlot is True:
            plottest = PlotMultiTough(self.simulatortype, self.filelocation, self.filetitle, generation=self.generation,
                                      restart_files=self.full_args,
                                      experiment=self.expt,
                                      x_slice_value=self.x_slice_value)
            if self.full_args is None:
                plottest.plotMultiParamSinglePlot(param, gridblocknumber, format_of_date, labels)

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
    file_locations (list of strings) - specifies the location of the files on the system
    file_titles (list of strings) - gives the title of the file e.g 'kdd.conc' or 'OUTPUT.csv
    simulator_type (string) can either be toughreact, tmvoc or tough3
    props (list of strings) -  are the properties to be plotted

    **kwargs
    x_slice value (integer) - if the plot should be sliced a the  x axis
    per_file -  (boolean) - if the plot should be made per file and not per property
    title (list of strings) - title of each of the plots
    """

    def __init__(self, simulator_type, file_locations, file_titles, props, **kwargs):
        assert isinstance(file_locations, list)
        assert isinstance(file_titles, list)
        self.file_locations = file_locations
        self.file_titles = file_titles
        self.simulator_type = simulator_type
        self.props = props
        self.x_slice_value = kwargs.get('x_slice_value')
        self.per_file = kwargs.get('per_file')
        self.title = kwargs.get('title')

    def plotTime(self, grid_block_number, legend, plot_kind='property', format_of_date='day'):
        # TODO write code to slice x axis
        # TODO write code to slice through domain

        """

        :param format_of_date:
        :param grid_block_number: grid block number in mesh
        :type grid_block_number: int
        :param legend:
        :type legend: list
        :param plot_kind:
        :type plot_kind: string
        """
        plottest = PlotMultiFiles(self.simulator_type, self.file_locations, self.file_titles, self.props,
                                  x_slice_value=self.x_slice_value, per_file=self.per_file, title=self.title)
        if len(self.props) == 1:
            plottest.multiFileSinglePlot(grid_block_number, legend)
        else:
            plottest.plotMultiElementMultiFile(grid_block_number, legend, format_of_date, plot_kind)

    def plotTimePerPanel(self, grid_block_number, panels, format_of_date='day'):
        plottest = PlotMultiFiles(self.simulator_type, self.file_locations, self.file_titles, self.props,
                                  x_slice_value=self.x_slice_value, per_file=self.per_file, title=self.title)
        plottest.plotMultiPerPanel(grid_block_number, panels, format_of_date)

    def plotParamWithLayer(self, directionX, directionY, layer_num, time, legend):
        plottest = PlotMultiFiles(self.simulator_type, self.file_locations, self.file_titles, self.props,
                                  x_slice_value=self.x_slice_value, per_file=self.per_file, title=self.title)
        if len(self.props) == 1:
            pass
        else:
            plottest.plotMultiFileDistance(directionX, directionY, time, layer_num, legend)
