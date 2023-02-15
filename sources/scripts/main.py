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
        'num_epochs': 10,
        'batch_size': 32,
        'learning_rate': 0.01,
        # 'optimizer': 'sgd',
        # 'loss': 'mse',
        # 'activation': 'relu',
        # 'hidden_dims': [28, 28],
        # ... TODO: find minimal set of hyperparameters
    }

    # network configuration
    config = {
        'num_nodes': 100,
        'topology': 'random',
        'connectivity': 'powerlaw',
        'model': 'mlp',
        'dataset': 'mnist',
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