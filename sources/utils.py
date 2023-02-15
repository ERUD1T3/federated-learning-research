############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: utils.py
#   Description: main file for miscellaneous functions 
#   and utilities that are used in the program
#############################################################

import pandas as pd
import os

def get_group_data(data_path, group):
    '''
    Get the data for a specific group
    Input:
        data_path: path to the data (string)
        group: group to get the data for (string)
    Output:
        data: data for the group (list)
    '''

    # read csv file into a dataframe
    df = pd.read_csv(data_path)       
    # get the data for the group
    groups = df.groupby(group)
    print(f'Number of sites: {len(groups)}')


def load_dir(dir_path):
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

def log_csv(path, histories, headers):
    '''
    log the data to the csv file
    Input:
        path: path to the csv file (string)
        histories: list of lists of data (list)
        headers: list of headers (list)
    Output:
        None
    '''
    headers = ['e'] + headers
    # open the file
    with open(path, 'w') as f:
        # write the headers
        f.write(','.join(headers) + '\n')
        # write the data
        for h in range(len(histories[0])):
            line = f'{h},'
            for hh in range(len(histories)):
                line += str(histories[hh][h]) + ','
            f.write(line[:-1] + '\n')