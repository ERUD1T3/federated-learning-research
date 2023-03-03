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
    Class to handle data loading for the bleaching dataset
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
            # Categorical # 
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

            ## below are not used as predictors #######################################
            # 'Site_ID','Sample_ID',  'Reef_ID', , 'Site_Name', 'Date_Day', 'Date_Month',
            # 'Date_Year', 'Bleaching_ID', ,
            # 'S1', 'S2', 'S3', 'S4', 'Severity_Code',
            # 'Bleaching_Prevalence_Score', 'Code_Comment', 'Cover_ID', 
            # 'Calculated_S1', 'Calculated_S2', 'Calculated_S3',
            # 'Calculated_S4', 'Country_Name',
        ]

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
            target_index = header.index(self.target)
            # find the indices of the inputs
            input_indices = [header.index(i) for i in self.inputs]
            # iterate through the rows
            for row in csv_reader:
                # get the target
                target = [float(row[target_index])]
                # get the inputs
                inputs = [row[i] for i in input_indices]
                # convert the inputs to floats. TODO: handle non-float inputs
                inputs = [float(i) for i in inputs]
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

        