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

class DataLoader:
    '''
    Class to handle data loading
    '''

    def __init__(self, data_path, batch_size, shuffle=True):
        '''
        Initialize the DataLoader class
        Input:
            data_path: path to the data (string)
            batch_size: size of the batch (int)
            shuffle: whether to shuffle the data or not (bool)
        Output:
            None

        '''
        self.data_path = data_path
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.data = self.read_data()

    def gen_data(self):
        '''
        Read in the data and yield batches
        Input:
            None
        Output:
            data: data in batches (list)
        '''

        # shuffle data
        if self.shuffle:
            random.shuffle(self.data)

        # yield batches
        for i in range(0, len(self.data), self.batch_size):
            yield self.data[i:i+self.batch_size]


        