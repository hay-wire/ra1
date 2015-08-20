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

       #breaking the list in different individual list
       A = imageMatrixArr[0]
       B = imageMatrixArr[1]
       C = imageMatrixArr[2]
       D = np.zeros((w, h)) #[[0 for x in range(h)] for x in range(w)]
       E = np.zeros((w, h)) #[[0 for x in range(h)] for x in range(w)]


       # populate D based on the relation between A and B
       for x in range(0, w) :
           for y in range(0, h) :
               if A[x][y] == B[x][y] :
                   D[x][y] = C[x][y]
               else :
                   D[x][y] = 255 - C[x][y]

               if A[x][y] == C[x][y] :
                   E[x][y] = B[x][y]
               else :
                   E[x][y] = 255 - B[x][y]


       ansImg = Image.fromarray(D)
       ansImg.show()

       optionsImageList = ['1','2','3','4','5','6']
       optionsImageMatrix = []
       # print "D: "
       # print D

       i = 0
       for img in optionsImageList:
           image = Image.open(problem.figures[img].visualFilename)
           imageMatrix = self.imageToPixelMatrix(image)
           # print optionsImageList[i]+": "
           # print imageMatrix

           if (imageMatrix == D).all():
                print "Answer: " + problem.figures[img].name
                return problem.figures[img].name

           if (imageMatrix == E).all():
                print "Answer: " + problem.figures[img].name
                return problem.figures[img].name

           i+=1

           #optionsImageMatrix.append(self.imageToPixelMatrix(image))

       print "No match found\n"
       # r, g, b , a = im.split()
       # variable = Image.merge("RGB", (b,g,r))
       # print(np.asarray(variable))
       # exit()
       return -1