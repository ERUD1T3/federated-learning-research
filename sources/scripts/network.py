import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random
# from scipy.stats import powerlaw
import numpy as np
import pandas as pd

class Message:
    '''Message passed by node'''
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = 0

    def __str__(self) -> str:
        return f'Message {self.content} from {self.sender} to {self.receiver}'

    
class Node:
    '''A node device in the network'''
    def __init__(self, id, data):
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
        self.spam_params = [] # parameters for spam detection according to power law

        # message queues 
        self.incoming_msgs = []
        self.outgoing_msgs = []

        # # initialize list of incoming messages at random
        # for neighbor in self.neighbors:
        #     # generate a random message
        #     msg = Message(self.id, neighbor.id, None)
        #     # add the message to the incoming messages
        #     self.incoming_msgs.append(msg)
    
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

        
class Network:
    '''Network of nodes implemented as a graph'''
    def __init__(self, nodes=None):

        if nodes is None:
            self.nodes = {}
            self.edges = {}

            # initialize the network at random
            # generate a random number of nodes
            n = 100
            # generate a random number of edges
            m = np.random.randint(5, 10)
            # generate a random graph according to power law
            G = nx.powerlaw_cluster_graph(n, m, 0.1)
            # get the nodes
            nodes = list(G.nodes)
            # print(f'Nodes: {nodes}')
            # get the edges
            edges = list(G.edges)
            # print(f'edges: {edges}')
            # add the nodes to the network
            for node in nodes:
                self.add_node(node)
            # add the edges to the network
            for edge in edges:
                self.add_edge(edge[0], edge[1])
        else:
            self.nodes = nodes
            self.edges = {}

            # connected all the node to each other with distance as weight
            for id1, id2 in combinations(nodes, 2):
                # get node 1 and node 2
                node1 = self.nodes[id1]
                node2 = self.nodes[id2]
                self.add_edge(node1, node2) # TODO: add threshold so sites too far away are not connected


    def __str__(self):
        return f'Network with {len(self.nodes)} nodes and {len(self.edges)} edges'

    def plot(self):
        '''Plot the network'''
        # get the nodes
        nodes = list(self.nodes.keys())
        # get the edges
        edges = list(self.edges.keys())
        # create the graph
        G = nx.Graph()
        # add the nodes
        G.add_nodes_from(nodes)
        # add the edges
        G.add_edges_from(edges)
        # plot the graph
        nx.draw(G, with_labels=True)
        plt.title("Random Graph Generation")
        # make plot bigger
        plt.rcParams['figure.figsize'] = [10, 10]
        plt.show()

    def add_node(self, id, neighbors):
        '''Add a node to the network'''
        # create the node
        node = Node(id, neighbors)
        # add the node to the network
        self.nodes[id] = node
        # add the edges to the network
        for neighbor in neighbors:
            self.edges[(id, neighbor.id)] = 1

    def add_edge(self, node1, node2, threshold=1000):
        '''Add an edge to the network based on distance'''
        # calculate the distance between the nodes
        dist = calc_distance(node1, node2)
        # check if the distance is below the threshold
        # if dist < threshold:
        # add the edge to the network
        self.edges[(node1.id, node2.id)] = dist
        # add the edge to the nodes
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

            

    def get_node(self, id):
        '''Get a node from the network'''
        return self.nodes[id]

    def get_neighbors(self, id):
        '''Get a node's neighbors'''
        return self.nodes[id].neighbors
    
    def simulate(self, iterations=10):
        '''Run the message passing simulation'''
        # initialize the incoming messages at random for all nodes
        for node in self.nodes.values():
            # get node object
            # node = self.get_node(node)
            # generate a random message to each neighbor
            for neighbor in node.neighbors:
                print(f'Node {node} has neighbor {neighbor}')
                # generate a random message
                msg = Message(node, neighbor, None)
                # add the message to the incoming messages
                node.incoming_msgs.append(msg)
        
        # run the simulation
        for i in range(iterations):
            # run each node
            for node in self.nodes.values():
                node.run() # nodes communicate with each other
            # # print the network
            # print(self)
            # # plot the network
            # self.plot()

# all the columns

def calc_distance(node1, node2):
    '''Calculate the distance between two points'''
    # get lat and longs of nodes as floats
    lat1 = node1.data['Latitude_Degrees'].values[0]
    lon1 = node1.data['Longitude_Degrees'].values[0]
    lat2 = node2.data['Latitude_Degrees'].values[0]
    lon2 = node2.data['Longitude_Degrees'].values[0]

    # print(f'lat1: {lat1}, lon1: {lon1}, lat2: {lat2}, lon2: {lon2}')


    # convert to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    # calculate the distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
            
def main():
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
   

if __name__ == '__main__':
    main()