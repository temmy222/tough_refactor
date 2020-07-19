class Utilities(object):
    def __init__(self):
        welcome = "welcome to utilities"

    def convert_times_year(self, arraylist):
        intermediate = arraylist
        timeyear = []
        for i in range(len(intermediate)):
            timeyear.append(intermediate[i] / 3.154e+7)
        return timeyear