import itertools

import utils.utilities as processor
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from fileparser import tough3, toughreact
from fileparser.toughreact import MultiToughReact
from fileparser.experiment import Experiment

class PlotStatistics(object):
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