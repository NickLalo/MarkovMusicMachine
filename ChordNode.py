# keyNote is the MIDI note that corresponds with the 1 interval of the key.
# defaults middle C MIDI value 60

# oneNote is the MIDI note that corresponds with the 1 interval of the chord.

# chordBuild is a list of steps needed to build each note in the chord.  Each "note" is the
# number of steps up from the oneNote of the chord.

# buildFormat keeps track of the format for chordBuild.  Steps vs Interval.  Defaults to steps.

# name is the music theory name of the chord
# TODO --------------------------------------------------------------
# TODO: implement a function that will accurately name all chords as
# TODO: RomanNumeral + == + ChordName.  Ex: MajI == C Maj7 b5
# TODO:
# TODO: implement a function to ensure that all chords entered into
# TODO: chordList have a unique ChordName.  I have no clue how I am
# TODO: going to deal with duplicate names.  Maybe don't allow them.
# TODO --------------------------------------------------------------

# modList is a list of all mutations on the chord.  This list will be updated every time the chord is mutated.

# conDict is a dictionary of all other ChordNode this chord is connected to.
# The connections between ChordNodes is what makes up the Markov Decision Chain
# conDict = { chordName :
#               { "destination" : pointer to another ChordNode,
#                 "weight" : 100
#               }
#           }

# compensation is a list that is used when converting steps to intervals or vice versa
# converting between steps and intervals can only within certain values
# Steps are 0 - 11, 12 is an octave above 0
# Interval values are 0 - 7, 8 is an octave above 0
# compensation holds a value that will be added back to chordBuild after conversion
# Ex: chordBulid in Interval form [1, 5, 8] before being converted to step would set
# compensation to [0, 0, 12] and chordBuild to [1, 5, 1].  chordBuild gets converted to
# step being [0, 7, 0].  Then we add compensation to chord build giving us [0, 7, 12] and reset compensation.

# compliance is a list of true of false values that correspond to notes in chordBuild.
# If true then note is in key.  If false then note is not in key.


class ChordNode:

    def __init__(self, keyNote=60, oneNote=60, chordBuild=[0, 4, 7], buildFormat="step", chordName=""):
        self.keyNote = keyNote
        self.oneNote = oneNote
        self.chordBuild = chordBuild
        self.buildFormat = buildFormat
        self.chordName = chordName
        self.modList = []
        self.conDict = {}
        self.compensation = []
        self.compliance = []

    # addCon adds an entry in conDict to another ChordNode
    def addCon(self, destination):

        # if the connection is already in the dictionary ignore
        for key in self.conDict:
            if self.conDict[key]["location"] == destination:
                return

        # init default connection
        innerDict = {"location": destination,
                     "weight": 100}

        # add inner dict to key and then update conDict
        key = {destination.chordName: innerDict}
        self.conDict.update(key)

        # add a connection from destination ChordNode back to this ChordNode
        destination.addCon(self)
