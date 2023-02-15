############################################################
#   Dev(s): Josias Moukpe
#   Class: Research in CS
#   Date: 2/14/2023
#   file: main.py
#   Description: main file to run the decentralized 
#   parallel stochastic gradient descent algorithm 
#   for training artificial neural networks in simulation
#############################################################

# imports
import argparse
from network import Network
from mnode import Mnode

def parse_args():
    '''parse the arguments for the program'''

    parser = argparse.ArgumentParser(
        description='Federated Peer-to-Peer Learning for Artificial Neural Networks'
    )

    # TODO: add arguments necessary for running experiments

    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help='debug mode, prints statements activated (optional)'
    )

    # parse arguments
    args = parser.parse_args()
    return args


def main():
    '''
    main of the program
    Input:
        None
    Output:
        None
    
    '''
    args = parse_args() # parse arguments
    print(' args received',args)
    
    # node model hyperparameters
    h = {
        'input_dim': 10, # TODO: figure out how to get this from the dataset,
        'output_dim': 1,
        'num_epochs': 10,
        'batch_size': 32,
        'learning_rate': 0.01,
        # 'optimizer': 'sgd',
        'loss': 'mse',
        'activation': 'relu',
        'hidden_dims': [28, 28],
        'momentum': 0.9,
        'weight_decay': 0.0005,
        'data_dir': '/datasets/bleaching/'
        # 'k-fold': 5,
        # ... TODO: find minimal set of hyperparameters
    }

    # network configuration
    config = {
        'num_nodes': 100,
        'topology': 'random',
        'connectivity': 'powerlaw',
        'encryption': 'rsa',
        # 'model': 'mlp',
    }


    # create the network
    network = Network(
        hyperparams=h, 
        config=config
    )
    # print the network
    print(network)
    # plot the network
    network.plot()
    # simulate the network
    network.simulate()
    
if __name__ == '__main__':
    main()