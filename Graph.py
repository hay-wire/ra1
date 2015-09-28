__author__ = 'haywire'

from Nodes import Node
from Card import Card
import pprint
import operator
import re

class Graph:
    def __init__(self):
        self.nodes = {}
        self.nodesSimilarityScores = {}
        self.cards = {}
        self.inCard = {}
        self.correspondenceList = {}

    # cardOfNodes is a dict which records which node is in which card.
    # ex: cardOfNode['a'] = 'A'
    # cardOfNode['b'] = 'A'
    # cardOfNode['c'] = 'B' and so on
    def addCard(self, card):
        self.cards[card.name] = card

    def getCard(self, cardName):
        return self.cards[cardName]
        # for key in self.cards:
        #     card = self.cards[key]
        #     if card.name == cardName:
        #         return card

    def nodeExists(self, nodeName):
        exists = True
        try:
            z = self.nodes[nodeName]
        except KeyError:
            exists = False
        return exists

    # check if node exists. If not, then form a new node
    def addNode(self, nodeName, relations, properties):
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
        for key in self.cards:
            card = self.cards[key]
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
            try:
                print "\t: "+nodeX.properties.get(prop)+" : " + nodeY.properties.get(prop)

                if nodeX.properties.get(prop) == nodeY.properties.get(prop):
                    score = score + w
                else:
                    score = score - w
            except Exception, e:
                score = score - w
            print "Analysing factor: "+prop+"=>"+str(score)


        print "Score: ("+nodeX.name+","+nodeY.name+")="+str(score)
        return score

    def calculateSimilarityInCards(self, cardXName, cardYName):
        print "calculating similarity in "+cardXName+" and "+cardYName
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.cards)

        cardX = self.cards[cardXName]
        cardY = self.cards[cardYName]
        score = 0
        if len(cardY.nodes) == len(cardX.nodes):
            score += 5
        else:
            score -= 100

        correspondenceList = self.matchNodesInCards(cardXName, cardYName)
        for (x, y , w) in correspondenceList['related']:
            score += w

        return score

    def selectProbableSolnCard(self, solnCardsList, optionCardsList):
        scoreDict = {}
        for solnCardName in solnCardsList:
            for optionCardName in optionCardsList:
                print "Matching probable soln cards: "+solnCardName+" and "+optionCardName
                scoreDict[solnCardName+","+optionCardName] = self.calculateSimilarityInCards(solnCardName, optionCardName)

        sortedScoreList = sorted(scoreDict.items(), key=operator.itemgetter(1), reverse=True)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(sortedScoreList)
        (cardsPair, score) = sortedScoreList[0]
        cardNames = cardsPair.split(',')
        print "Winner is: "+cardNames[1]
        return cardNames[1]




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
        print "Card Y is: "
        pp.pprint(cardY.nodes)
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
        return correspondenceList


    def predictSolnCard(self, cardAName, cardBName, cardCName, cardDName):
        pp = pprint.PrettyPrinter(indent=4)

        D = Card(cardDName)
        #Predict number of nodes in D

        nodesInA = len(self.cards[cardAName].nodes)
        nodesInB = len(self.cards[cardBName].nodes)
        nodesInC = len(self.cards[cardCName].nodes)
        nodesInD = nodesInC - (nodesInA - nodesInB)            #################### got 1 que

        possibleSolns = {}
        for i in range(1,6):
            nodesInOption = len(self.cards[str(i)].nodes)
            print "Nodes in D are: "+ str(nodesInD)
            if nodesInOption == nodesInD:
                try :
                    # increment weight of the possible solution
                    possibleSolns[self.cards[str(i).name]] = possibleSolns[self.cards[str(i)].name]+1
                except Exception, e:
                    #solution key did not exists, so initiate a new key for the answer and assign it weight 1
                    possibleSolns[self.cards[str(i)].name] = 1

        print "Possible solutions: "
        pp.pprint(possibleSolns)

        #find the possible answer with maximum weight and return it as answer
        (ansName, w) = (-1, -1000)
        for ansCardName in possibleSolns:
            weight = possibleSolns[ansCardName]
            if weight > w:
                ansName = ansCardName

        print "Returning answer: "
        print ansName
        #return ansName
        # apply triangular properties and relations
        #  A--B
        #  |
        #  C
        #
        # - Regus
        #for i in range(1, nodesInOption):
        i=-1
        # deducting  for 2x2
        ABRel = self.correspondenceList[cardAName+','+cardBName]
        ACRel = self.correspondenceList[cardAName+','+cardCName]
        # from ACRel.related, remove the sets which contain elements from AB.deleted
        validNodesInC = []
        for (x,y,w) in ACRel['related']:
            if x not in ABRel['deleted']:
                # find the related pair of x in ABRel[related] and match it with x
                for (p, q,r) in ABRel['related']:
                    if p == x:
                        #got it. form CBRel
                        validNodesInC.append((y, p, q, 0))

        print "CABRelation nodes in C:"
        pp.pprint(validNodesInC)

        #also add newly added nodes
        #for x in ABRel['added']:
        #    validNodesInC.append(x)

        i=-1
        for (c, a, b, w) in validNodesInC:
            i+=1
            c = self.nodes[c]
            a = self.nodes[a]
            b = self.nodes[b]

            dNode = Node(D.name+"_"+str(i), {}, {}, {})
            print "Initialized dNode"+dNode.name
            dNode.printNode()
            D.addNode(dNode)
            print "Creating nodes in "+dNode.name +"("+c.name+","+a.name+","+b.name+")"

            # predict properties:
            for property in b.properties:
                print "Recreating property: "+b.name+"."+ property+"="+b.properties[property]+ " in "+dNode.name

                # predict value of d.property based on the property type
                valA  = a.properties[property]
                valB = b.properties[property]
                valC = c.properties[property]

                if valA.isdigit() and valB.isdigit() and valC.isdigit():
                    valD = int(valC)-(int(valA)-int(valB))
                    print "int D."+property+" = "+str(valD)
                    dNode.addProperties(property, str(valD) )

                # Predict Boolean property
                elif self.isBool(valA):
                    if valA == valB:
                        dNode.addProperties(property, valC)
                    else:
                        dNode.addProperties(property, self.invertBoolProperty(valC))

                else:
                    dNode.addProperties(property, self.predictFromChain(valA, valB, valC))

            #predict relations:
            #for relation in b.relations:
            #    dNode.addRelation(relation, b.relations[relation])


            dNode.addProperties('inCard', D.name)
            dNode.printNode()
            self.addNode(dNode.name, dNode.properties, {})

        self.addCard(D)
        return D.name



        """
        for (x,y,w) in ABRel['related']:
            i+=1
            x = self.nodes[x]
            y = self.nodes[y]


            dNode = Node(D.name+"_"+str(i))
            D.addNode(dNode.name)
            print ""
            print "Creating nodes in "+dNode.name+" for ("+x.name+","+y.name+","+str(w)+")"

            for property in y.properties:
                print "Recreating property: "+y.name+"."+ property+"="+y.properties[property]+ " in "+dNode.name

                # predict value of d.property based on the property type
                valA  = x.properties[property]
                valB = y.properties[property]
                valC = y.properties[property]

                if valA.isdigit() and valB.isdigit() and valC.isdigit():
                    valD = int(valC)-(int(valA)-int(valB))
                    print "int D."+property+" = "+str(valD)
                    dNode.addProperties(property, str(valD) )

                # Predict Boolean property
                elif self.isBool(valA):
                    if valA == valB:
                        dNode.addProperties(property, valC)
                    else:
                        dNode.addProperties(property, self.invertBoolProperty(valC))

                else:
                    dNode.addProperties(property, -1000)

            dNode.addProperties('inCard', D.name)

            dNode.printNode()
        """
        return ansName

    def isBool(self, property):
        if property in ['true', 'yes', 'false', 'no']:
            return True
        return False

    def invertBoolProperty(self, property):
        a = ['yes', 'no']
        if property  in a:
            return a[(a.index(property)+1)%2]
        b = ['true', 'false']
        if property in b:
            return a[(a.index(property)+1)%2]

    def predictNumericProperty(self, propA, propB, propC):
        return propC - (propA - propB)

    def predictFromChain(self, propA, propB, propC):
        if propA == propB:
            return propC
        elif propA == propC:
            return propB
        else:
            return "__unknown__"



