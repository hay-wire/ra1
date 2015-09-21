__author__ = 'haywire'
import pprint

class Node:
    #attribs are:
    #   attribs['filled'] = full
    #   attribs['angle'] = 120

    # and relations are:
    #   relations['inside'] = 'a'

    def __init__(self, name, relations={}, properties={}):
        self.name = name
        self.properties = relations
        self.relations = properties

    def addProperties(self, property, value):
        self.properties[property] = value

    def addAllProperties(self, properties):
        self.properties = property

    def addRelation(self, relationName, toNode):
        self.relations[relationName] = toNode

    def addAllRelations(self, relations):
        self.relations = relations

    def getRelationsWith(self, target):
        relations = []
        for relation, toNode in self.relations:
            if toNode == target:
                relations.append(relation)
        return relations

    def printNode(self):

        for property, val in self.properties:
            print "\t"+property+" : "+val


        for relation, val in self.relations:
            print "\t"+self.name + " ---"+relation+"--->"+val
