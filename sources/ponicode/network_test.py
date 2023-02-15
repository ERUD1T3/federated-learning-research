import network
import pytest

class Test_Network_Plot:
    
    @pytest.fixture()
    def network(self):
        return network.Network()
    

    def test_plot_1(self, network):
        result = network.plot()

