import csv
import os
import tough_refactor.utils.utilities as processor
import pandas as pd
import tough_refactor.plotting.plottough as plot


class Tough3(object):
    def __init__(self, simulatortype, filelocation, filetitle, **kwargs):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.generation = kwargs.get('generation')
        self.file_as_list = []

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle + ' for ' + self.simulatortype

    def read_file(self):
        os.chdir(self.filelocation)
        with open(self.filetitle) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            self.file_as_list = []
            for row in csv_reader:
                self.file_as_list.append(row)
        return self.file_as_list

    def get_times(self):
        """
        get times stored for duration of the simulation
        :return: a list of all times
        """
        self.read_file()
        time = []
        timeraw = []
        if self.generation is True:
            for i in range(1, len(self.file_as_list)):
                timeraw.append(float(self.file_as_list[i][0]))
        else:
            for i in range(len(self.file_as_list)):
                if len(self.file_as_list[i]) == 1:
                    time.append(self.file_as_list[i])
            for i in range(len(time)):
                interim = time[i][0].split()
                timeraw.append(float(interim[2]))
        return timeraw

    def convert_times(self, format_of_date):
        """
        convert time to desirable time e.g day, month, year
        :param format_of_date: string of type 'day', 'month', 'year'
        :return: a list of the time
        """
        intermediate = self.get_times()
        firstusage = processor.Utilities()
        timeyear = firstusage.convert_times(intermediate, format_of_date)
        return timeyear

    def get_time_index(self):
        self.read_file()
        indextime = []
        for index, value in enumerate(self.file_as_list):
            if len(self.file_as_list[index]) == 1:
                indextime.append(index)
        indextime.append(len(self.file_as_list))
        return indextime

    def getGenerationData(self, param):
        self.read_file()
        resultarray=[]
        heading = []
        heading_first = self.file_as_list[0]
        heading_first_modify = []
        for i in heading_first:
            heading_first_modify.append(i.upper())
        for i in range(len(heading_first_modify)):
            heading.append(heading_first_modify[i].lstrip())
        index_param = heading.index(param.upper())
        for i in range(1, len(self.file_as_list)):
            resultarray.append(float(self.file_as_list[i][index_param]))
        return resultarray

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

    def get_X_data(self, time):
        return self.get_element_data(time, 'x')

    def get_Y_data(self, time):
        return self.get_element_data(time, 'y')

    def get_Z_data(self, time):
        return self.get_element_data(time, 'z')

    def get_coord_data(self, direction, timer):
        if direction.lower() == 'x':
            value = self.get_X_data(timer)
        elif direction.lower() == 'y':
            value = self.get_Y_data(timer)
        elif direction.lower() == 'z':
            value = self.get_Z_data(timer)
        else:
            print("coordinates can either be X, Y or Z")
        return value

    def getUniqueXData(self, timer):
        ori_array = self.get_coord_data('x', timer)
        indices_array = []
        for i in range(0, len(ori_array)):
            try:
                if ori_array[i] > ori_array[i + 1]:
                    indices_array.append(i)
                else:
                    continue
            except:
                pass
        output_data = ori_array[0:indices_array[0] + 1]
        return output_data

    def getXStartPoints(self, timer):
        ori_array = self.get_coord_data('x', timer)
        indices_array = []
        for i in range(0, len(ori_array)):
            try:
                if ori_array[i] > ori_array[i + 1]:
                    indices_array.append(i)
                else:
                    continue
            except:
                pass
        output_data = ori_array[0:indices_array[0] + 1]
        return indices_array

    def getUniqueYData(self, timer):
        ori_array = self.get_coord_data('y', timer)
        output = list(set(ori_array))
        return output

    def getUniqueZData(self, timer):
        ori_array = self.get_coord_data('z', timer)
        output = list(set(ori_array))
        return output

    def getNumberOfLayers(self, direction):
        if direction.lower() == 'x':
            array = self.getUniqueXData(0)
        elif direction.lower() == 'y':
            array = self.getUniqueYData(0)
        elif direction.lower() == 'z':
            array = self.getUniqueZData(0)
        else:
            print("coordinates can either be X, Y or Z")
        number = len(array)
        return number

    def getZLayerData(self, layer_number, param, timer):
        x_start = self.getXStartPoints(timer)
        z_data = self.get_element_data(timer, param)
        total_grid_in_z = self.getNumberOfLayers('z')
        if layer_number > 1:
            begin_index = x_start[layer_number - 2] + 1
        else:
            begin_index = 0
        if layer_number < total_grid_in_z:
            end_index = x_start[layer_number - 1] + 1
        else:
            end_index = 50
        output = z_data[begin_index:end_index]
        return output

    def getXDepthData(self, line_number, param, timer):
        element_data = self.get_element_data(timer, param)
        x_layers = self.getNumberOfLayers('x')
        z_layers = self.getNumberOfLayers('z')
        data_array = []
        for i in range(0, z_layers):
            data_array.append(element_data[line_number - 1])
            line_number = line_number + x_layers
        return data_array

    def getLayerData(self, direction, layer_number, timer, param):
        number_of_layers = self.getNumberOfLayers(direction)
        if layer_number > number_of_layers:
            raise ValueError("The specified layer is more than the number of layers in the model")
        else:
            if direction.lower() == 'z':
                data_array = self.getZLayerData(layer_number, param, timer)
            elif direction.lower() == 'x':
                data_array = self.getXDepthData(layer_number, param, timer)
        return data_array

    def get_unique_coord_data(self, direction, timer):
        if direction.lower() == 'x':
            value = self.getUniqueXData(timer)
        elif direction.lower() == 'y':
            value = self.getUniqueYData(timer)
        elif direction.lower() == 'z':
            value = self.getUniqueZData(timer)
        else:
            print("coordinates can either be X, Y or Z")
        return value


class MultiTough3(object):
    def __init__(self, simulator_type, file_location, file_title, prop):
        assert isinstance(file_location, list)
        assert isinstance(file_title, list)
        assert isinstance(prop, list)
        self.file_location = file_location
        self.file_title = file_title
        self.simulator_type = simulator_type
        self.prop = prop

    def __repr__(self):
        return 'Multiple Results from provided file locations and provided files for' + self.simulator_type

    def retrieve_data_multi_timeseries(self, grid_block_number, format_of_date='year'):
        data_table = pd.DataFrame()
        for i in range(0, len(self.file_location)):
            tough_data = Tough3(self.simulator_type, self.file_location[i], self.file_title[i])
            os.chdir(self.file_location[i])
            result_data = tough_data.get_timeseries_data(self.prop[0], grid_block_number)
            time_data = tough_data.convert_times(format_of_date='year')
            time_data_label = 'time' + str(i)
            result_data_label = 'result' + str(i)
            data_table[time_data_label] = pd.Series(time_data)
            data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def retrieve_data_multi_file_fixed_time(self, direction, time):
        data_table = pd.DataFrame()
        for i in range(0, len(self.file_location)):
            tough_data = Tough3(self.simulator_type, self.file_location[i], self.file_title[i])
            os.chdir(self.file_location[i])
            x_data = tough_data.get_coord_data(direction, time)
            result_data = tough_data.get_element_data(time, self.prop[i])
            x_data_label = 'x' + str(i)
            result_data_label = 'result' + str(i)
            data_table[x_data_label] = pd.Series(x_data)
            data_table[result_data_label] = pd.Series(result_data)
            print(tough_data.getXDepthData(1, self.prop[i], time))
        return data_table

    def retrieve_data_multi_file_fixed_time_layer(self, direction, time, layer_num):
        data_table = pd.DataFrame()
        for i in range(0, len(self.file_location)):
            tough_data = Tough3(self.simulator_type, self.file_location[i], self.file_title[i])
            os.chdir(self.file_location[i])
            x_data = tough_data.get_coord_data(direction, time)
            result_data = tough_data.getLayerData(direction, layer_num, time, self.prop[i])
            x_data_label = 'x' + str(i)
            result_data_label = 'result' + str(i)
            data_table[x_data_label] = pd.Series(x_data)
            data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def getMultiElementData(self, grid_block_number, format_of_date):
        data_table = pd.DataFrame()
        pd.set_option('float_format',  lambda x: '%.9f' % x)
        # pd.set_option('display.chop_threshold', 0.00000001)
        for i in range(0, len(self.file_location)):
            for j in range(0, len(self.prop)):
                os.chdir(self.file_location[i])
                tough_data = Tough3(self.simulator_type, self.file_location[i], self.file_title[i])
                result_data = tough_data.get_timeseries_data(self.prop[j], grid_block_number)
                time_data = tough_data.convert_times(format_of_date)
                time_data_label = self.prop[j] + 'time' + str(i) + str(j)
                result_data_label = self.prop[j] + 'result' + str(i) + str(j)
                data_table[time_data_label] = pd.Series(time_data)
                data_table[result_data_label] = pd.Series(result_data)
        print(data_table.iloc[15][result_data_label])
        return data_table
