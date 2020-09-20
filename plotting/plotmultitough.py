import utils.utilities as processor
import os
import numpy as np
import matplotlib.pyplot as plt

from fileparser import tough3, toughreact
from fileparser.toughreact import MultiToughReact


class PlotMultiTough(object):
    def __init__(self, simulatortype, filelocations, filetitles):
        self.filelocations = filelocations
        self.filetitles = filetitles
        self.simulatortype = simulatortype
        self.modifier = processor.Utilities()

    def read_file(self):
        os.chdir(self.filelocations)
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            fileReader = tough3.Tough3(self.simulatortype, self.filelocations, self.filetitles)
        else:
            fileReader = toughreact.ToughReact(self.simulatortype, self.filelocations, self.filetitles)
        return fileReader

    def read_file_multi(self, file, filetitle):
        os.chdir(file)
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            fileReader = tough3.Tough3(self.simulatortype, file, filetitle)
        else:
            fileReader = toughreact.ToughReact(self.simulatortype, file, filetitle)
        return fileReader

    def multi_time_plot(self, param, gridblocknumber, format_of_date, style='horizontal'):
        fileReader = self.read_file()
        time_year = fileReader.convert_times(format_of_date)
        j = 0
        if style.lower() == 'horizontal':
            if isinstance(param, list) and len(param) < 3:
                try:
                    with plt.style.context('mystyle'):
                        fig = plt.figure()
                        fig, axs = plt.subplots(len(param), sharex=False)
                        for parameter in param:
                            result_array = fileReader.get_timeseries_data(parameter, gridblocknumber)
                            axs[j].plot(time_year, result_array, marker='^',
                                        label=self.modifier.param_label_full(parameter.upper()))
                            axs[j].set_ylabel(self.modifier.param_label_full(parameter.upper()), fontsize=12)
                            axs[j].spines['bottom'].set_linewidth(1.5)
                            axs[j].spines['left'].set_linewidth(1.5)
                            axs[j].spines['top'].set_linewidth(0)
                            axs[j].spines['right'].set_linewidth(0)
                            # axs[j].legend(loc='best',borderpad=0.1)
                            if format_of_date.lower() == 'year':
                                axs[j].set_xlabel('Time (year)', fontsize=12)
                            elif format_of_date.lower() == 'day':
                                axs[j].set_xlabel('Time (day)', fontsize=12)
                            elif format_of_date.lower() == 'hour':
                                axs[j].set_xlabel('Time (hour)', fontsize=12)
                            elif format_of_date.lower() == 'min':
                                axs[j].set_xlabel('Time (min)', fontsize=12)
                            axs[j].ticklabel_format(useOffset=False)
                            plt.setp(axs[j].get_xticklabels(), fontsize=12)
                            plt.setp(axs[j].get_yticklabels(), fontsize=12)
                            j = j + 1
                        plt.tight_layout()
                        plt.show()
                        fig.savefig('Multi plot' + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)
                except:
                    with plt.style.context('classic'):
                        fig = plt.figure()
                        fig, axs = plt.subplots(len(param), sharex=False)
                        for parameter in param:
                            result_array = fileReader.get_timeseries_data(parameter, gridblocknumber)
                            axs[j].plot(time_year, result_array, marker='^',
                                        label=self.modifier.param_label_full(parameter.upper()))
                            axs[j].set_ylabel(self.modifier.param_label_full(parameter.upper()), fontsize=12)
                            axs[j].spines['bottom'].set_linewidth(1.5)
                            axs[j].spines['left'].set_linewidth(1.5)
                            axs[j].spines['top'].set_linewidth(0)
                            axs[j].spines['right'].set_linewidth(0)
                            # axs[j].legend(loc='best',borderpad=0.1)
                            if format_of_date.lower() == 'year':
                                axs[j].set_xlabel('Time (year)', fontsize=12)
                            elif format_of_date.lower() == 'day':
                                axs[j].set_xlabel('Time (day)', fontsize=12)
                            elif format_of_date.lower() == 'hour':
                                axs[j].set_xlabel('Time (hour)', fontsize=12)
                            elif format_of_date.lower() == 'min':
                                axs[j].set_xlabel('Time (min)', fontsize=12)
                            axs[j].ticklabel_format(useOffset=False)
                            plt.setp(axs[j].get_xticklabels(), fontsize=12)
                            plt.setp(axs[j].get_yticklabels(), fontsize=12)
                            j = j + 1
                        plt.tight_layout()
                        plt.show()
                        fig.savefig('Multi plot' + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)

            else:
                print("Parameters must be a list of parameter values with parameters less than 3")
        elif style.lower() == 'vertical':
            if isinstance(param, list) and len(param) < 3:
                with plt.style.context('mystyle'):
                    fig = plt.figure()
                    for number in range(1, len(param) + 1):
                        ax = fig.add_subplot(1, len(param), number)
                        result_array = fileReader.get_timeseries_data(param[number - 1], gridblocknumber)
                        ax.plot(time_year, result_array, marker='^',
                                label=self.modifier.param_label_full(param[number - 1].upper()))
                        ax.set_ylabel(self.modifier.param_label_full(param[number - 1].upper()), fontsize=12)
                        ax.spines['bottom'].set_linewidth(1.5)
                        ax.spines['left'].set_linewidth(1.5)
                        ax.spines['top'].set_linewidth(0)
                        ax.spines['right'].set_linewidth(0)
                        # ax.ticklabel_format(useOffset=False,style='plain')
                        ax.ticklabel_format(useOffset=False)
                        plt.setp(ax.get_xticklabels(), fontsize=12)
                        plt.setp(ax.get_yticklabels(), fontsize=12)
                        # ax.legend(loc='best',borderpad=0.1)
                        if format_of_date.lower() == 'year':
                            ax.set_xlabel('Time (year)', fontsize=12)
                        elif format_of_date.lower() == 'day':
                            ax.set_xlabel('Time (day)', fontsize=12)
                        elif format_of_date.lower() == 'hour':
                            ax.set_xlabel('Time (hour)', fontsize=12)
                        elif format_of_date.lower() == 'min':
                            ax.set_xlabel('Time (min)', fontsize=12)
                        j = j + 1
                    plt.tight_layout()
                    plt.show()
                    fig.savefig('Multi plot' + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)
            else:
                print("Parameters must be a list of parameter values with parameters less than 3")

    def retrieve_multi_data(self, param, gridblocknumber):
        dataStorage = {}
        fileNames = []
        for parameter in param:
            fileNumber = 0
            for file in self.filelocations:
                fileReader = self.read_file_multi(file, self.filetitles[fileNumber])
                filename = parameter + str(fileNumber)
                dataStorage[filename] = fileReader.get_timeseries_data(parameter, gridblocknumber)
                fileNames.append(filename)
                fileNumber = fileNumber + 1
        return fileNames, dataStorage

    def multi_param_multi_file_plot(self, param, gridblocknumber, labels, format_of_date='year', style='horizontal',
                                    width=12, height=8):
        fig = plt.figure(figsize=(width, height))
        fileReader = self.read_file_multi(self.filelocations[0], self.filetitles[0])
        time_year = fileReader.convert_times(format_of_date)
        lst, dictionary = self.retrieve_multi_data(param, gridblocknumber)
        colors = ['r', 'royalblue', 'g', 'k', 'c', 'm', 'y']
        markers = ["o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D",
                   "d", "|", "_"]
        kpansa = 0
        param_counter = 0
        subplot_i = 2
        k = 0
        subplot_j = 2
        data_step = len(self.filelocations) - 1
        fig, axs = plt.subplots(subplot_i, subplot_j)
        for number in range(subplot_i):
            for i in range(subplot_j):
                for j in range(len(self.filelocations)):
                    axs[number, i].plot(time_year, dictionary[lst[kpansa + j]], label=labels[k], linewidth=2,
                                        color=colors[j], marker=markers[j])
                    axs[number, i].set_ylabel(self.modifier.strip_param(param[param_counter]))
                    axs[number, i].set_title(self.modifier.param_label_full(param[param_counter].upper()))
                    axs[number, i].set_xlabel('Time (year)')
                    axs[number, i].spines['bottom'].set_linewidth(1.5)
                    axs[number, i].spines['left'].set_linewidth(1.5)
                    axs[number, i].spines['top'].set_linewidth(0.0)
                    axs[number, i].spines['right'].set_linewidth(0.0)
                kpansa = kpansa + len(self.filelocations)
                param_counter = param_counter + 1
            k = k + 1
        # handles, labels = axs[number, i].get_legend_handles_labels()
        # axs[number, i].legend(handles, labels, loc='lower center', bbox_to_anchor=(-0.1, -0.5), fancybox=False, shadow=False, ncol=4)
        plt.subplots_adjust(left=0.125, wspace=0.4, top=0.95)
        plt.tight_layout()
        plt.show()
