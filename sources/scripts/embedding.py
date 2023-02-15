############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: embedding.py
#   Description: main class that will handle the embedding
#   of the node into a higher dimensional embedding space 
#############################################################

import numpy as np

class Embedding:
    '''
    Class to handle the embedding of the node into 
    a higher dimensional embedding space
    '''

    def __init__(self, embed_dim=4):
        '''
        Initialize the Embedding class
        Input:
            embed_dim: dimension of the embedding space (int)
        Output:
            None
        '''

        self.embed_dim = embed_dim
        self.embedding = np.array([
            0, # longitude
            0, # latitude
            0, # elevation
            0, # 0 land, 1 water
        ])

    def set_embedding(self, **kwargs):
        '''
        Set the embedding of the node
        Input:
            kwargs: keyword arguments for the embedding
        Output:
            None
        '''
        self.embedding = np.array([
            kwargs['longitude'],
            kwargs['latitude'],
            kwargs['elevation'],
            kwargs['water']
        ])

    def get_geo_distance(self, other):
        '''
        Compute the geodesic distance between two nodes
        Input:
            other: other node embedding (Embedding)
        Output:
            distance: geodesic distance between the two nodes (float)
        '''

        # get the coordinates of the two nodes
        lat1, lon1 = self.embedding[1], self.embedding[0]
        lat2, lon2 = other.embedding[1], other.embedding[0]

        # convert to radians
        lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

        # compute the distance
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
        c = 2 * np.arcsin(np.sqrt(a))
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles

        # return the distance
        return c * r

    def get_euclidean_distance(self, other):
        '''
        Compute the euclidean distance between two nodes with 
        the same embedding space and some coefficients
        Input:
            other: other node embedding (Embedding)
        Output:
            distance: euclidean distance between the two nodes (float)
        '''
        coefficients = np.array([
            1, # longitude
            1, # latitude
            1, # elevation
            1, # 0 land, 1 water
        ])

        # compute the distance
        distance = np.linalg.norm(self.embedding - other.embedding) * coefficients

        # return the distance
        return distance

    
    def __str__(self) -> str:
        '''
        String representation of the embedding
        Input:
            None
        Output:
            string representation of the embedding vector (string)
        '''
        return f'Embedding({self.embedding})'

    
    def __repr__(self) -> str:
        '''
        String representation of the embedding
        Input:
            None
        Output:
            string representation of the embedding vector (string)
        '''
        return f'Embedding({self.embedding})'