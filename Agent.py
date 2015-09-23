# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
from Graph import Graph
from Card import Card
import pprint

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):

        if problem.hasVerbal and problem.problemType == '2x2':
            graph = self.formSemanticNet(problem)
            print "Printing graph: "
            graph.printAllinCards()
            graph.printAllNodes()
        return -1

    def formSemanticNet(self, problem):
        graph = Graph()
        inCard = {}
        pp = pprint.PrettyPrinter(indent=4)

        #populate all inCard[obects] = figure, before parsing other things
        # example inCards[b] = A
        for figName, figure in problem.figures.iteritems():
            # print "Figure: "+figName
            # pp.pprint(figure.objects)

            for objName, obj in figure.objects.iteritems():
                inCard[obj.name] = figure.name
                #pp.pprint(obj.attributes)

        # print "inCards are: "
        # pp.pprint(inCard)
        graph.inCard = inCard

        print "done building inCards. Initiating SemNet construction..."
        # now we can identify which attribute is an attribute and which attribute is a relation
        for figName, figure in problem.figures.iteritems():
            # print "Parsing Figure: "+figName
            # print figure.visualFilename
            # pp.pprint(figure.objects)

            card = Card(figure.name)
            for objName, obj in figure.objects.iteritems():
                properties = {}
                properties['inCard'] = figure.name # add the additional property to identify the parent figure
                relations = {}
                #clientForMigration.php

                #print "Object attributes:"
                #pprint.pprint(obj.attributes)
                for attrib, val in obj.attributes.iteritems():
                    if val in inCard:
                        # relations are saved in the format: relation['inside'] = 'b',
                        # where inside is the relation and 'b; is the target node
                        relations[attrib] = val
                    else:
                        # properties are saved in the format: properties['filled'] = 'yes'
                        properties[attrib] = val

                # got all relations and properties of the object. form the node now.
                graph.addNode(obj.name, relations, properties)
                card.addNode(graph.getNode(obj.name))
            # end of for
            graph.addCard(card)

        return graph


