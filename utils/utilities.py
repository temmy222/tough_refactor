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