############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: mnode.py
#   Description: main class for a node in the network that 
#   will store the model training on the data
#   TODO: figure out who best manages the data (node or network level)
#############################################################

import numpy as np
from message import Message
from embedding import Embedding
from dataloader import DataLoader
from models.ann import ANN

class Mnode:
    '''A model node on the network'''
    def __init__(self, id, data_path, hyperparams=None):
        '''
        Initialize a model node
        Input:
            id: id of the node (int)
            data_path: path to the data (string)
        Output:
            None
        '''

        self.id = id
        self.neighbors = [] # refs to nodes that are neighbors

        # intialize the model
        self.model = ANN(hyperparams=hyperparams)

        self.embedding = Embedding()
        self.data = DataLoader(data_path=data_path)

        # model flags
        self.is_trained = False
        self.is_updated = False
        self.is_selected = False

        # message flags
        self.is_sent = False
        self.is_received = False

        # message queues 
        self.incoming_msgs = []
        self.outgoing_msgs = []

        # any constraints on the node or model
        self.constraints = [] #TODO: figure out how to include constraints

        # initialize list of messages to send
        self.msgs_to_send = [Message()]

    

    # TODO: find better ways to represent the nodes
    def __str__(self):
        return f'Node {self.id}'

    def __repr__(self):
        return f'Node {self.id}'

    
    def process_incoming_msgs(self):
        '''
        Process incoming messages
        Input:
            None
        Output:
            None
        '''
        for msg in self.incoming_msgs:
            # process the message
            res = self.process_msg(msg)
            self.outgoing_msgs.append(res)
        # clear the incoming messages
        self.incoming_msgs = []

    def send_outgoing_msgs(self):
        '''
        Send outgoing messages
        Input:
            None
        Output:
            None
        '''
        for msg in self.outgoing_msgs:
            # send the message
            self.send_msg(msg)
        # clear the outgoing messages
        self.outgoing_msgs = []

    def send_msg(self, msg):
        '''
        Send a message to a neighbor
        Input:
            msg: message to send (Message)
        Output:
            None
        '''
        # get the receiver node
        receiver = msg.receiver
        
        # add the message to the receiver's incoming messages
        receiver.incoming_msgs.append(msg)
        # set the message as sent
        self.is_sent = True

    def process_msg(self, msg):
        '''
        Process a message, i.e. update the model or
        send a new message or do nothing, etc, 
        Input:
            msg: message to process (Message)
        Output:
            msg: processed message (Message)
        '''
        # process the message
        msg.content = 'processed'
        return msg

    def run(self):
        '''
        Run the node which includes the loading of the data batch,
        training the model, and sending the messages
            TODO: add the training part
        Input:
            None
        Output:
            None
        '''
        # process incoming messages
        print(f'Processing incoming messages for {self}')
        self.process_incoming_msgs()
        # send outgoing messages
        print(f'Sending outgoing messages for {self}')
        self.send_outgoing_msgs()
        # print queues
        print(f'Incoming messages for {self}: {self.incoming_msgs}')
        print(f'Outgoing messages for {self}: {self.outgoing_msgs}')

        
