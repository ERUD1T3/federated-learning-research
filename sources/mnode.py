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
from sources.message import Message
from sources.embedding import Embedding
from sources.dataloader import DataLoader
from sources.models.ann import ANN
from sources.utils import load_dir

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
        # self.msgs_to_send = [Message()]

    

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

        # training the model
        self.node_train()

        # process incoming messages
        print(f'Processing incoming messages for {self}')
        self.process_incoming_msgs()
        # send outgoing messages
        print(f'Sending outgoing messages for {self}')
        self.send_outgoing_msgs()
        # print queues
        print(f'Incoming messages for {self}: {self.incoming_msgs}')
        print(f'Outgoing messages for {self}: {self.outgoing_msgs}')

        
    def load_data(self):
        '''
        Load the data
        Input:
            None
        Output:
            None
        '''
        # load the data
        self.data = DataLoader(data_path=self.data_path)

    def node_train(self):
        '''
        Train the model
        Input:
            None
        Output:
            None
        '''

        self.model.train(self.data)


if __name__ == '__main__':
    # test training on the node
    
    # 1000060 -> 0
    # node model hyperparameters
    h = {
        'input_dim': 1,  # TODO: figure out how to get this from the dataset,
        'output_dim': 1,
        'num_epochs': 10,
        'batch_size': 1,
        'learning_rate': 0.01,
        # 'optimizer': 'sgd',
        'loss': 'mse',
        'activation': 'relu',
        'hidden_dims': [28, 28],
        'momentum': 0.9,
        'weight_decay': 0.0005,
        'data_dir': '../datasets/flbleaching',
        'k_fold': 5,
        # ... TODO: find minimal set of hyperparameters
    }

    # load the datafiles name from the data directory
    datafiles = load_dir(h['data_dir'])
    node = Mnode(id=4, data_path=datafiles[4], hyperparams=h)

    # get a batch
    batch = node.data.get_batch()

    # put it into list
    # batch = [x for x in batch]

    # print a batch of the data
    print(batch)

    # train the model
    loss = node.model.training_step(batch)
    # print the loss
    print(loss)