import numpy as np
import random
class Utilities(object):
    def __init__(self):
        welcome = "welcome to utilities"

    def convert_times_year(self, arraylist):
        intermediate = arraylist
        timeyear = []
        for i in range(len(intermediate)):
            timeyear.append(intermediate[i] / 3.154e+7)
        return timeyear

    def choplist(self,liste,number=40):
        if isinstance(liste, list):
            finallist =[]
            finallist.append(liste[0])
            newlist = liste[1:-1]
            len_newlist = len(newlist)
            ascend = list(np.linspace(1,len_newlist,len_newlist))
            randomi = random.sample(ascend,number)
            randomi.sort()
            myList = [int(x) for x in randomi]
            for index,value in enumerate(myList):
                finallist.append(liste[value])
            finallist.append(liste[-1])
        else:
            print('Input must be a list')
        return finallist

    def param_label_full(self, param):
        dict_param = {'PRES':'Pressure (Pa)','TEMP':'Temperature ($^o C$)','SAT_G':'Gas Saturation (-)','SAT_L':'Liquid Saturation (-)',
                      'SAT_N':'NAPL Saturation (-)','X_WATER_G':'Water Mass Fraction in Gas (-)','X_AIR_G':'Air Mass Fraction in Gas (-)',
                      'X_WATER_L':'Water Mass Fraction in Liquid (-)','X_AIR_L':'Air Mass Fraction in Liquid (-)','X_WATER_N':'Water Mass Fraction in NAPL (-)',
                      'X_AIR_N':'Air Mass Fraction in NAPL (-)','REL_G"':'Relative Permeability of Gas (-)','REL_L':'Relative Permeability of Liquid (-)',
                      'REL_N':'Relative Permeability of NAPL (-)','PCAP_GL':'Capillary Pressure of Gas in Liquid (Pa)',
                      'PCAP_GN':'Capillary Pressure of Gas in NAPL (Pa)','DEN_G':'Gas Density ($kg/m^3$)','DEN_L':'Liquid Density ($kg/m^3$)',
                      'DEN_N':'NAPL Density ($kg/m^3$)','POR':'Porosity','BIO1':'Biomass Mass Fraction(-)','BIO2':'Biomass Mass Fraction(-)',
                      'X_BENZEN_L':'Mass Fraction of Benzene in Liquid','X_TOLUEN_L':'Mass Fraction of Toluene in Liquid',
                      'X_N-DECA_L': 'Mass Fraction of Decane in Liquid','X_TOLUEN_N':'Mass Fraction of Toluene in NAPL',
                      'X_TOLUEN_G':'Mass Fraction of Toluene in Gas', 'PH':'pH'}
        return dict_param[param]