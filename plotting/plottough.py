import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.ticker as ticker
from matplotlib import style
from random import randrange
import random
from scipy import interpolate
from scipy.interpolate import griddata
import fileparser.fileread as input
import utils.utilities as processor
import fileparser.fileread as fileDetails
import fileparser.tough3 as tough3
import fileparser.toughreact as toughreact
import pandas as pd




class PlotTough(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.modifier = processor.Utilities()

    def read_file(self):
        if self.simulatortype.lower() == "tmvoc" or self.simulatortype.lower() == "tough3":
            fileReader = tough3.Tough3(self.simulatortype, self.filelocation, self.filetitle)
        else:
            fileReader = toughreact.ToughReact(self.simulatortype, self.filelocation, self.filetitle)
        return fileReader

    def plotParamWithTime(self, param, gridblocknumber):
        with plt.style.context('mystyle'):

            fileReader = self.read_file()
            time_year = fileReader.convert_times_year()
            result_array = fileReader.get_timeseries_data(param, gridblocknumber)
            fig, axs = plt.subplots(1, 1)
            axs.plot(time_year, result_array, marker='^')
            axs.set_xlabel('Time (year)')
            parameters = processor.Utilities()
            axs.set_ylabel(parameters.param_label_full(param.upper()))
            plt.tight_layout()
            plt.show()
            fig.savefig(param + ' vs ' + 'time' + '.png', bbox_inches='tight', dpi=600)

    def plotParamWithParam(self, param1, param2, gridblocknumber):

        with plt.style.context('mystyle'):
            fileReader = self.read_file()
            result_array_x = fileReader.get_timeseries_data(param1, gridblocknumber)
            result_array_y = fileReader.get_timeseries_data(param2, gridblocknumber)
            fig, axs = plt.subplots(1, 1)
            axs.plot(result_array_x, result_array_y, marker='^')
            axs.set_xlabel(self.modifier.param_label_full(param1.upper()))
            axs.set_ylabel(self.modifier.param_label_full(param2.upper()))
            plt.tight_layout()
            plt.show()
            fig.savefig(param2 + ' vs ' + param1 + '.png', bbox_inches='tight', dpi=600)

    def plot2D_one(self, direction1, direction2, param, timer):
        fileReader = self.read_file()
        fig, ax = plt.subplots(1, 1)
        X = fileReader.get_coord_data(direction1, timer)
        Z = fileReader.get_coord_data(direction2, timer)
        data = fileReader.get_element_data(timer, param)
        xi, yi = np.meshgrid(X, Z)
        data1 = griddata((X, Z), data, (xi, yi), method='nearest')
        # cs2 = plt.contourf (xi,yi,data1,800,extend='neither',cmap='coolwarm')
        cs2 = plt.contourf(xi, yi, data1, 800, cmap='coolwarm', vmin=min(data), vmax=max(data))
        #  ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
        # c = ax.pcolor(xi, yi, data, cmap='RdBu')
        vmin = min(data)
        if vmin < 1 or vmin > 1000:
            cbar = fig.colorbar(cs2, pad=0.01, format=ticker.FuncFormatter(self.modifier.fmt))
        else:
            cbar = fig.colorbar(cs2, pad=0.01)
        cbar.ax.set_ylabel(self.modifier.param_label_full(param.upper()), fontsize=12)
        ticklabs = cbar.ax.get_yticklabels()
        #  ticklabs.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
        cbar.ax.set_yticklabels(ticklabs, fontsize=12)
        plt.xlabel('Horizontal Distance(m)', fontsize=12)
        plt.ylabel('Vertical Depth (m)', fontsize=12)
        plt.tick_params(axis='x', labelsize=12)
        plt.tick_params(axis='y', labelsize=12)
        plt.tight_layout()
        plt.show()
        fig.savefig('2D plain' + str(timer) + param + '.png', bbox_inches='tight', dpi=600)

    def plot2D_withgrid(self, direction1, direction2, param, timer):
        fileReader = self.read_file()
        fig, ax = plt.subplots(1, 1)
        X = fileReader.get_coord_data(direction1, timer)
        Z = fileReader.get_coord_data(direction2, timer)
        # param = tre.element[self.parameters[paramNum]]
        df = pd.DataFrame(index=range(len(X)))
        df['X'] = X
        df['Z'] = Z
        Zvalues, Ztotal = self.modifier.getgridnumber(df, 'Z')
        Xvalues, Xtotal = self.modifier.getgridnumber(df, 'X')
        xi, yi = np.meshgrid(X, Z)
        orig_data = fileReader.get_element_data(timer, param)
        data = np.asarray(orig_data)
        data = data.reshape(Ztotal, Xtotal)
        data1 = griddata((X, Z), orig_data, (xi, yi), method='nearest')
        extent = [min(X), max(X), min(Z), max(Z)]
        cs2 = plt.imshow(np.reshape(data, newshape=(Ztotal, Xtotal)), cmap='coolwarm', interpolation='none')
        ax = plt.gca()
        # Major ticks
        x_tick = np.arange(0, Xtotal, 1)
        z_tick = np.arange(0, Ztotal, 1)
        Z_array = np.asarray(Z)
        Z_array = np.abs(Z_array)
        ax.set_xticks(x_tick)
        num_tick_x = len(x_tick)
        num_tick_z = len(z_tick)
        ax.set_yticks(z_tick)
        # Labels for major ticks
        tick_x = max(X) - min(X)
        tick_z = max(Z) - min(Z)
        if max(X) < 1 or max(Z) < 1:
            ax.set_xticklabels(np.round(self.modifier.crange(min(X), max(X), tick_x / (num_tick_x - 1)), 4), fontsize=8)
            ax.set_yticklabels(np.round(self.modifier.crange(min(Z_array), max(Z_array), tick_z / (num_tick_z - 1)), 4),
                               fontsize=8)
        else:
            ax.set_xticklabels(np.round(self.modifier.crange(min(X), max(X), tick_x / (num_tick_x - 1)), 2), fontsize=8)
            ax.set_yticklabels(np.round(self.modifier.crange(min(Z_array), max(Z_array), tick_z / (num_tick_z - 1)), 2),
                               fontsize=8)
        # Minor ticks
        ax.set_xticks(np.arange(-.5, Xtotal, 1), minor=True)
        ax.set_yticks(np.arange(-.5, Ztotal, 1), minor=True)
        # Gridlines based on minor ticks
        ax.grid(which='minor', color='k', linestyle='-', linewidth=1)
        cbar = fig.colorbar(cs2, ax=ax, pad=0.2, orientation="horizontal")
        # cbar.ax.set_ylabel(param,fontsize=8)
        cbar.ax.set_title(param, fontsize=12)
        cbar.ax.tick_params(labelsize=12)
        cbar.ax.locator_params(nbins=5)
        cbar.ax.ticklabel_format(useOffset=False, style='plain')
        plt.xticks(rotation=90)
        plt.xlabel('Horizontal Distance(m)', fontsize=12)
        plt.ylabel('Vertical Depth (m)', fontsize=12)
        plt.tight_layout()
        plt.show()
        fig.savefig('Grid' + str(timer) + param + '.png', bbox_inches='tight', dpi=600)

