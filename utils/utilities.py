import numpy as np
from more_itertools import unique_everseen
import random
import matplotlib.pyplot as plt


class Utilities(object):
    def __init__(self):
        welcome = "welcome to utilities"

    def convert_times(self, arraylist, format_of_date):
        intermediate = arraylist
        timeyear = []
        if format_of_date.lower() == 'year':
            for i in range(len(intermediate)):
                timeyear.append(intermediate[i] / 3.154e+7)
        elif format_of_date.lower() == 'day':
            for i in range(len(intermediate)):
                timeyear.append(intermediate[i] / 86400)
        elif format_of_date.lower() == 'hour':
            for i in range(len(intermediate)):
                timeyear.append(intermediate[i] / 3600)
        elif format_of_date.lower() == 'minute':
            for i in range(len(intermediate)):
                timeyear.append(intermediate[i] / 60)
        else:
            raise ValueError("format can either be year, day, hour or minute")
        return timeyear

    def choplist(self, liste, number=3):
        global finallist
        if isinstance(liste, list):
            # finallist = []d[0])
            # newlist = liste[1:-1]
            # len_newlist = len(newlist)
            # ascend = list(np.linspace(1, len_newlist, len_newlist))
            # randomi = random.sample(ascend, number)
            # randomi.sort()
            # myList = [int(x) for x in randomi]
            # for index, value in enumerate(myList):
            #     finallist.append(liste[value])
            # finallist.append(liste[-1])
            if len(liste) > 100:
                liste = liste[0:len(liste):number]
                self.choplist(liste)
            else:
                finallist = liste[0:len(liste):number]
        return finallist

    def cutdata(self, time_data, resultdata, slicevalue):
        for i in range(len(time_data) - 1, 0, -1):
            if time_data[i] > slicevalue:
                del time_data[i]
                del resultdata[i]
        return time_data, resultdata

    def removeRepetiting(self, time_list, value_list):
        final_time_list = []
        final_value_list = []
        for i in range(0, len(time_list)):
            if time_list[i] not in final_time_list:
                final_time_list.append(time_list[i])
                final_value_list.append(value_list[i])
        for i in range(len(final_time_list) - 1, 0, -1):
            if final_time_list[i] - final_time_list[i - 1] < 1:
                del final_time_list[i]
                del final_value_list[i]
        return final_time_list, final_value_list

    def param_label_full(self, param):
        dict_param = {'PRES': 'Pressure (Pa)', 'TEMP': 'Temperature ($^o C$)', 'SAT_G': 'Gas Saturation (-)',
                      'SAT_L': 'Liquid Saturation (-)',
                      'SAT_N': 'NAPL Saturation (-)', 'X_WATER_G': 'Water Mass Fraction in Gas (-)',
                      'X_AIR_G': 'Air Mass Fraction in Gas (-)',
                      'X_WATER_L': 'Water Mass Fraction in Liquid (-)', 'X_AIR_L': 'Air Mass Fraction in Liquid (-)',
                      'X_WATER_N': 'Water Mass Fraction in NAPL (-)',
                      'X_AIR_N': 'Air Mass Fraction in NAPL (-)', 'REL_G"': 'Relative Permeability of Gas (-)',
                      'REL_L': 'Relative Permeability of Liquid (-)',
                      'REL_N': 'Relative Permeability of NAPL (-)',
                      'PCAP_GL': 'Capillary Pressure of Gas in Liquid (Pa)',
                      'PCAP_GN': 'Capillary Pressure of Gas in NAPL (Pa)', 'DEN_G': 'Gas Density ($kg/m^3$)',
                      'DEN_L': 'Liquid Density ($kg/m^3$)',
                      'DEN_N': 'NAPL Density ($kg/m^3$)', 'POR': 'Porosity', 'BIO1': 'Biomass Mass Fraction(-)',
                      'BIO2': 'Biomass Mass Fraction(-)',
                      'X_BENZEN_L': 'Mass Fraction of Benzene in Liquid',
                      'X_TOLUEN_L': 'Mass Fraction of Toluene in Liquid',
                      'X_N-DECA_L': 'Mass Fraction of Decane in Liquid',
                      'X_TOLUEN_N': 'Mass Fraction of Toluene in NAPL',
                      'X_TOLUEN_G': 'Mass Fraction of Toluene in Gas', 'PH': 'pH', 'T_NA+': 'Concentration of Sodium',
                      'T_CL-': 'Concentration of Chlorine',
                      'T_CA+2': 'Concentration of Calcium', 'T_H2O': 'Concentration of Water',
                      'T_H+': 'Concentration of Hydrogen',
                      'CALCITE': 'Calcite', 'PORTLANDITE': 'Portlandite', 'GYPSUM': 'Gypsum',
                      'POROSITY': 'Porosity', 'ETTRINGITE': 'Ettringite'
                      }
        return dict_param[param]

    def fmt(self, x, pos):
        a, b = '{:.2e}'.format(x).split('e')
        b = int(b)
        return r'${} \times 10^{{{}}}$'.format(a, b)

    def get_number_of_grids(self, input_list):
        output = set()
        for x in input_list:
            output.add(x)
        output = list(output)
        return len(output)

    def getgridnumber(self, df, direction):
        X = df[direction]
        d = {}
        for i in X:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        m = list(d.keys())
        return m, len(d)

    def cust_range(self, *args, rtol=1e-05, atol=1e-08, include=[True, False]):
        """
        Combines numpy.arange and numpy.isclose to mimic
        open, half-open and closed intervals.
        Avoids also floating point rounding errors as with
        >>> numpy.arange(1, 1.3, 0.1)
        array([1. , 1.1, 1.2, 1.3])

        args: [start, ]stop, [step, ]
            as in numpy.arange
        rtol, atol: floats
            floating point tolerance as in numpy.isclose
        include: boolean list-like, length 2
            if start and end point are included
        """
        # process arguments
        if len(args) == 1:
            start = 0
            stop = args[0]
            step = 1
        elif len(args) == 2:
            start, stop = args
            step = 1
        else:
            assert len(args) == 3
            start, stop, step = tuple(args)

        # determine number of segments
        n = (stop - start) / step + 1

        # do rounding for n
        if np.isclose(n, np.round(n), rtol=rtol, atol=atol):
            n = np.round(n)

        # correct for start/end is excluded
        if not include[0]:
            n -= 1
            start += step
        if not include[1]:
            n -= 1
            stop -= step

        return np.linspace(start, stop, int(n))

    def crange(self, *args, **kwargs):
        return self.cust_range(*args, **kwargs, include=[True, True])

    def orange(self, *args, **kwargs):
        return self.cust_range(*args, **kwargs, include=[True, False])

    def strip_param(self, param):
        if param.lower() == 'porosity':
            output = 'Porosity'
        elif param.startswith("t_"):
            output = "Total Concentration (mol/L)"
        elif param.startswith("pH"):
            output = 'pH'
        return output
