import os

from fileparser.tough3 import MultiTough3
from fileparser.toughreact import MultiToughReact
import matplotlib.pyplot as plt

from utils.utilities import Utilities


class PlotMultiFiles(object):
    def __init__(self, simulator_type, file_locations, file_titles, props, **kwargs):
        assert isinstance(file_locations, list)
        assert isinstance(file_titles, list)
        assert isinstance(props, list)
        self.file_locations = file_locations
        self.file_titles = file_titles
        self.simulator_type = simulator_type
        self.props = props
        self.modifier = Utilities()
        self.text = kwargs.get('text')

    def validateInput(self):
        if self.simulator_type.lower() == 'toughreact':
            multi_tough = MultiToughReact(self.simulator_type, self.file_locations, self.file_titles, self.props)
        elif self.simulator_type.lower() == 'tmvoc':
            multi_tough = MultiTough3(self.simulator_type, self.file_locations, self.file_titles, self.props)
        else:
            print("Code only has capability for TOUGHREACT or TOUGH3 (by extension TMVOC)")
        return multi_tough

    def plotRawSingle(self, data, legend):
        prop_index = 0
        fig, axs = plt.subplots(1, 1)
        for i in range(0, len(data.columns), 2):
            x_data = data.iloc[:, i]
            y_data = data.iloc[:, i + 1]
            axs.plot(x_data, y_data, marker='^')
            axs.set_xlabel('Time (year)')
            axs.set_ylabel(self.props[prop_index])
            axs.legend(legend, loc='best')
            axs.ticklabel_format(useOffset=False)
            # prop_index = prop_index + 1
        os.chdir(self.file_locations[0])
        plt.tight_layout()
        plt.show()
        fig.savefig(self.props[0] + ' for different files ' + '.png', bbox_inches='tight', dpi=600)

    def plotRawMulti(self, data, legend):
        fig = plt.figure()
        plot_counter = 1
        start_point = 0
        prop_index = 0
        initial_length = len(self.props) * 2
        for number in range(1, len(self.props)):
            axs = plt.subplot(3, 2, plot_counter)
            legend_index = 0
            for i in range(start_point, initial_length, 2):
                x_data = data.iloc[:, i]
                y_data = data.iloc[:, i + 1]
                axs.plot(x_data, y_data, marker='^', label=legend[legend_index])
                axs.set_xlabel('Time (year)')
                axs.set_ylabel(self.props[prop_index])
                legend_index = legend_index + 1
            plot_counter = plot_counter + 1
            start_point = start_point + (len(self.props) * 2)
            initial_length = initial_length + (len(self.props) * 2)
            prop_index = prop_index + 1
        handles, labels = axs.get_legend_handles_labels()
        plt.figlegend(handles, labels, loc='lower center', ncol=5, labelspacing=0.)
        plt.show()
        fig.savefig(self.props[0] + ' for different files ' + '.png', bbox_inches='tight', dpi=600)

    def plotRawMultiFile(self, data, legend):
        fig = plt.figure(figsize=(10, 8))
        plot_counter = 1
        start_point = 0
        prop_index = 0
        markers = ['^', 'o', 's', 'x', 'd']
        for number in range(1, len(self.props) + 1):
            axs = plt.subplot(3, 2, plot_counter)
            legend_index = 0
            for i in range(start_point, len(data.columns), (len(self.props) * 2)):
                x_data = data.iloc[:, i]
                y_data = data.iloc[:, i + 1]
                axs.plot(x_data, y_data, marker=markers[legend_index], label=legend[legend_index])
                axs.set_xlabel('Time (year)', fontsize=14)
                axs.set_ylabel(self.props[prop_index], fontsize=14)
                axs.ticklabel_format(useOffset=False)
                legend_index = legend_index + 1
            plot_counter = plot_counter + 1
            start_point = start_point + 2
            prop_index = prop_index + 1
        handles, labels = axs.get_legend_handles_labels()
        plt.setp(axs.get_xticklabels(), fontsize=14)
        plt.setp(axs.get_yticklabels(), fontsize=14)
        plt.figlegend(handles, labels, loc='lower center', ncol=4, labelspacing=0.)
        fig.tight_layout()
        plt.show()
        os.chdir(self.file_locations[0])
        print("yes")
        fig.savefig(self.props[0] + ' for different files ' + '.png', bbox_inches='tight', dpi=600)

    def multiFileSinglePlot(self, grid_block_number, legend):
        multi_tough = self.validateInput()
        data = multi_tough.retrieve_data_multi_timeseries(grid_block_number)
        try:
            with plt.style.context('mystyle'):
                self.plotRawSingle(data, legend)
        except:
            with plt.style.context('classic'):
                self.plotRawSingle(data, legend)

    def plotMultiElementMultiFilePerFile(self, grid_block_number, legend):
        multi_tough = self.validateInput()
        data = multi_tough.getMultiElementData(grid_block_number)
        print('Each plot shows results from a file')
        try:
            with plt.style.context('mystyle'):
                self.plotRawMulti(data, legend)
        except:
            with plt.style.context('classic'):
                self.plotRawMulti(data, legend)

    def plotMultiElementMultiFilePerProp(self, grid_block_number, legend):
        multi_tough = self.validateInput()
        data = multi_tough.getMultiElementData(grid_block_number)
        print('Each plot shows results per parameter')
        try:
            with plt.style.context('mystyle'):
                self.plotRawMultiFile(data, legend)
        except:
            with plt.style.context('classic'):
                self.plotRawMultiFile(data, legend)

    def plotMultiElementMultiFile(self, grid_block_number, legend, plot_kind='property'):
        if plot_kind.lower() == 'property':
            self.plotMultiElementMultiFilePerProp(grid_block_number, legend)
        elif plot_kind.lower() == 'file':
            self.plotMultiElementMultiFilePerFile(grid_block_number, legend)
        else:
            print('Plot kind can either be property or file')
