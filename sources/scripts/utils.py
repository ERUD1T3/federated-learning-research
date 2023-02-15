############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: utils.py
#   Description: main file for miscellaneous functions 
#   and utilities that are used in the program
#############################################################

import pandas as pd

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