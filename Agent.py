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


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
       pass

    def imageToPixelMatrix(self, image):
        w,h = image.size
        imageL = image.convert('L')
        imageMatrix = np.zeros(image.size)
        for x in range(0, w) :
           for y in range(0, h) :
               imageMatrix[x][y] = imageL.getpixel((x, y))
        return imageMatrix

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
        print "Evaluating "+problem.name

        imageList = ['A','B','C']
        imageMatrixArr = []

        for img in imageList :
           image = Image.open(problem.figures[img].visualFilename)
           imageMatrixArr.append(self.imageToPixelMatrix(image))
        (w, h) = image.size

        ansMatrixArr = {}
        for i in range(1, 7):
           print "ansImg is",i
           image = Image.open(problem.figures[str(i)].visualFilename)
           ansMatrixArr[str(i)] = self.imageToPixelMatrix(image)

        #breaking the list in different individual list
        A = imageMatrixArr[0]
        B = imageMatrixArr[1]
        C = imageMatrixArr[2]
        #D = np.zeros((w, h)) #[[0 for x in range(h)] for x in range(w)]
        #E = np.zeros((w, h)) #[[0 for x in range(h)] for x in range(w)]

        print "Triangularizing.."
        trA = self.triangularize(A, w, h)
        trB = self.triangularize(B, w, h)
        trC = self.triangularize(C, w, h)
        trAns = {}
        for i in range(1, 7):
            trAns[str(i)] = self.triangularize(ansMatrixArr[str(i)], w, h)


        sortedTrA = sorted(trA['attribs'], key=trA['attribs'].__getitem__, reverse=True)
        sortedTrB = sorted(trB['attribs'], key=trB['attribs'].__getitem__, reverse=True)
        sortedTrC = sorted(trC['attribs'], key=trC['attribs'].__getitem__, reverse=True)

        #print "trA: ", trA
        print "trA: ",sortedTrA
        # pp.pprint(trA)

        #print "trB ", trB
        print "trB: ",sortedTrB
        # pp.pprint(trB)

        #print "trC: ", trC
        print "trC: ",sortedTrC
        # pp.pprint(trC)
        return -1

        # print "trD: "
        # pp.pprint(trD)
        print "diff (A, B):"
        diffAB = self.triangularDiff(trA, trB)
        print "\ndiff (A, C):"
        diffAC = self.triangularDiff(trA, trC)

        diffHorizAns = {}
        for i in range(1, 7):
            print "\ndiff (C,"+str(i)+")"
            diffHorizAns[str(i)] = self.triangularDiff(trC, trAns[str(i)])


        #self.triangularDiff(trA, trC)


        # populate D based on the relation between A and B
        # for x in range(0, w) :
        #    for y in range(0, h) :
        #        if A[x][y] == B[x][y] :
        #            D[x][y] = C[x][y]
        #        else :
        #            D[x][y] = 255 - C[x][y]
        #
        #        if A[x][y] == C[x][y] :
        #            E[x][y] = B[x][y]
        #        else :
        #            E[x][y] = 255 - B[x][y]
        #
        #
        # ansImg = Image.fromarray(D)
        # ansImg.show()
        #
        #
        # optionsImageList = ['1','2','3','4','5','6']
        # optionsImageMatrix = []
        # # print "D: "
        # # print D
        #
        # i = 0
        # for img in optionsImageList:
        #    image = Image.open(problem.figures[img].visualFilename)
        #    imageMatrix = self.imageToPixelMatrix(image)
        #    # print optionsImageList[i]+": "
        #    # print imageMatrix
        #    #     0    1    2    3
        #    #   ____________________________
        #    #0  | 0    1    1    0    *    *
        #    #1  | 1    1    0    0    *    *
        #    #2  | 0    1    1    0    *    *
        #    #3  | 1    0    0    1    *    *
        #    #   | *    *    *    *    *    *
        #    #   | *    *    *    *    *    *
        #    #   | *    *    *    *    *    *
        #
        #    if (imageMatrix == D).all():
        #         print "Answer: " + problem.figures[img].name
        #         return problem.figures[img].name
        #
        #    if (imageMatrix == E).all():
        #         print "Answer: " + problem.figures[img].name
        #         return problem.figures[img].name
        #
        #    i+=1
        #
        #    #optionsImageMatrix.append(self.imageToPixelMatrix(image))
        #
        # print "No match found\n"
        # # r, g, b , a = im.split()
        # # variable = Image.merge("RGB", (b,g,r))
        # # print(np.asarray(variable))
        # # exit()
        return -1

    def test(self):
        A = np.zeros((2,2))
        A[0][0] = A[0][1] = 1
        rA = self.triangularize(A, 2, 2)
        pp.pprint(rA)

    def triangularize(self, A, w, h):
        attrib = {}
        rA = np.zeros((int(w/2),int(h/2)))
        for x in range(0,int(w/2)):
            for y in range(0,int(h/2)):
                bx = x*2
                by = y*2
                #print "\nx,y = "+str(x)+","+str(y)
                #print "bx,by = "+str(bx)+","+str(by)
                #tmpA = np.zeros(2,2)
                rA[x][y] = 0
                for i in range(0,2):
                    for j in range(0,2):
                        tmp = 1 if (A[bx+i][by+j]==0) else -1
                        placeVal = int(math.pow(3, (i*2 + j*1)))
                        #print "placeval:"+str(i)+","+str(j)+"="+str(placeVal)+"*"+str(tmp)
                        rA[x][y] += placeVal * tmp
                        #print "rA["+str(x)+"]["+str(y)+"] = "+str(rA[x][y])
                shapeId = rA[x][y]

                if str(shapeId) in attrib:
                    attrib[str(shapeId)] += 1
                else:
                    attrib[str(shapeId)] = 1
        #return { 'shapeMatrix': rA, 'attribs': attrib }
        return { 'attribs': attrib }

    def triangularDiff(self, trA, trB):
        diff = {}
        #return diff
        print "diff attrib1 is: ", trA['attribs']
        print "diff attrib2 is: ", trB['attribs']

        # insert all the attribs present in A
        for attrib in trA['attribs']:
            if attrib in trB['attribs']:
                diff[attrib] = trA['attribs'][attrib] - trB['attribs'][attrib]
            else:
                diff[attrib] = trA['attribs'][attrib]

        # insert the attribs present in B but not in A
        for attrib in trB['attribs']:
            if attrib not in diff:
                diff[attrib] = 0 - trB['attribs'][attrib]   # 0 - B because these attribs were absent in A
        print "triangularDiff: ", diff
        return diff

    #def is

    def triangularIntersect(self, trA, trB):
        intersect = {}
        for attrib in trA.attribs:
            if attrib in trB.attribs:
                intersect[attrib] = trA.attribs[attrib] - trB.attribs[attrib]
        return intersect

    def triangularUnion(self, trA, trB):
        union = trA.attribs
        for attrib in trB.attribs:
            if attrib in union:
                union[attrib] += trB.attribs[attrib]
            else:
                union[attrib] = trB.attribs[attrib]
        return union

# agent = Agent()
# agent.test()