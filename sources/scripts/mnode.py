############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: mnode.py
#   Description: main class for a node in the network that 
#   will store the model training on the data
#############################################################

import numpy as np
from message import Message
from embedding import Embedding
from dataloader import DataLoader

class Mnode:
    '''A model node on the network'''
    def __init__(self, id, data):
        '''
        Initialize a model node
        Input:
            id: id of the node (int)
            data: data to train on (np.array)
        Output:
            None
        '''

        self.id = id
        self.neighbors = []
        # self.constraints = []
        self.model = None
        self.data = data
        self.is_trained = False
        self.is_updated = False
        self.is_selected = False
        self.is_sent = False
        self.is_received = False
        self.embedding_vec = [] # parameters for spam detection according to power law

        # message queues 
        self.incoming_msgs = []
        self.outgoing_msgs = []

        # # initialize list of incoming messages at random
        # for neighbor in self.neighbors:
        #     # generate a random message
        #     msg = Message(self.id, neighbor.id, None)
        #     # add the message to the incoming messages
        #     self.incoming_msgs.append(msg)
    

    # TODO: find better ways to represent the nodes
    def __str__(self):
        return f'Node {self.id}'

    def __repr__(self):
        return f'Node {self.id}'

    
    def process_incoming_msgs(self):
        '''Process incoming messages'''
        for msg in self.incoming_msgs:
            # process the message
            res = self.process_msg(msg)
            self.outgoing_msgs.append(res)
        # clear the incoming messages
        self.incoming_msgs = []

    def send_outgoing_msgs(self):
        '''Send outgoing messages'''
        for msg in self.outgoing_msgs:
            # send the message
            self.send_msg(msg)
        # clear the outgoing messages
        self.outgoing_msgs = []

    def send_msg(self, msg):
        '''Send a message to a neighbor'''
        # get the receiver node
        receiver = msg.receiver
        
        # add the message to the receiver's incoming messages
        receiver.incoming_msgs.append(msg)
        # set the message as sent
        self.is_sent = True

    def process_msg(self, msg):
        '''Process a message'''
        # process the message
        msg.content = 'processed'
        return msg

    def run(self):
        '''Run the node'''
        # do stuff 
        # process incoming messages
        print(f'Processing incoming messages for {self}')
        self.process_incoming_msgs()
        # send outgoing messages
        print(f'Sending outgoing messages for {self}')
        self.send_outgoing_msgs()
        # print queues
        print(f'Incoming messages for {self}: {self.incoming_msgs}')
        print(f'Outgoing messages for {self}: {self.outgoing_msgs}')

        
