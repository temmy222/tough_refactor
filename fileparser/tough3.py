import csv
import os
import utils.utilities as processor
import plotting.plottough as plot


class Tough3(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.file_as_list = []

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle +  ' for ' + self.simulatortype

    def read_file(self):
        os.chdir(self.filelocation)
        with open(self.filetitle) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            self.file_as_list = []
            for row in csv_reader:
                self.file_as_list.append(row)
        return self.file_as_list

    def get_times(self):
        self.read_file()
        time = []
        timeraw = []
        for i in range(len(self.file_as_list)):
            if len(self.file_as_list[i]) < 25:
                time.append(self.file_as_list[i])
        for i in range(len(time)):
            interim = time[i][0].split()
            timeraw.append(float(interim[2]))
        return timeraw

    def convert_times_year(self):
        intermediate = self.get_times()
        firstusage = processor.Utilities()
        timeyear = firstusage.convert_times_year(intermediate)
        return timeyear

    def get_time_index(self):
        self.read_file()
        indextime = []
        for index, value in enumerate(self.file_as_list):
            if len(self.file_as_list[index]) < 25:
                indextime.append(index)
        indextime.append(len(self.file_as_list))
        return indextime

    def get_elements(self):
        self.read_file()
        indextime = self.get_time_index()
        temp_file = self.file_as_list[indextime[0] + 1:indextime[1]]
        elements = []
        for i in range(len(temp_file)):
            elements.append(temp_file[i][0])
        return elements

    def resultdict(self):
        self.read_file()
        resultdict = {}
        tempdict = {}
        indextime = self.get_time_index()
        timeraw = self.get_times()
        for i in range(len(indextime) - 1):
            tempdict[i] = self.file_as_list[indextime[i] + 1:indextime[i + 1]]
        for i in range(len(timeraw)):
            resultdict[timeraw[i]] = tempdict[i]
        return resultdict

    def get_timeseries_data(self, param, gridblocknumber):
        self.read_file()
        results = self.resultdict()
        resultarray = []
        heading = []
        heading_first = self.file_as_list[0]
        heading_first_modify = []
        for i in heading_first:
            heading_first_modify.append(i.upper())
        for i in range(len(heading_first_modify)):
            heading.append(heading_first_modify[i].lstrip())
        index_param = heading.index(param.upper())
        for k in results.keys():
            resultarray.append(results[k][gridblocknumber][index_param].lstrip())
        final_data = [float(x) for x in resultarray]
        return final_data

    def get_element_data(self, time, param):
        self.read_file()
        timeraw = self.get_times()
        results = self.resultdict()
        heading = []
        heading_first = self.file_as_list[0]
        heading_first_modify = []
        for i in heading_first:
            heading_first_modify.append(i.upper())
        for i in range(len(heading_first_modify)):
            heading.append(heading_first_modify[i].lstrip())
        index_param = heading.index(param.upper())
        if time < timeraw[0]:
            time = timeraw[0]
        elif time > timeraw[-1]:
            time = timeraw[-1]
        else:
            absolute_difference_function = lambda list_value: abs(list_value - time)
            time = min(timeraw, key=absolute_difference_function)
        results_specific = results[time]
        data = []
        for i in range(len(results_specific)):
            data.append(results_specific[i][index_param].lstrip())
        final_data = [float(x) for x in data]
        return final_data

    def plot_time(self, param, gridblocknumber):
        result_array = self.get_timeseries_data(param, gridblocknumber)
        time_year = self.convert_times_year()
        plotting = plot.PlotTough()
        plotting.plot_time(param, gridblocknumber, time_year, result_array)


