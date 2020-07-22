import utils.utilities as processor
import os
import numpy as np
import matplotlib.pyplot as plt

from fileparser import tough3, toughreact


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
            fileReader = toughreact.Toughreact(self.simulatortype, self.filelocations, self.filetitles)
        return fileReader

    def read_file_multi(self, file, filetitle):
        os.chdir(file)
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            fileReader = tough3.Tough3(self.simulatortype, file, filetitle)
        else:
            fileReader = toughreact.Toughreact(self.simulatortype, file, filetitle)
        return fileReader

    def multi_time_plot(self, param, gridblocknumber, style='horizontal'):
        fig = plt.figure()
        fileReader = self.read_file()
        time_year = fileReader.convert_times_year()
        j = 0
        if style.lower() == 'horizontal':
            if isinstance(param, list):
                fig, axs = plt.subplots(len(param), sharex=False)
            else:
                print("Must be a list of parameter values")
            for parameter in param:
                result_array = fileReader.get_timeseries_data(parameter, gridblocknumber)
                axs[j].plot(time_year, result_array, marker='^', label=self.modifier.param_label_full(parameter.upper()))
                axs[j].set_ylabel(self.modifier.param_label_full(parameter.upper()), fontsize=12)
                axs[j].spines['bottom'].set_linewidth(1.5)
                axs[j].spines['left'].set_linewidth(1.5)
                axs[j].spines['top'].set_linewidth(0)
                axs[j].spines['right'].set_linewidth(0)
                # axs[j].legend(loc='best',borderpad=0.1)
                axs[j].set_xlabel('Time (year)', fontsize=12)
                axs[j].ticklabel_format(useOffset=False)
                plt.setp(axs[j].get_xticklabels(), fontsize=12)
                plt.setp(axs[j].get_yticklabels(), fontsize=12)
                j = j+1
            plt.tight_layout()
            plt.show()
            fig.savefig('Multi plot' + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)
        elif style.lower() == 'vertical':
            for number in range(1, len(param)+1):
                ax = fig.add_subplot(1, len(param), number)
                result_array = fileReader.get_timeseries_data(param[number-1], gridblocknumber)
                ax.plot(time_year, result_array, marker='^', label=self.modifier.param_label_full(param[number-1].upper()))
                ax.set_ylabel(self.modifier.param_label_full(param[number-1].upper()), fontsize=12)
                ax.spines['bottom'].set_linewidth(1.5)
                ax.spines['left'].set_linewidth(1.5)
                ax.spines['top'].set_linewidth(0)
                ax.spines['right'].set_linewidth(0)
                # ax.ticklabel_format(useOffset=False,style='plain')
                ax.ticklabel_format(useOffset=False)
                plt.setp(ax.get_xticklabels(), fontsize=12)
                plt.setp(ax.get_yticklabels(), fontsize=12)
                # ax.legend(loc='best',borderpad=0.1)
                ax.set_xlabel('Time (year)', fontsize=12)
                j = j+1
            plt.tight_layout()
            plt.show()
            fig.savefig('Multi plot' + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)

    # def retrieve_multi_data(self, param, gridblocknumber):
    #     dataStorage = {}
    #     for file in self.filelocations:
    #         fileNumber = 0
    #         for parameter in param:
    #             fileReader = self.read_file_multi(file, self.filetitles[fileNumber])
    #             filename = parameter + str(fileNumber)
    #             dataStorage[filename] = fileReader.get_timeseries_data(parameter, gridblocknumber)
    #             fileNumber = fileNumber + 1
    #     return dataStorage

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


    def multi_param_multi_file_plot(self, param, gridblocknumber, labels, style='horizontal', width=12, height=8):
        fig = plt.figure(figsize=(width, height))
        paralengthdouble = len(param) * 2
        fileReader = self.read_file_multi(self.filelocations[0], self.filetitles[0])
        time_year = fileReader.convert_times_year()
        lst, dictionary = self.retrieve_multi_data(param, gridblocknumber)
        colors = ['r', 'royalblue', 'g', 'k', 'c', 'm', 'y']
        markers = ["o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D",
                   "d", "|", "_"]
        j = 0
        kpansa = 0
        counter = 1
        axs = plt.subplots(3, 2)
        for number in range(0, len(param)):
            k = 0
            for i in range(kpansa, len(dictionary)):
                axs[number, i].plot(time_year, dictionary[lst[kpansa]], label=labels[k], linewidth=2,
                         color=colors[k], marker=markers[k])
