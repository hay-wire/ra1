__author__ = 'haywire'
import pprint

class Node:
    #attribs are:
    #   attribs['filled'] = full
    #   attribs['angle'] = 120

    # and relations are:
    #   relations['inside'] = 'a'

    def __init__(self, name, relations={}, properties={}, similarity={}):
        self.name = name
        self.properties = properties
        self.relations = relations
        self.similarity = similarity

    def addProperties(self, property, value):
        self.properties[property] = value

    def addAllProperties(self, properties):
        self.properties = property

    def addRelation(self, relationName, toNode):
        self.relations[relationName] = toNode

    def addAllRelations(self, relations):
        self.relations = relations

    def addSimilarity(self, targetCard, targetNode, score):
        self.similarity[targetCard+'.'+targetNode] = score

    def getRelationsWith(self, target):
        relations = []
        for relation, toNode in self.relations:
            if toNode == target:
                relations.append(relation)
        return relations

    def printNode(self):

        print "Node "+self.name
        print "\tProperties: "
        for property, val in self.properties.iteritems():
            print "\t\t"+property+" : "+val

        print "\tRelations: "
        for relation, val in self.relations.iteritems():
            print "\t\t"+self.name + " -"+relation+"-> "+val
