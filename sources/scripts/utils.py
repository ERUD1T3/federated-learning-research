############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: utils.py
#   Description: main file for miscellaneous functions 
#   and utilities that are used in the program
#############################################################
import random
import numpy as np
import numba as nb


def onehot( attr, value):
    '''
    Preprocess to convert a data instance 
    to one-of-n/onehot encoding
    '''
    # get the index of the value
    encoded = [0.0 for _ in range(len(self.attributes[attr]))]
    encoded[self.attributes[attr].index(value)] = 1.0

    return encoded


# all the columns

def get_phys_dist(node1, node2):
    '''Calculate the distance between two points'''
    # get lat and longs of nodes as floats
    lat1 = node1.data['Latitude_Degrees'].values[0]
    lon1 = node1.data['Longitude_Degrees'].values[0]
    lat2 = node2.data['Latitude_Degrees'].values[0]
    lon2 = node2.data['Longitude_Degrees'].values[0]

    # print(f'lat1: {lat1}, lon1: {lon1}, lat2: {lat2}, lon2: {lon2}')


    # convert to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    # calculate the distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r