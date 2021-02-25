import math
import os

from tough_refactor.fileparser.tough3 import MultiTough3
from tough_refactor.fileparser.toughreact import MultiToughReact
import matplotlib.pyplot as plt

from tough_refactor.utils.utilities import Utilities


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
        self.x_slice_value = kwargs.get('x_slice_value')
        self.per_file = kwargs.get('per_file')
        self.title = kwargs.get('title')

    def validateInput(self):
        if self.simulator_type.lower() == 'toughreact':
            multi_tough = MultiToughReact(self.simulator_type, self.file_locations, self.file_titles, self.props,
                                          x_slice_value=self.x_slice_value)
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
            axs.set_xlabel('Time (year)', fontsize=14)
            axs.set_ylabel(self.props[prop_index], fontsize=14)
            axs.legend(legend, loc='best')
            axs.ticklabel_format(useOffset=False)
            # prop_index = prop_index + 1
        plt.setp(axs.get_xticklabels(), fontsize=14)
        plt.setp(axs.get_yticklabels(), fontsize=14)
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
        plt.setp(axs.get_xticklabels(), fontsize=14)
        plt.setp(axs.get_yticklabels(), fontsize=14)
        plt.figlegend(handles, labels, loc='lower center', ncol=5, labelspacing=0.)
        plt.show()
        fig.savefig(self.props[0] + ' for different files ' + '.png', bbox_inches='tight', dpi=600)

    def setToughYLabel(self, value):
        if 'tobermorite(' in value:
            value = 'Tobermorite'
        elif 'monosulfoalu' in value:
            value = 'Monosulfoaluminate'
        elif 'katoite' in value:
            value = 'Katoite'
        if 'pH' not in value:
            value = value.capitalize()
        if 'C3fh6' in value:
            value = 'C3FH6'
        if self.simulator_type =='tmvoc':
            value = value.upper()
        return value

    def plotRawMultiFile(self, data, legend, format_of_date):
        fig = plt.figure(figsize=(10, 10))
        plot_counter = 1
        start_point = 0
        prop_index = 0
        markers = ['^', 'o', 's', 'x', 'd']
        for number in range(1, len(self.props) + 1):
            if number == 4:
                trye = axs
            axs = plt.subplot(math.ceil(len(self.props) / 2)+1, 2, plot_counter)
            legend_index = 0
            for i in range(start_point, len(data.columns), (len(self.props) * 2)):
                x_data = data.iloc[:, i]
                y_data = data.iloc[:, i + 1]
                axs.plot(x_data, y_data, marker=markers[legend_index], label=legend[legend_index])
                axs.set_xlabel('Time ' + '(' + format_of_date + ')', fontsize=14)
                axs.set_ylabel(self.setToughYLabel(self.props[prop_index]), fontsize=14)
                axs.ticklabel_format(useOffset=False)
                legend_index = legend_index + 1
            plot_counter = plot_counter + 1
            start_point = start_point + 2
            prop_index = prop_index + 1
            plt.setp(axs.get_xticklabels(), fontsize=14)
            plt.setp(axs.get_yticklabels(), fontsize=14)
        handles, labels = axs.get_legend_handles_labels()
        fig.tight_layout()
        if len(self.props) > 3:
            # plt.subplots_adjust(bottom=0.5)
            # plt.figlegend(handles, labels, loc='lower center', bbox_to_anchor=(0, -0.1, 1, 1))
            plt.figlegend(handles, labels, loc='lower center', ncol=4, labelspacing=0.)

            # plt.legend(handles, labels, loc='lower right', bbox_to_anchor=(1.05, -0.3), fancybox=False, shadow=False,
            #            ncol=4)
            # plt.subplots_adjust(top=0.85, wspace=0.001, right=0.97, left=-0.07)
            # plt.setp(axs.get_legend().get_texts(), fontsize='14')

        else:
            plt.figlegend(handles, labels, loc='lower center', ncol=4, labelspacing=0.)
        # fig.tight_layout(pad=0)
        # axs.legend(ncol=4, bbox_to_anchor=(1, -0.1))
        # lastSubplot = plt.subplot(1, 1, 1)
        # lastSubplot.set_frame_on(False)
        # lastSubplot.get_xaxis().set_visible(False)
        # lastSubplot.get_yaxis().set_visible(False)
        # plt.plot(0, 0, marker='o', color='r', label='line1')
        # plt.plot(0, 0, marker='o', color='b', label='line2')
        # lastSubplot.legend(loc='lower right')
        plt.show()
        os.chdir(self.file_locations[0])
        fig.savefig(self.props[0] + ' for different files ' + '.png', bbox_inches='tight', dpi=600)

    def plotRawMultiFilePerFile(self, data, legend):
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
                if "Porosity" in data.columns[i]:
                    # ax2s = axs.twinx()
                    # ax2s.plot(x_data, y_data, marker=markers[legend_index], label=self.setToughYLabel(legend[legend_index]), color='k')
                    # ax2s.set_xlabel('Time (year)', fontsize=14)
                    # ax2s.set_ylabel("Porosity", fontsize=14)
                    # ax2s.set_ylim(0.2, 0.45)
                    axs.plot(x_data, y_data, marker=markers[legend_index],
                             label=self.setToughYLabel(legend[legend_index]))
                    axs.set_xlabel('Time (year)', fontsize=14)
                    axs.set_ylabel("Change in volume fraction", fontsize=14)
                else:
                    axs.plot(x_data, y_data, marker=markers[legend_index], label=self.setToughYLabel(legend[legend_index]))
                    axs.set_xlabel('Time (year)', fontsize=14)
                    axs.set_ylabel("Change in volume fraction", fontsize=14)
                axs.ticklabel_format(useOffset=False)
                plt.setp(axs.get_xticklabels(), fontsize=14)
                plt.setp(axs.get_yticklabels(), fontsize=14)
                legend_index = legend_index + 1
            # axs.set_title(self.title[prop_index], fontsize='14')
            axs.set_title(self.props[prop_index], fontsize='14')
            plot_counter = plot_counter + 1
            start_point = start_point + 2
            prop_index = prop_index + 1
        handles, labels = axs.get_legend_handles_labels()
        # handles2, labels2 = ax2s.get_legend_handles_labels()
        # handles.append(handles2[0])
        # labels.append(labels2[0])
        plt.figlegend(handles, labels, loc='lower center', ncol=4, labelspacing=0.)
        fig.tight_layout()
        plt.show()
        os.chdir(self.file_locations[0])
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

    def plotMultiElementMultiFilePerFile(self, grid_block_number, legend, format_of_date):
        multi_tough = self.validateInput()
        data = multi_tough.getMultiElementData(grid_block_number)
        print('Each plot shows results from a file')
        try:
            with plt.style.context('mystyle'):
                self.plotRawMultiFilePerFile(data, legend)
        except:
            with plt.style.context('classic'):
                self.plotRawMultiFilePerFile(data, legend)

    def plotMultiElementMultiFilePerProp(self, grid_block_number, legend, format_of_date):
        multi_tough = self.validateInput()
        data = multi_tough.getMultiElementData(grid_block_number, format_of_date)
        print('Each plot shows results per parameter')
        try:
            with plt.style.context('mystyle'):
                self.plotRawMultiFile(data, legend, format_of_date)
        except:
            with plt.style.context('classic'):
                self.plotRawMultiFile(data, legend, format_of_date)

    def plotMultiElementMultiFile(self, grid_block_number, legend, format_of_date, plot_kind='property'):
        if plot_kind.lower() == 'property':
            self.plotMultiElementMultiFilePerProp(grid_block_number, legend, format_of_date)
        elif plot_kind.lower() == 'file':
            self.plotMultiElementMultiFilePerFile(grid_block_number, legend, format_of_date)
        else:
            print('Plot kind can either be property or file')

    def plotMultiFileDistance(self, directionX, directionY, time, layer_num, legend):
        multi_tough = self.validateInput()
        data = multi_tough.getMultiFileDistance(directionX, directionY, time, layer_num)
        if self.per_file is True:
            try:
                with plt.style.context('mystyle'):
                    self.plotRawMultiFilePerFile(data, legend)
            except:
                with plt.style.context('classic'):
                    self.plotRawMultiFilePerFile(data, legend)
        else:
            try:
                with plt.style.context('mystyle'):
                    self.plotRawMultiFile(data, legend)
            except:
                with plt.style.context('classic'):
                    self.plotRawMultiFile(data, legend)
