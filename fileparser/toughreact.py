import csv
import os
import pytough.t2listing as toughreact
import utils.utilitiestoughreact as fileprocessor
import utils.utilities as processor
import pandas as pd
import plotting.plottough as plot
from collections import OrderedDict


class ToughReact(object):
    def __init__(self, simulatortype, filelocation, filetitle):
        self.filelocation = filelocation
        os.chdir(self.filelocation)
        self.filetitle = filetitle
        self.simulatortype = simulatortype
        self.data = toughreact.toughreact_tecplot(self.filetitle, self.get_elements())

    def __repr__(self):
        return 'Results from ' + self.filelocation + ' in ' + self.filetitle + ' for ' + self.simulatortype

    def getParameters(self):
        return self.data.element.column_name

    def get_elements(self):
        tre1 = fileprocessor.UtilitiesToughreact(self.filelocation, 'CONNE')
        tre1.findword()
        tre1.sliceoffline()
        tre1.writetofile()
        with open('test.txt') as f:
            grid_blocks = f.read().splitlines()
        return grid_blocks

    def get_times(self):
        time_data = self.data.times
        time_data2 = list(time_data)
        value = processor.Utilities()
        time_data = value.choplist(time_data2, 40)
        return time_data

    def convert_times(self, format_of_date):
        intermediate = self.get_times()
        firstUsage = processor.Utilities()
        timeyear = firstUsage.convert_times(intermediate, format_of_date)
        return timeyear

    def get_timeseries_data(self, param, gridblocknumber):
        os.chdir(self.filelocation)
        grid = self.get_elements()[gridblocknumber]
        mf = self.data.history([(grid, param)])
        timeseries = mf[1]
        timeseries = list(timeseries)
        value = processor.Utilities()
        timeseries = value.choplist(timeseries, 40)
        return timeseries

    def get_element_data(self, time, param):
        self.data.set_time(time)
        final_data = self.data.element[param]
        return final_data

    def get_X_data(self, time):
        return self.get_element_data(time, 'X(m)')

    def get_Y_data(self, time):
        return self.get_element_data(time, 'Y(m)')

    def get_Z_data(self, time):
        return self.get_element_data(time, 'Z(m)')

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
        z_data = self.get_element_data(timer, param)
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



class MultiToughReact(object):
    def __init__(self, simulator_type, file_location, file_title, prop, **kwargs):
        assert isinstance(file_location, list)
        assert isinstance(file_title, list)
        assert isinstance(prop, list)
        self.file_location = file_location
        self.file_title = file_title
        self.simulator_type = simulator_type
        self.prop = prop
        self.x_slice_value = kwargs.get('x_slice_value')

    def __repr__(self):
        return 'Multiple Results from provided file locations and provided files for' + self.simulator_type

    def retrieve_data_multi_timeseries(self, grid_block_number, format_of_date='year'):
        data_table = pd.DataFrame()
        for i in range(0, len(self.file_location)):
            tough_data = ToughReact(self.simulator_type, self.file_location[i], self.file_title[i])
            print(self.file_location[i])
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
            tough_data = ToughReact(self.simulator_type, self.file_location[i], self.file_title[i])
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
            tough_data = ToughReact(self.simulator_type, self.file_location[i], self.file_title[i])
            os.chdir(self.file_location[i])
            x_data = tough_data.get_coord_data(direction, time)
            result_data = tough_data.getLayerData(direction, layer_num, time, self.prop[i])
            x_data_label = 'x' + str(i)
            result_data_label = 'result' + str(i)
            data_table[x_data_label] = pd.Series(x_data)
            data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def getMultiPropDistance(self, directionX, directionY, time, layer_num):
        data_table = pd.DataFrame()
        for i in range(0, len(self.file_location)):
            for j in range(0, len(self.prop)):
                os.chdir(self.file_location[i])
                tough_data = ToughReact(self.simulator_type, self.file_location[i], self.file_title[j])
                x_data = tough_data.get_unique_coord_data(directionX, time)
                result_data = tough_data.getLayerData(directionY, layer_num, time, self.prop[j])
                if self.x_slice_value is not None:
                    inter = processor.Utilities()
                    time_data, result_data = inter.cutdata(x_data, result_data, self.x_slice_value)
                time_data_label = self.prop[j] + 'time' + str(i) + str(j)
                result_data_label = self.prop[j] + 'result' + str(i) + str(j)
                data_table[time_data_label] = pd.Series(x_data)
                data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def getMultiFileDistance(self, directionX, directionY, time, layer_num):
        data_table = pd.DataFrame()
        for i in range(0, len(self.prop)):
            for j in range(0, len(self.file_location)):
                os.chdir(self.file_location[j])
                tough_data = ToughReact(self.simulator_type, self.file_location[j], self.file_title[j])
                x_data = tough_data.get_unique_coord_data(directionX, time)
                result_data = tough_data.getLayerData(directionY, layer_num, time, self.prop[i])
                if self.x_slice_value is not None:
                    inter = processor.Utilities()
                    time_data, result_data = inter.cutdata(x_data, result_data, self.x_slice_value)
                time_data_label = self.prop[i] + 'time' + str(i) + str(j)
                result_data_label = self.prop[i] + 'result' + str(i) + str(j)
                data_table[time_data_label] = pd.Series(x_data)
                data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def getMultiElementData(self, grid_block_number, format_of_date='year'):
        data_table = pd.DataFrame()
        for i in range(0, len(self.file_location)):
            for j in range(0, len(self.prop)):
                os.chdir(self.file_location[i])
                tough_data = ToughReact(self.simulator_type, self.file_location[i], self.file_title[j])
                result_data = tough_data.get_timeseries_data(self.prop[j], grid_block_number)
                time_data = tough_data.convert_times(format_of_date='year')
                if self.x_slice_value is not None:
                    inter = processor.Utilities()
                    time_data, result_data = inter.cutdata(time_data, result_data, self.x_slice_value)
                time_data_label = self.prop[j] + 'time' + str(i) + str(j)
                result_data_label = self.prop[j] + 'result' + str(i) + str(j)
                data_table[time_data_label] = pd.Series(time_data)
                data_table[result_data_label] = pd.Series(result_data)
        return data_table

    def getDataPerPanelSingle(self, grid_block_number, panel, filetype, format_of_date):
        all_data = []
        for i in range(len(self.file_location)):
            data_table = pd.DataFrame()
            os.chdir(self.file_location[i])
            tough_data = ToughReact(self.simulator_type, self.file_location[i], filetype)
            result_data = tough_data.get_timeseries_data(panel, grid_block_number)
            time_data = tough_data.convert_times(format_of_date='year')
            if self.x_slice_value is not None:
                inter = processor.Utilities()
                time_data, result_data = inter.cutdata(time_data, result_data, self.x_slice_value)
            time_data_label = panel + 'time' + str(i)
            result_data_label = panel + 'result' + str(i)
            data_table[time_data_label] = pd.Series(time_data)
            data_table[result_data_label] = pd.Series(result_data)
            all_data.append(data_table)
        # all_data[0].merge(all_data[1])
        # return data_table
        # all_data[0]['tmp'] = 1
        # all_data[1]['tmp'] = 1
        # df = pd.merge(all_data[0], all_data[1], on=['tmp'])
        # df = df.drop('tmp', axis=1)
        return all_data
