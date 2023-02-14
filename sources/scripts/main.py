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
    '''main of the program'''
    args = parse_args() # parse arguments
    print(' args received',args)
    
    # hyperparameters
    h = {}
    # read csv file into a dataframe
    df = pd.read_csv('data/bleaching.csv')          
    # split the data by Site_ID
    sites = df.groupby('Site_ID')
    print(f'Number of sites: {len(sites)}')
    # create a node for every site and add the site data to the node
    nodes = {}
    for site in sites:
        # get the site id
        site_id = site[0]
        # get the site data
        site_data = site[1]
        # create a node for the site
        node = Node(site_id, site_data)
        # add the node to the nodes dictionary
        nodes[site_id] = node

    # create the network
    network = Network(nodes)
    # print the network
    print(network)
    # plot the network
    network.plot()
    # simulate the network
    # network.simulate()



    
if __name__ == '__main__':
    main()