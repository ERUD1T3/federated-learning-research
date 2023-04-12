############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: dataloader.py
#   Description: main file to handle the data management
#  and execute loads of data and split them into batches
#############################################################

import csv
import random
import os

class DataLoader:
    '''
    Class to handle data loading for the flbleaching dataset
    '''

    def __init__(self, data_path, shuffle=False):
        '''
        Initialize the DataLoader class
        Input:
            data_path: path to the data (string)
            shuffle: whether to shuffle the data or not (bool)
        Output:
            None

        '''
        self.data_path = data_path
        self.shuffle = shuffle
        self.target = ['Percent_Bleached_Sum']
        self.inputs = [
            ## Predictors ########################################################
            # Categorical #
            # 'Data_Source',  # (AGRRA, Donner, FRRP, Kumagai, McClanahan, Nuryana, Reef_Check, Safaie, Setiawan)
            # 'Ocean_Name',  # (Arabian Gulf, Atlantic, Indian, Pacific, Read Sea))
            # 'Realm_Name',  # (
            # # Central Indo-Pacific, Eastern Indo-Pacific, Western Indo-Pacific,
            # # Temperate Australasia, Temperate Northern Atlantic,
            # # Temperate Northern Pacific, Temperate Southern Africa,
            # # Tropical Atlantic, Tropical Eastern Pacific)
            # 'Exposure',  # (Exposed, Sheltered, Sometimes)
            # 'Bleaching_Level',  # (Colony, Population)
            # 'Substrate_Name', # (Hard Coral)
            # Continuous #
            'Latitude_Degrees', 'Longitude_Degrees', 'Distance_to_Shore',
            'Cyclone_Frequency', 'Depth_m', 'Percent_Cover_Sum', 'ClimSST',
            'Temperature_Kelvin', 'Temperature_Mean', 'Temperature_Minimum',
            'Temperature_Maximum', 'Temperature_Kelvin_Standard_Deviation',
            'Windspeed', 'SSTA', 'SSTA_Standard_Deviation', 'SSTA_Mean',
            'SSTA_Minimum', 'SSTA_Maximum', 'SSTA_Frequency', 'Turbidity',
            'SSTA_Frequency_Standard_Deviation', 'SSTA_FrequencyMax',
            'SSTA_FrequencyMean', 'SSTA_DHW', 'SSTA_DHW_Standard_Deviation',
            'SSTA_DHWMax', 'SSTA_DHWMean', 'TSA', 'TSA_Standard_Deviation',
            'TSA_Minimum', 'TSA_Maximum', 'TSA_Mean', 'TSA_Frequency',
            'TSA_Frequency_Standard_Deviation', 'TSA_FrequencyMax',
            'TSA_FrequencyMean', 'TSA_DHW', 'TSA_DHW_Standard_Deviation',
            'TSA_DHWMax', 'TSA_DHWMean',

            ## below are not used as predictors #######################################
            # 'Site_ID','Sample_ID',  'Reef_ID', , 'Site_Name', 'Date_Day', 'Date_Month',
            # 'Date_Year', 'Bleaching_ID', ,
            # 'S1', 'S2', 'S3', 'S4', 'Severity_Code',
            # 'Bleaching_Prevalence_Score', 'Code_Comment', 'Cover_ID', 
            # 'Calculated_S1', 'Calculated_S2', 'Calculated_S3',
            # 'Calculated_S4', 'Country_Name',
        ]

        self.categorical_inputs = [
            'Data_Source', # (AGRRA, Donner, FRRP, Kumagai, McClanahan, Nuryana, Reef_Check, Safaie, Setiawan)
            'Ocean_Name', # (Arabian Gulf, Atlantic, Indian, Pacific, Read Sea))
            'Realm_Name', # (
            # Central Indo-Pacific, Eastern Indo-Pacific, Western Indo-Pacific,
            # Temperate Australasia, Temperate Northern Atlantic,
            # Temperate Northern Pacific, Temperate Southern Africa,
            # Tropical Atlantic, Tropical Eastern Pacific)
            'Exposure', # (Exposed, Sheltered, Sometimes)
            'Bleaching_Level', # (Colony, Population)
            # 'Substrate_Name', # (Hard Coral)
        ]

    def handle_inputs(self, _input):
        """
        Handle the inputs
        Convert categorical inputs to one-hot
        Convert continuous inputs to float
        Input:
            _input: input data (float or string)
        Output:
            _input: processed input (float or list)
       """
        # if the input is a string, convert it to a one-hot vector
        if isinstance(_input, float):
            return _input

        if isinstance(_input, int):
            return float(_input)

        if isinstance(_input, str):
            # if _input in self.categorical_inputs:
            # if input_index == 0: # Data_Source
            if _input == 'AGRRA':
                return [1, 0, 0, 0, 0, 0, 0, 0, 0]
            elif _input == 'Donner':
                return [0, 1, 0, 0, 0, 0, 0, 0, 0]
            elif _input == 'FRRP':
                return [0, 0, 1, 0, 0, 0, 0, 0, 0]
            elif _input == 'Kumagai':
                return [0, 0, 0, 1, 0, 0, 0, 0, 0]
            elif _input == 'McClanahan':
                return [0, 0, 0, 0, 1, 0, 0, 0, 0]
            elif _input == 'Nuryana':
                return [0, 0, 0, 0, 0, 1, 0, 0, 0]
            elif _input == 'Reef_Check':
                return [0, 0, 0, 0, 0, 0, 1, 0, 0]
            elif _input == 'Safaie':
                return [0, 0, 0, 0, 0, 0, 0, 1, 0]
            elif _input == 'Setiawan':
                return [0, 0, 0, 0, 0, 0, 0, 0, 1]

        # elif input_index == 1: # Ocean_Name
            elif _input == 'Arabian Gulf':
                return [1, 0, 0, 0, 0]
            elif _input == 'Atlantic':
                return [0, 1, 0, 0, 0]
            elif _input == 'Indian':
                return [0, 0, 1, 0, 0]
            elif _input == 'Pacific':
                return [0, 0, 0, 1, 0]
            elif _input == 'Red Sea':
                return [0, 0, 0, 0, 1]

        # elif input_index == 2: # Realm_Name
            elif _input == 'Central Indo-Pacific':
                return [1, 0, 0, 0, 0, 0, 0, 0, 0]
            elif _input == 'Eastern Indo-Pacific':
                return [0, 1, 0, 0, 0, 0, 0, 0, 0]
            elif _input == 'Western Indo-Pacific':
                return [0, 0, 1, 0, 0, 0, 0, 0, 0]
            elif _input == 'Temperate Australasia':
                return [0, 0, 0, 1, 0, 0, 0, 0, 0]
            elif _input == 'Temperate Northern Atlantic':
                return [0, 0, 0, 0, 1, 0, 0, 0, 0]
            elif _input == 'Temperate Northern Pacific':
                return [0, 0, 0, 0, 0, 1, 0, 0, 0]
            elif _input == 'Temperate Southern Africa':
                return [0, 0, 0, 0, 0, 0, 1, 0, 0]
            elif _input == 'Tropical Atlantic':
                return [0, 0, 0, 0, 0, 0, 0, 1, 0]
            elif _input == 'Tropical Eastern Pacific':
                return [0, 0, 0, 0, 0, 0, 0, 0, 1]

        # elif input_index == 3: # Exposure
            elif _input == 'Exposed':
                return [1, 0, 0]
            elif _input == 'Sheltered':
                return [0, 1, 0]
            elif _input == 'Sometimes':
                return [0, 0, 1]

        # elif input_index == 4: # Bleaching_Level
            elif _input == 'Colony':
                return [1, 0]
            elif _input == 'Population':
                return [0, 1]
            elif _input == '':
                return float("-inf")
            else:
                return float(_input)




    def get_batch(self, batch_size=1):
        '''
        Read in the data and yield batches
        target is the Percent_Bleached_Sum
        input is the rest of the columns
        Input:
            batch_size: size of the batch (int)
        Output:
            data: data in batches (list)
        '''

        batch = []

        # open the csv file
        with open(self.data_path, 'r') as f:
            # create a csv reader
            csv_reader = csv.reader(f)
            # get the header
            header = next(csv_reader)
            # find the index of the target
            target_index = header.index(self.target[0])
            # find the indices of the inputs
            input_indices = [header.index(i) for i in self.inputs]
            # iterate through the rows
            for row in csv_reader:
                # get the target
                target = [float(row[target_index])]
                # get the inputs
                inputs = [row[i] for i in input_indices]
                # convert the inputs to floats. TODO: handle non-float inputs
                inputs = [self.handle_inputs(v) for v in inputs]
                # collect the data in batches
                batch.append((inputs, target))

                # yield the batch when it is full
                if len(batch) == batch_size:
                    # if shuffle is true, shuffle the data
                    if self.shuffle:
                        random.shuffle(batch)
                    yield batch
                    batch = []


        # yield the last batch if it is not empty
        if len(batch) > 0:
            # if shuffle is true, shuffle the data
            if self.shuffle:
                random.shuffle(batch)
            yield batch

        