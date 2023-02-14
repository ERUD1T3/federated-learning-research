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

    def __init__(self, node, embed_dim):
        '''
        Initialize the Embedding class
        Input:
            node: node to embed (MNode)
            embed_dim: dimension of the embedding space (int)
        Output:
            None
        '''

        self.node = node
        self.embed_dim = embed_dim
        self.embedding = self.get_embedding()

    def get_embedding(self):
        '''
        Get the embedding of the node
        Input:
            None
        Output:
            embedding: embedding of the node (np.array)
        '''

        # get the embedding of the node
        embedding = self.node.model.get_weights()[0]

        # reshape the embedding
        embedding = np.reshape(embedding, (self.embed_dim,))

        return embedding