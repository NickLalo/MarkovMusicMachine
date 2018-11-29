from ChordNode import *
from ConversionDicts import *

# Reference chart of intervals, steps, and the steps in between intervals
# INTERVALS:========= 1  2  3  4  5  6  7
# WHOLE OR HALF:=====   w  w  h  w  w  w
# STEPS UP:==========   2  2  1  2  2  2
# STEPS FROM ZERO:=== 0  2  4  5  7  9  11


# convert chordBuild to base step range of 0 - 11
# and prepare compensation list for after conversion
def prepForStepToInterval(chordNode):

    chordBuild = chordNode.chordBuild
    tmp = []

    compensate = 0

    # populate compensation list
    for note in chordBuild:

        while note < 0 or note > 11:
            if note < 0:
                note += 12
                compensate -= 8

                # step 0 corresponds with interval 1.  Offset compensate by -1
                if note == 0:
                    compensate -= 1

            if note > 11:
                note -= 12
                compensate += 8

                # step 0 corresponds with interval 1.  Offset compensate by -1
                if note == 0:
                    compensate -= 1

        tmp.append(note)

        chordNode.compensation.append(compensate)
        compensate = 0

    chordNode.chordBuild = tmp

    return


# convert chordBuild to base interval range of 0 - 7
# and prepare compensation list for after conversion
def prepForIntervalToStep(chordNode):

    chordBuild = chordNode.chordBuild
    tmp = []

    compensate = 0

    # populate compensation list
    for note in chordBuild:

        while note < 0 or note > 7:
            if note < 0:
                note += 8
                compensate -= 12

                # interval 0 does not exist
                # intervals start at 1
                if note == 0:
                    note += 1

            if note > 7:
                note -= 8
                compensate += 12

                # interval 0 does not exist
                # intervals start at 1
                if note == 0:
                    note += 1

        tmp.append(note)

        chordNode.compensation.append(compensate)
        compensate = 0

    chordNode.chordBuild = tmp

    return


def StepIntervalConvert(chordNode):

    if chordNode.buildFormat == "step":
        prepForStepToInterval(chordNode)
    elif chordNode.buildFormat == "interval":
        prepForIntervalToStep(chordNode)

    chordBuild = chordNode.chordBuild
    compensation = chordNode.compensation
    tmp = []

    # determine chordQuality 1,2,3,4,5,6,7
    chordQuality = stepToChordQuality[chordNode.oneNote - chordNode.keyNote]

    # convert steps to intervals OR intervals to steps
    for num in range(0, len(chordBuild)):

        newValue = stepIntervalConvert[chordQuality][chordNode.buildFormat][chordBuild[num]]
        newValue += compensation[num]

        tmp.append(newValue)

    # update chordBuild, buildFormat, and compensation
    chordNode.chordBuild = tmp
    if chordNode.buildFormat == "interval":
        chordNode.buildFormat = "step"
    elif chordNode.buildFormat == "step":
        chordNode.buildFormat = "interval"
    chordNode.compensation = []

    return


# check to see if there are any flat of sharp notes in a chord
# save values to compliance list.  Convert all notes to their proper interval names.
# Ex: -1 interval would actually be a 7 interval.
def keyCompliance(chordNode):

    originalChordBuild = chordNode.chordBuild

    prepForStepToInterval(chordNode)

    # determine chordQuality 1,2,3,4,5,6,7
    chordQuality = stepToChordQuality[chordNode.oneNote - chordNode.keyNote]

    for note in chordNode.chordBuild:

        # check to see if notes of chord are in the key
        if note in stepIntervalConvert[chordQuality][chordNode.buildFormat]:

            # convert note to interval and add it to compliance list
            interval = (str(stepIntervalConvert[chordQuality][chordNode.buildFormat][note]))

        # increment note value and flat
        else:

            note += 1

            interval = "b"
            interval += str(stepIntervalConvert[chordQuality][chordNode.buildFormat][note])

        chordNode.compliance.append(interval)

    # reset chordBuild to its value before start of keyCompliance function
    chordNode.chordBuild = originalChordBuild

    return


if __name__ == "__main__":
    chordNode = ChordNode(60, 60, [-1, 4, 7, 12, 14], "step", "MajI == Cmaj7")
    chordNode2 = ChordNode(60, 60, [-1, 3, 5, 8, 10], "interval", "MajI")
    StepIntervalConvert(chordNode)
    StepIntervalConvert(chordNode2)

    print(chordNode.chordBuild)
    print(chordNode2.chordBuild)

    chordNode3 = ChordNode(60, 60, [-2, 4, 7, 12, 14], "step", "MajI == Cmaj7")
    keyCompliance(chordNode3)
    print(chordNode3.compliance)
