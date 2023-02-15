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
    Class to handle data loading
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

    def get_batch(self, batch_size=1):
        '''
        Read in the data and yield batches
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
            # iterate through the rows
            for row in csv_reader:
                # collect the data in batches
                batch.append(row)

                # yield the batch when it is full
                if len(batch) == batch_size:
                    yield batch
                    batch = []


        # yield the last batch if it is not empty
        if len(batch) > 0:
            yield batch

    @staticmethod
    def load_dir(self, dir_path):
        '''
        return a list of filepaths in a directory
        Input:
            dir_path: path to the directory (string)
        Output:
            filepaths: list of filepaths (list)
        '''

        filepaths = []
        # iterate through the files in the directory
        for file in os.listdir(dir_path):
            # get the full path to the file
            filepath = os.path.join(dir_path, file)
            # add the filepath to the list
            filepaths.append(filepath)

        return filepaths
            
        

        