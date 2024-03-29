import itertools

import utils.utilities as processor
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from fileparser import tough3, toughreact
from fileparser.toughreact import MultiToughReact
from fileparser.experiment import Experiment


class PlotMultiTough(object):
    def __init__(self, simulatortype, filelocations, filetitles, **kwargs):
        self.filelocations = filelocations
        self.filetitles = filetitles
        self.simulatortype = simulatortype
        self.modifier = processor.Utilities()
        self.generation = kwargs.get('generation')
        self.args = kwargs.get('restart_files')
        self.expt = kwargs.get('experiment')
        self.x_slice_value = kwargs.get('x_slice_value')

    def read_file(self):
        os.chdir(self.filelocations)
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            fileReader = tough3.Tough3(self.simulatortype, self.filelocations, self.filetitles,
                                       generation=self.generation)
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

    def getRestartLocations(self):
        restart_files = list()
        restart_files.append(self.filelocations)
        restart_files = restart_files + self.args
        return restart_files

    def getRestartDataTime(self, format_of_date):
        locations = self.getRestartLocations()
        final_time = []
        for i in range(0, len(locations)):
            if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
                fileReader = tough3.Tough3(self.simulatortype, locations[i], self.filetitle)
            else:
                fileReader = toughreact.ToughReact(self.simulatortype, locations[i], self.filetitles)
            if i == 0:
                time_year = fileReader.convert_times(format_of_date)
                final_time.append(time_year)
            else:
                time_year = fileReader.convert_times(format_of_date)
                time_year = time_year[1:]
                final_time.append(time_year)
        final_time = list(itertools.chain.from_iterable(final_time))
        return final_time

    def getRestartDataElement(self, param, gridblocknumber):
        locations = self.getRestartLocations()
        final_result = []
        for i in range(0, len(locations)):
            if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
                fileReader = tough3.Tough3(self.simulatortype, locations[i], self.filetitles)
            else:
                fileReader = toughreact.ToughReact(self.simulatortype, locations[i], self.filetitles)
            if i == 0:
                result_array = fileReader.get_timeseries_data(param, gridblocknumber)
                final_result.append(result_array)
            else:
                result_array = fileReader.get_timeseries_data(param, gridblocknumber)
                result_array = result_array[1:]
                final_result.append(result_array)
        final_result = list(itertools.chain.from_iterable(final_result))
        return final_result

    def raw_multi_plot_restart_horizontal(self, param, format_of_date, gridblocknumber):
        time_year = self.getRestartDataTime(format_of_date)
        j = 0
        fig, axs = plt.subplots(len(param), sharex=False)
        for parameter in param:
            result_array = self.getRestartDataElement(parameter, gridblocknumber)
            parameters = processor.Utilities()
            time_year, result_array = parameters.removeRepetiting(time_year, result_array)
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

    def raw_multi_plot_restart_vertical(self, param, gridblocknumber, format_of_date):
        fig = plt.figure()
        for number in range(1, len(param) + 1):
            ax = fig.add_subplot(1, len(param), number)
            result_array = self.getRestartDataElement(param[number - 1], gridblocknumber)
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

    def multi_time_plot_restart(self, param, gridblocknumber, format_of_date, style='horizontal'):
        if style.lower() == 'horizontal':
            if self.expt:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_restart_horizontal_with_expt(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_restart_horizontal_with_expt(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")
            else:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_horizontal(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_horizontal(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")
        elif style.lower() == 'vertical':
            if self.expt:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_vertical_with_expt(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_vertical_with_expt(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")
            else:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_vertical(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_vertical(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")

    def raw_multi_plot_horizontal(self, param, format_of_date, gridblocknumber):
        fileReader = self.read_file()
        time_year = fileReader.convert_times(format_of_date)
        j = 0
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

    def raw_multi_plot_horizontal_with_expt(self, param, format_of_date, gridblocknumber):
        fileReader = self.read_file()
        time_year = fileReader.convert_times(format_of_date)
        expt_test = Experiment(self.expt[0], 'data_file.csv')
        time_year_expt = expt_test.get_times()
        j = 0
        fig, axs = plt.subplots(len(param), sharex=False)
        for parameter in param:
            result_array = fileReader.get_timeseries_data(parameter, gridblocknumber)
            result_array_expt = expt_test.get_timeseries_data(parameter)
            axs[j].plot(time_year, result_array, marker='^',
                        label='simulation')
            if max(result_array_expt) <= 0:
                dy = 0.1 * abs(min(result_array_expt))
            else:
                dy = 0.1 * abs(max(result_array_expt))
            # axs[j].plot(time_year_expt, result_array_expt, '--', marker='o', color='r',
            #         label='experiment')
            axs[j].errorbar(time_year_expt, result_array_expt, yerr=dy, fmt='--or', color='--r', label='experiment')
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
            axs[j].legend(loc='best')
            plt.setp(axs[j].get_xticklabels(), fontsize=12)
            plt.setp(axs[j].get_yticklabels(), fontsize=12)
            j = j + 1
        plt.tight_layout()
        plt.show()
        os.chdir(self.filelocations)
        fig.savefig('Multi plot' + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)

    def raw_multi_plot_restart_horizontal_with_expt(self, param, format_of_date, gridblocknumber):
        time_year = self.getRestartDataTime(format_of_date)
        j = 0
        fig, axs = plt.subplots(len(param), sharex=False)
        expt_test = Experiment(self.expt[0], 'data_file.csv')
        time_year_expt = expt_test.get_times()
        for parameter in param:
            result_array = self.getRestartDataElement(parameter, gridblocknumber)
            parameters = processor.Utilities()
            time_year, result_array = parameters.removeRepetiting(time_year, result_array)
            result_array_expt = expt_test.get_timeseries_data(parameter)
            axs[j].plot(time_year, result_array, marker='^',
                        label='simulation')
            # axs[j].plot(time_year_expt, result_array_expt, '--', color ='r', marker='o',
            #             label='experiment')
            if max(result_array_expt) <= 0:
                dy = 0.15 * abs(min(result_array_expt))
            else:
                dy = 0.15 * abs(max(result_array_expt))
            axs[j].errorbar(time_year_expt, result_array_expt, yerr=dy, fmt='--or', color='--r', label='experiment')
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
            axs[j].legend()
            j = j + 1
        plt.tight_layout()
        plt.show()
        os.chdir(self.filelocations)
        fig.savefig('Multi plot' + ' vs ' + 'experiment restart time' + '.png', bbox_inches='tight', dpi=600)

    def raw_multi_plot_vertical(self, param, format_of_date, gridblocknumber):
        fileReader = self.read_file()
        time_year = fileReader.convert_times(format_of_date)
        j = 0
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

    def raw_multi_plot_vertical_with_expt(self, param, format_of_date, gridblocknumber):
        fileReader = self.read_file()
        time_year = fileReader.convert_times(format_of_date)
        expt_test = Experiment(self.expt[0], 'data_file.csv')
        time_year_expt = expt_test.get_times()
        j = 0
        fig = plt.figure()
        for number in range(1, len(param) + 1):
            ax = fig.add_subplot(1, len(param), number)
            result_array_expt = expt_test.get_timeseries_data(param[number - 1])
            result_array = fileReader.get_timeseries_data(param[number - 1], gridblocknumber)
            ax.plot(time_year, result_array, marker='^',
                    label='simulation')
            ax.plot(time_year_expt, result_array_expt, '--', marker='o', color='r',
                    label='experiment')
            ax.set_ylabel(self.modifier.param_label_full(param[number - 1].upper()), fontsize=12)
            ax.spines['bottom'].set_linewidth(1.5)
            ax.spines['left'].set_linewidth(1.5)
            ax.spines['top'].set_linewidth(0)
            ax.spines['right'].set_linewidth(0)
            # ax.ticklabel_format(useOffset=False,style='plain')
            ax.ticklabel_format(useOffset=False)
            plt.setp(ax.get_xticklabels(), fontsize=12)
            plt.setp(ax.get_yticklabels(), fontsize=12)
            ax.legend(loc='best', borderpad=0.1)
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

    def multi_time_plot(self, param, gridblocknumber, format_of_date, style='horizontal'):
        if style.lower() == 'horizontal':
            if self.expt:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_horizontal_with_expt(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_horizontal_with_expt(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")
            else:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_horizontal(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_horizontal(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")
        elif style.lower() == 'vertical':
            if self.expt:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_vertical_with_expt(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_vertical_with_expt(param, format_of_date, gridblocknumber)
                else:
                    print("Parameters must be a list of parameter values with parameters less than 3")
            else:
                if isinstance(param, list) and len(param) < 3:
                    try:
                        with plt.style.context('mystyle'):
                            self.raw_multi_plot_vertical(param, format_of_date, gridblocknumber)
                    except:
                        with plt.style.context('classic'):
                            self.raw_multi_plot_vertical(param, format_of_date, gridblocknumber)
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

    def retrieve_multi_data_generation(self, param, format_of_date):
        data_table = pd.DataFrame()
        fileReader = self.read_file()
        for i in range(len(param)):
            time_data_label = 'time' + str(i)
            result_data_label = 'result' + str(i)
            time_data = fileReader.convert_times(format_of_date=format_of_date)
            result_data = fileReader.getGenerationData(param[i])
            data_table[time_data_label] = pd.Series(time_data)
            data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def slice_value(self, time, result):
        first_time = time[0]
        first_result = result[0]
        last_time = time[-1]
        last_result = result[-1]
        time_array = np.array(time)
        result_array = np.array(result)
        time_array = time_array[0:len(time_array) + 8:10]
        result_array = result_array[0:len(result_array) + 8:10]
        if len(time_array) > 10:
            return self.slice_value(time_array, result_array)
        time_array = np.append(time_array, last_time)
        result_array = np.append(result_array, last_result)
        return time_array, result_array

    def plotMultiParamSinglePlot(self, param, gridblocknumber, format_of_date, labels=None):
        if self.generation is True:
            with plt.style.context('classic'):
                fig, axs = plt.subplots(1, 1)
                dataFile = self.retrieve_multi_data_generation(param, format_of_date)
                legend_index = 0
                for i in range(0, len(dataFile.columns), 2):
                    if labels is None:
                        axs.plot(dataFile.iloc[:, i], dataFile.iloc[:, i + 1], label=param[legend_index])
                    else:
                        axs.plot(dataFile.iloc[:, i], dataFile.iloc[:, i + 1], label=labels[legend_index])
                    axs.set_xlabel('Time (' + format_of_date + ")", fontsize=14)
                    axs.set_ylabel('Mass Fraction', fontsize=14)
                    legend_index += 1
                plt.setp(axs.get_xticklabels(), fontsize=14)
                plt.setp(axs.get_yticklabels(), fontsize=14)
                plt.legend()
                plt.tight_layout()
                plt.show()
                fig.savefig('multiple param  vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)
        else:
            with plt.style.context('classic'):
                fig, axs = plt.subplots(1, 1)
                markers = [".", "v", "^", "<", ">", "8", "s", "p", "P", "*", "h"]
                fileReader = self.read_file()

                for i in range(0, len(param)):
                    time_year = fileReader.convert_times(format_of_date)
                    result_array = fileReader.get_timeseries_data(param[i], gridblocknumber)
                    if len(time_year) > 50:
                        time_year, result_array = self.slice_value(time_year, result_array)
                    if labels is None:
                        axs.plot(time_year, result_array, label=param[i], marker=markers[i])
                    else:
                        axs.plot(time_year, result_array, label=labels[i], marker=markers[i])
                    axs.set_xlabel('Time (' + format_of_date + ")", fontsize=14)
                    axs.set_ylabel('Mass Fraction', fontsize=14)
                    axs.ticklabel_format(useOffset=False, style='plain', axis='both')
                plt.setp(axs.get_xticklabels(), fontsize=14)
                plt.setp(axs.get_yticklabels(), fontsize=14)
                plt.legend(loc='best')
                plt.tight_layout()
                plt.show()
                plt.tick_params(axis='x', which='major', labelsize=3)
                fig.savefig(param[0] + 'multiple param OUTPUT vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)

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
