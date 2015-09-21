__author__ = 'haywire'

from Nodes import Node
from Card import Card

class Graph:
    def __init__(self):
        self.nodes = {}
        self.cards = []
        self.inCard = {}

    # cardOfNodes is a dict which records which node is in which card.
    # ex: cardOfNode['a'] = 'A'
    # cardOfNode['b'] = 'A'
    # cardOfNode['c'] = 'B' and so on
    def addCard(self, card):
        self.cards.append(card)

    def nodeExists(self, nodeName):
        exists = True
        try:
            z = self.nodes[nodeName]
        except KeyError:
            exists = False
        return exists

    # check if node exists. If not, then form a new node
    def addNode(self, nodeName, relations={}, properties={}):
        if self.nodeExists(nodeName) is not True :
            self.nodes[nodeName] = Node(nodeName, relations, properties)

    # def addRelation(self, fromNode, relation, toNode):
    #     self.ensureNodeExists(fromNode)
    #     self.ensureNodeExists(toNode)
    #     self.nodes[fromNode].addRelation(relation, toNode)
    #
    # def addAttribute(self, nodeName, propery, value):
    #     self.nodes[nodeName, propery, value]

    def diff(self, X, Y):
        # find difference between two cards X and Y
        print "Hello"

    def generatePossibleNodes(self, A, B, C):
        # analyse the relations between A and B and
        # determine all the possible solutions for
        D = [];

        #alanyse A:B first
        ABRel = A.getRelationsWith(B)
        ACRel = A.getRelationsWith(C)
        D.append(self.generateNode(ABRel))
        D.append(self.generateNode(ACRel))

    def generateNode(self, XYRelation):
        #XY relation is an array of keywords (eg for X 'inside' Y or X 'above' Y, XYRelation would be: ['inside', 'above'] )
        print "Hello"

    def testGeneratedNodes(self):
        print "Hello"

    def addCard(self, cardName):
        card = Card(cardName)

    def getNode(self, nodeName):
        if self.nodeExists(nodeName):
            return self.nodes[nodeName]
        return None

    def printAllCards(self):
        for nodeName, cardName in self.inCard:
            print nodeName + " is in card " + cardName


    def printAllNodes(self):
        for node in self.nodes:
            node.printNode()
            print "\n"






