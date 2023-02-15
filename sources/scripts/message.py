############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: message.py
#   Description: main class for the messages being actually
#   exchanged between nodes in the network
#############################################################

import numpy as np
import time

class Message:
    '''Message passed between nodes during training'''

    def __init__(self, sender_id, receiver_id, content):
        '''
        Initialize the Message class
        Input:
            sender: sender of the message (Node)
            receiver: receiver of the message (Node)
            content: content of the message (np.array)
        Output:
            None
        '''

        self.message_id = np.random.randint(0, 1000000) # random message id for now
        self.sender = sender_id
        self.receiver = receiver_id
        self.content = content
        self.timestamp = time.time() # time at which the message was sent

    def __str__(self):
        return f'Message {self.content} from {self.sender} to {self.receiver}'

    def __repr__(self):
        return f'Message {self.content} from {self.sender} to {self.receiver}'

    def __eq__(self, other):
        return self.content == other.content
