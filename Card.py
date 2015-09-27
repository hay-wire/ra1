__author__ = 'haywire'
from Nodes import Node

class Card:
    # Name is A, or B or C or 1 or 2, etc
    # nodes are x, y, z, etc contained inside cards like A
    def __init__(self, name):
        self.name = name
        self.nodes = []
        #return self

    def addNode(self, nodeName):
        if not nodeName in self.nodes:
            self.nodes.append(nodeName)
            return True
        else :
            return False
