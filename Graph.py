__author__ = 'haywire'

from Nodes import Node
from Card import Card
import pprint
import operator

class Graph:
    def __init__(self):
        self.nodes = {}
        self.nodesSimilarityScores = {}
        self.cards = []
        self.inCard = {}
        self.correspondenceList = {}

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
        # weightCard = {
        #     'shape': 10,
        #     'size': 5,
        #     'angle': 3,
        #     'fill': 1
        # }
        # weightCard = {
        #     'shape': 1,
        #     'size': 1,
        #     'angle': 1,
        #     'fill': 1
        # }

        weightCard = {}
        for key in nodeX.properties.keys():
            weightCard[key] = 1

        for key in nodeY.properties.keys():
            weightCard[key] = 1

        print "Weight Card: "
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(weightCard)

        #if properties of the objects are similar, score them high else give them negative marking
        for prop, w in weightCard.iteritems():
            print "Analysing factor: "+prop+"=>"+str(w)

            try:
                print "\t: "+nodeX.properties.get(prop)+" : " + nodeY.properties.get(prop)

                if nodeX.properties.get(prop) == nodeY.properties.get(prop):
                    score = score + w
                else:
                    score = score - w
            except Exception, e:
                score = score - w
        print "Score: ("+nodeX.name+","+nodeY.name+")="+str(score)
        return score

    def matchNodesInCards(self, cardXName, cardYName):
        #    1. Fix cards
        #    2. Match objects in card A and B
        #    3. Identify next in series patterns between obx, oby => probable D
        #    4. score probable Ds to break tie
        #    5. return D
        pp = pprint.PrettyPrinter(indent=4)


        cardX = self.getCard(cardXName)
        cardY = self.getCard(cardYName)
        scoreDict = {}
        correspondenceList = {
            'related': [],
            'added': [],
            'deleted': [],
            #'score': -100
        }

        # form a set of all the nodes in the two cards to do elimination later
        cardsSet = []
        for nodeY in cardY.nodes:
            cardsSet.append(nodeY.name)

        # form the scoring matrix
        for nodeX in cardX.nodes:
            cardsSet.append(nodeX.name)
            for nodeY in cardY.nodes:
                # [a_p] [10]
                # [a_q] [12]
                # [b_p] [9]
                # [b_q] [13]
                scoreDict[nodeX.name+","+nodeY.name] = self.calculateSimilarityInNodes(self, nodeX, nodeY)

        # sort scoring matrix on scores
        sortedScoreList = sorted(scoreDict.items(), key=operator.itemgetter(1), reverse=True)
        print "Sorted score list: "
        self.nodesSimilarityScores['scoreDict'] = scoreDict
        self.nodesSimilarityScores['sorted'] = sortedScoreList
        #pp.pprint(sortedScoreList)
        for nodeNames, score in sortedScoreList:
            print "Cards set is now as follows: "
            pp.pprint(cardsSet)
            nodeX, nodeY = nodeNames.split(",")
            if nodeX in cardsSet:
                print nodeX+" in cardsSet"
            else:
                print nodeX+" not in cardsSet"

            if nodeY in cardsSet:
                print nodeY+" in cardsSet"
            else:
                print nodeY+" not in cardsSet"


            if nodeX in cardsSet and nodeY not in cardsSet:
                print "deleting "+ nodeX +","+ nodeY
                correspondenceList['deleted'].append(nodeX)
            elif nodeX not in cardsSet and nodeY in cardsSet:
                print "adding "+ nodeX +","+ nodeY
                correspondenceList['added'].append(nodeY)
            elif nodeX in cardsSet and nodeY in cardsSet:
                # both nodeX and nodeY are present in cardsList
                print "related "+ nodeX +","+ nodeY
                correspondenceList['related'].append((nodeX, nodeY, scoreDict[nodeX+","+nodeY]))

            # remove the just appended items from cards List
            # cardsSet.remove(nodeX)
            # cardsSet.remove(nodeY)
            try:
                cardsSet.remove(nodeX)
            except Exception, e:
                True # do nothing

            try:
                cardsSet.remove(nodeY)
            except Exception, e:
                True # do nothing

        self.correspondenceList[cardXName+","+cardYName] = correspondenceList
        pp.pprint(self.correspondenceList)


    def predictSolnCard(self, i, nodeAName, nodeBName, nodeCName):
        # deducting  for 2x2
        ABRel = self.correspondenceList[nodeAName+','+nodeBName]
        ACRel = self.correspondenceList[nodeAName+','+nodeCName]

        D = Card('D'+str(i))
        #Predict number of nodes in D

        cardsInA = len(self.cards[nodeAName].nodes)
        cardsInB = len(self.cards[nodeBName].nodes)
        cardsInC = len(self.cards[nodeCName].nodes)
        cardsInD = cardsInC + (cardsInA - cardsInB)             #################### got 1 que

        print "Cards in D are: "+ str(cardsInD)
        # apply triangular properties and relations
        #  A--B
        #  |
        #  C
        #
        # - Regus

























