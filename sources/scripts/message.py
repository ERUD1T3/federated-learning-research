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

    def __init__(self, sender, receiver, content):
        '''
        Initialize the Message class
        Input:
            sender: sender of the message (Node)
            receiver: receiver of the message (Node)
            content: content of the message (np.array)
        Output:
            None
        '''

        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = time.time() # time at which the message was sent

    def __str__(self):
        return f'Message {self.content} from {self.sender} to {self.receiver}'

    def __repr__(self):
        return f'Message {self.content} from {self.sender} to {self.receiver}'

    def __eq__(self, other):
        return self.content == other.content
