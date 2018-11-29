# TODO: --------------------------------------------------------------------------------------
# TODO: create a non key compliant mutating function that takes in chord quality 1,2,3,4,5,6,7
# TODO: and uses that to pick a note from the chord and modify it in such a way that creates
# TODO: a unique change.
# TODO: I, V, minV, I <-- something to create chords like this
# TODO: ---------------------------------------------------------------------------------------


# chord must already be in interval format for this function to work
# interval will already be chosen
def invertChord(chordBuild, interval):

    # remove old bass note from possible new bass note
    oldBassNote = chordBuild[0]
    chordBuild.remove(oldBassNote)

    # can only invert notes that are actually in the chord
    # this allows for any number to be inserted as the interval
    interval = interval % len(chordBuild)

    newBassNote = chordBuild[interval]
    chordBuild.remove(newBassNote)
    print(newBassNote)

    #add old bass note back in
    chordBuild.insert(0, oldBassNote)

    # to keep this function from increasingly moving chords higher and higher
    if newBassNote > 5:
        newBassNote -= 8

    tmp = [newBassNote]

    oneIntervalAway = 0

    # TODO: ----------------------------------------------------------------------
    # TODO: can't help but feel like this is not a very efficient nested for loop
    # TODO: rewrite this code so it is better
    # TODO: ----------------------------------------------------------------------
    # loop to ensure that new bass note is the lowest note
    for note in chordBuild:
        while note < tmp[0]:
            note += 8

        oneIntervalAway = 0

        # for loop to ensure no notes are within 1 interval of each other
        # priority is given to notes already placed in tmp.  so 5,6 would get rid of 6
        for newNote in tmp:

            # don't check note with itself
            if note != newNote:
                if abs(note - newNote) <= 1:
                    oneIntervalAway += 1

        if oneIntervalAway == 0:
            tmp.append(note)

    # reorder tmp list as the above loops might compromise the order of the inversion
    tmp = sorted(tmp)

    return tmp


# fiveToFour is a first line mutation function
# input 1, 3, 5
# outputs 1, 4
def fiveToFour(chordBuild):

    # change 3 interval to 4
    chordBuild[1] += 1

    # remove the 5 interval
    chordBuild.remove(chordBuild[2])

    return chordBuild


# fiveToSix is a first line mutation function
# input 1, 3, 5
# output 1, 3, 6
def fiveToSix(chordBuild):

    chordBuild[2] += 1

    return chordBuild


# add a 3rd above the highest note in the chord
# from most basic chord form this makes a 7th interval
def addThirdAbove(chordBuild):

    note = chordBuild[-1]
    note += 3
    chordBuild.append(note)

    return chordBuild


# add a 4th above the highest note in the chord
# from most basic chord form this makes a 9th interval
def addFourthAbove(chordBuild):

    note = chordBuild[-1]
    note += 4
    chordBuild.append(note)

    return chordBuild


# add a 5th above the highest note in the chord
# from basic chord form this makes a 10th interval
def addFifthAbove(chordBuild):

    note = chordBuild[-1]
    note += 5
    chordBuild.append(note)

    return chordBuild


if __name__ == "__main__":
    print(invertChord([1, 3, 5, 7], 0))
    print(fiveToFour([1,3,5]))
    print(fiveToSix([1,3,5]))
    print(addThirdAbove([1,3,5]))
    print(addFourthAbove([1,3,5]))
    print(addFifthAbove([1,3,5]))
