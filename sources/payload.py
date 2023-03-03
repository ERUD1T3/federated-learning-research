class Payload:
    '''
    Payload for messages content
    to be used as content type
    (other payload to be used)
    '''

    def __init__(self,
                 weight_deltas,
                 source_site,
                 timestamp,
                 sequence,
                 data_size,
                 epochs_delta,
                 loss):
        '''
        Initialize the Payload class
        Input:
            weight_deltas: the deltas for each weight in a structure mirroring the learned model (ANN, CNN,...)
            source_site: the description of the site position as longitude/latitude usable in the distance function
            timestamp: the time of the message composition in usec (optional given a timestamp already present in message)
            sequence: the counter of the payloads from this site, incremented at each composition
            data_size: how many samples were used in the training since the last sequence number
            epochs_delta: how many epochs were run since the last sequence from this site.
        Output:
        '''
        self.weight_deltas = weight_deltas # datastructure of weights/deltas
        self.souce_site = source_site # sender sends and receiver computes distance
        self.timestamp = timestamp # time of payload creation standard utc time
        self.sequence = sequence # digit representing the sequence of payloads from this site
        self.data_size = data_size # more weight to the payload with more data
        self.epochs_delta = epochs_delta # more weight to the payload with more epochs
        self.loss = loss
        # data and epochs quantify the quality of delta
        # TODO: some indicator of convergence of the model to the data
        # general set of features


    def __str__(self):
        return f'Payload: seq {self.sequence}, epochs {self.epochs_delta}'

