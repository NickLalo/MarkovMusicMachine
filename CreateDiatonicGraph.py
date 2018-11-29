from ChordNode import ChordNode


# initGraph creates a basic set of the seven diatonic chords as ChordNodes
# Maj1, min2, min2, Maj4, Maj5, min6, dim7
# initGraph takes input of KeyNote in MIDI
def initGraph(keyNote = 60):

    # KeyNote and oneNote will be the same for Maj1 chord
    oneNote = keyNote

    # steps from oneNote to build 1, 3, 5 of each chord type
    Maj = [0, 4, 7]
    min = [0, 3, 7]
    dim = [0, 3, 6]

    # create diatonic chords and increment oneNote
    Maj1 = ChordNode(keyNote, oneNote, Maj, "step", "Maj I")
    oneNote += 2  # whole step up to 2 interval

    min2 = ChordNode(keyNote, oneNote, min, "step", "min II")
    oneNote += 2  # whole step up to 3 interval

    min3 = ChordNode(keyNote, oneNote, min, "step", "min III")
    oneNote += 1  # half step up to 4 interval

    Maj4 = ChordNode(keyNote, oneNote, Maj, "step", "Maj IV")
    oneNote += 2  # whole step up to 5 interval

    Maj5 = ChordNode(keyNote, oneNote, Maj, "step", "min V")
    oneNote += 2  # whole step up to 6 interval

    min6 = ChordNode(keyNote, oneNote, min, "step", "min VI")
    oneNote += 2  # whole step up to 7 interval

    dim7 = ChordNode(keyNote, oneNote, Maj, "step", "dim VII")

    # create chordList that contains all Nodes
    chordList = [Maj1, min2, min3, Maj4, Maj5, min6, dim7]

    # connect all chords to each other
    initialConnection(chordList)

    return chordList


# connect add ChordNodes in chordList to each other by adding connections in conDict of all chords
def initialConnection(chordList):

    # nest for loop to connect each chord to every other chord
    for chord in chordList:

        # for range loop because I did't feel like coming up with another variable name for chord
        for num in range(0, len(chordList)):

            # logic so that chords do not connect back to themselves
            if chordList[num] != chord:
                chord.addCon(chordList[num])


# newly added mutated chord is the last in the list.
# Add a connection from every chord to this chord and vice versa
def mutateConnection(chordList):

    # exclude the last chord
    for num in range(0, len(chordList)-1):
        chordList[-1].addCon(chordList[num])


if __name__ == "__main__":

    # MIDI value that corresponds to desired key
    MIDI_KeyNote = 60
    chordList = initGraph(MIDI_KeyNote)

    for chord in chordList:
        print(chord.chordName)
        print(chord.chordBuild)
        print("MIDI start note is: ", chord.oneNote)
        print(chord.conDict)
        for connection in chord.conDict:
            print(chord.conDict[connection])
        print("------------------------")

