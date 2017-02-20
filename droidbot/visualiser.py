import logging
from pynteractive import *
import urlparse, urllib


class Visualiser(object):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('DroidBot')
        self.logger.info("Starting Visualiser")

        self.graph = Graph(directed=True)
        self.node_count = 0
        self.graph.addNode(node_id = self.node_count, label ="root")
        self.prev_node = self.node_count
        self.next_node = None

        self.graph.view()

    def add_node(self, name, event_name, filename):
        self.node_count += 1
        self.graph.addNode(node_id=self.node_count, title=name, image='http://localhost:8000/droidbot_out/states/' + filename)
        self.next_node = self.node_count
        self.graph.addEdge(self.prev_node, self.next_node, label=event_name)
        self.prev_node = self.node_count
