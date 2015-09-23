__author__ = 'haywire'

from Nodes import Node
from Card import Card
import pprint

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

    def getCard(self, cardName):
        for card in self.cards:
            if card.name == cardName:
                return card

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
        D = []

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

    def getNode(self, nodeName):
        if self.nodeExists(nodeName):
            return self.nodes[nodeName]
        return None

    def printAllinCards(self):
        for nodeName, card in self.inCard.iteritems():
            print nodeName + " is in card " + card

        print "Cards Details:"
        for card in self.cards:
            print card.name
            for node in card.nodes:
                print "\t"+node.name

    def printAllNodes(self):
        # print "Graph.nodes:"
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.nodes)

        for nodeName, node in self.nodes.iteritems():
            node.printNode()
            print "\n"


    @staticmethod
    def calculateSimilarityInNodes(self, nodeX, nodeY):
        score = 0
        weightCard = {
            'shape': 10,
            'size': 5,
            'angle': 3,
            'fill': 1
        }
        #if properties of the objects are similar, score them high else give them negative marking
        for prop, w in weightCard:
            if nodeX.properties[prop] == nodeY.properties[prop]:
                score = score + w
            else:
                score = score - w

        return score

    def matchNodesInCards(self, cardXName, cardYName):
        #    1. Fix cards
        #    2. Match objects in card A and B
        #    3. Identify next in series patterns between obx, oby => probable D
        #    4. score probable Ds to break tie
        #    5. return D

        cardX = self.getCard(cardXName)
        cardY = self.getCard(cardYName)










