import itertools
from functools import reduce

import utils.utilities as processor
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from fileparser import tough3, toughreact
import seaborn as sns


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

    def getIndex(self, column_names, required_columns):
        output = []
        for i in range(len(column_names)):
            for value in required_columns:
                if value.lower() == column_names[i].lower():
                    output.append(i)
        return output

    def getDataIntoPandas(self, values, gridblocknumber):
        assert isinstance(values, list)
        data_table = pd.DataFrame()
        fileReader = self.read_file()
        all_elements = fileReader.getParameters()
        index = self.getIndex(all_elements, values)
        print(all_elements)
        for i in range(len(all_elements)):
            if i in index:
                if self.simulatortype.lower() == 'toughreact':
                    result_data = fileReader.get_timeseries_data(all_elements[i], gridblocknumber)
                else:
                    result_data = fileReader.get_timeseries_data(all_elements[i], gridblocknumber)
                data_table[all_elements[i]] = pd.Series(result_data)
        data_table.columns = map(lambda x: str(x).capitalize(), data_table.columns)
        return data_table

    def renamingChemical(self, x):
        if x.startswith('t_'):
            x = x[2:]
        return x

    def getAllDataIntoPandas(self, values, gridblocknumber):
        data_table = pd.DataFrame()
        assert isinstance(values, list)
        df1 = self.getAllMineralData(gridblocknumber)
        df2 = self.getAllChemicalData(gridblocknumber)
        df3 = self.getAllGasData(gridblocknumber)
        df1 = df1.set_index('X(m)')
        df2 = df2.set_index('X(m)')
        df3 = df3.set_index('X(m)')
        df_final = pd.concat([df1, df2, df3], axis=1)
        df_final.reset_index(inplace=True)
        df_final = df_final.loc[:, ~df_final.columns.duplicated()]
        df_final.columns = map(self.renamingChemical, df_final.columns)
        df_final.columns = map(lambda x: str(x).capitalize(), df_final.columns)
        all_elements = df_final.columns.tolist()
        index = self.getIndex(all_elements, values)
        for i in index:
            result_data = df_final.iloc[:, i]
            data_table[all_elements[i]] = pd.Series(result_data)
        return data_table

    def getAllMineralData(self, gridblocknumber):
        data_table = pd.DataFrame()
        fileReader = toughreact.ToughReact(self.simulatortype, self.filelocations, 'kdd_min.tec')
        all_elements = fileReader.getParameters()
        for i in range(len(all_elements)):
            if self.simulatortype.lower() == 'toughreact':
                result_data = fileReader.get_timeseries_data(all_elements[i], gridblocknumber)
            data_table[all_elements[i]] = pd.Series(result_data)
        return data_table

    def getAllChemicalData(self, gridblocknumber):
        data_table = pd.DataFrame()
        fileReader = toughreact.ToughReact(self.simulatortype, self.filelocations, 'kdd_conc.tec')
        all_elements = fileReader.getParameters()
        for i in range(len(all_elements)):
            if self.simulatortype.lower() == 'toughreact':
                result_data = fileReader.get_timeseries_data(all_elements[i], gridblocknumber)
            data_table[all_elements[i]] = pd.Series(result_data)
        return data_table

    def getAllGasData(self, gridblocknumber):
        data_table = pd.DataFrame()
        fileReader = toughreact.ToughReact(self.simulatortype, self.filelocations, 'kdd_gas.tec')
        all_elements = fileReader.getParameters()
        for i in range(len(all_elements)):
            if self.simulatortype.lower() == 'toughreact':
                result_data = fileReader.get_timeseries_data(all_elements[i], gridblocknumber)
            data_table[all_elements[i]] = pd.Series(result_data)
        return data_table

    def plotRegular(self, index, gridblocknumber, format='single', **kwargs):
        if format == 'single':
            data = self.getDataIntoPandas(index, gridblocknumber)
        elif format == 'all':
            data = self.getAllDataIntoPandas(index, gridblocknumber)
        else:
            raise ValueError("format can either be single or all")
        diags = kwargs.get('diagonal')
        g = sns.PairGrid(data)
        if diags:
            if diags.lower() == 'histogram':
                g.map_diag(sns.histplot)
                g.map_offdiag(sns.regplot)
            elif diags.lower() == 'scatter':
                g.map_diag(sns.scatterplot)
                g.map_offdiag(sns.regplot)
        else:
            g.map(sns.regplot)
        plt.tight_layout()
        plt.show()

    def plotScatter(self, index, gridblocknumber, **kwargs):
        data = self.getDataIntoPandas(index, gridblocknumber)
        diags = kwargs.get('diagonal')
        g = sns.PairGrid(data)
        if diags:
            if diags.lower() == 'histogram':
                g.map_diag(sns.histplot)
                g.map_offdiag(sns.scatterplot)
            elif diags.lower() == 'regular':
                g.map_diag(sns.regularplot)
                g.map_offdiag(sns.scatterplot)
        else:
            g.map(sns.scatterplot)
        plt.tight_layout()
        plt.show()
        
class PlotMultiStatistics(object):
    def __init__(self, simulatortype, filelocations, filetitles):
        self.filetitles = filetitles
        self.filelocations = filelocations
        self.simulatortype = simulatortype


