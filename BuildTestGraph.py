from ChordNode import *
from CreateDiatonicGraph import *
from ConversionDicts import *

def buildTestGraph(chordList):

    testList = []

    for num in range(0, 20):

        #chordNode = chordList[random.randint(0, len(chordList) - 1)]

        chordNode = chordList[0]

        print("creating chord number: ", num)

        newNode = mutate(chordNode)

        testList.append(newNode)

    for node in testList:

        print(node.chordBuild)

    return


# function for testing all chords in the chordList for key compliance
def chordQualityCheck(chordList):

    for chord in chordList:
        print("----------------------------------------")
        print("chord number", chordList.index(chord) + 1)
        keyCompliance(chord.chordBuild, chord)

    return


def basicMutateCheck(chordLit):

    count = 0

    for chord in chordList:

        chordBuild = chord.chordBuild

        # check the mutate functions
        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(1)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(2)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(3)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(4)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(5)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(6)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(7)

        chordBuild = extension(chordBuild, chord)
        keyCompliance(chordBuild, chord)
        print(8)

        count += 1
        if count == 1:
            return

    return


chordList = initGraph()
initialConnection(chordList)

basicMutateCheck(chordList)

#buildTestGraph(chordList)



