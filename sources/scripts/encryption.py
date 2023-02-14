############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: encryption.py
#   Description: This file contains the encryption 
#   algorithm for the messages being passed
#############################################################

import random

class encryption:
    '''
        This class contains the encryption algorithm 
        for the messages being passed
        TODO: implementation TBD
    '''
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.key = random.randint(0, 26)
        self.encrypted = ''
        self.decrypted = ''