############################################################
#   Dev(s): Josias Moukpe, 
#   Class: Research in CS
#   Date: 2/14/2023
#   file: network.py
#   Description: main class for the network of nodes
#   that will be used to train the nodes models in parallel
#   using the federated learning algorithm
#############################################################


import matplotlib.pyplot as plt
import networkx as nx
from random import random
import numpy as np
from mnode import Mnode


class Network:
    '''Network of nodes implemented as a graph'''
    def __init__(self, 
        config=None,
        hyperparams=None, 
        nodes=None, 
        edges=None
    ):
        '''
        Initialize the Network class
        Input:
            nodes: nodes in the network (dict)
            edges: edges in the network (dict)
            hyperparams: hyperparameters for the network (dict)
            config: configuration for the network (dict)
        Output:
            None
        '''

        # initialize the network

        if nodes is None:
            self.nodes = {}
            self.edges = {}

            # initialize the network at random
            # get a random number of nodes
            n = config['num_nodes']
            # get a random number of edges
            e = config['num_edges']

            if config['connectivity'] == 'powerlaw':
                # generate a random graph according to power law
                self.G = nx.powerlaw_cluster_graph(n, e, 0.1)
            elif config['connectivity'] == 'random':
                # generate a random graph
                self.G = nx.gnm_random_graph(n, e)

            # get the nodes
            node_ids = list(self.G.nodes)
            # print(f'Nodes: {nodes}')
            # get the edges
            edge_ids = list(self.G.edges)
            # print(f'edges: {edges}')
            # add the nodes to the network
            for node_id in node_ids:
                self.add_node(node_id)
            # add the edges to the network
            for edge_id in edge_ids:
                # get the nodes
                node1 = self.nodes[edge_id[0]]
                node2 = self.nodes[edge_id[1]]
                # add the edge to the network
                self.add_edge(node1, node2)

        else:
            # TODO: load the network from a file
            pass
            # self.nodes = nodes
            # self.edges = {}

            # # connected all the node to each other with distance as weight
            # for id1, id2 in combinations(nodes, 2):
            #     # get node 1 and node 2
            #     node1 = self.nodes[id1]
            #     node2 = self.nodes[id2]
            #     self.add_edge(node1, node2) # TODO: add threshold so sites too far away are not connected


    def __str__(self):
        return f'Network with {len(self.nodes)} nodes and {len(self.edges)} edges'

    def plot(self):
        '''Plot the network'''
        # # get the nodes
        # nodes = list(self.nodes.keys())
        # # get the edges
        # edges = list(self.edges.keys())
        # # create the graph
        # G = nx.Graph()
        # # add the nodes
        # G.add_nodes_from(nodes)
        # # add the edges
        # G.add_edges_from(edges)
        # plot the graph
        nx.draw(self.G, with_labels=True)
        plt.title("Network")
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