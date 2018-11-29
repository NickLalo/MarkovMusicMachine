# Reference chart of intervals, steps, and the steps in between intervals
# INTERVALS:========= 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
# WHOLE OR HALF:=====   w  w  h  w  w  w  h  w  w  h  w  w  w  h
# STEPS UP:==========   2  2  1  2  2  2  1  2  2  1  2  2  2  1
# STEPS FROM ZERO:=== 0  2  4  5  7  9  11 12 14 16 17 19 21 23 24


# converts the step value of (OneNote - KeyNote) to the
# interval value of the oneNote for the chord relative to the KeyNote
# Ex: KeyNote is 60, oneNote is 65.
# oneNote - KeyNote is 5
# Step value of 5 converts to 4 interval value letting you know this is a Maj IV chord.
stepToChordQuality = \
    {
     0: 1,
     2: 2,
     4: 3,
     5: 4,
     7: 5,
     9: 6,
     11: 7
    }

# Chord Quality, Step or Interval conversion
# Convert from Step to Interval or from Interval to Step
# Dict[ChordQuality][current form step or interval][num]
# for Step of Interval input what you have and get the other out

stepIntervalConvert = \
    {
        1:
            {
                "step":
                    {
                        0: 1,
                        2: 2,
                        4: 3,
                        5: 4,
                        7: 5,
                        9: 6,
                        11: 7
                    },

                "interval":
                    {
                        1: 0,
                        2: 2,
                        3: 4,
                        4: 5,
                        5: 7,
                        6: 9,
                        7: 11
                    }
            },
        2:
            {
                "step":
                    {
                        0: 1,
                        2: 2,
                        3: 3,
                        5: 4,
                        7: 5,
                        9: 6,
                        10: 7
                    },
                "interval":
                    {
                        1: 0,
                        2: 2,
                        3: 3,
                        4: 5,
                        5: 7,
                        6: 9,
                        7: 10
                    }
            },
        3:
            {
                "step":
                    {
                        0: 1,
                        1: 2,
                        3: 3,
                        5: 4,
                        7: 5,
                        8: 6,
                        10: 7
                    },
                "interval":
                    {
                        1: 0,
                        2: 1,
                        3: 3,
                        4: 5,
                        5: 7,
                        6: 8,
                        7: 10
                    }
            },
        4:
            {
                "step":
                    {
                        0: 1,
                        2: 2,
                        4: 3,
                        5: 4,
                        7: 5,
                        9: 6,
                        11: 7
                    },

                "interval":
                    {
                        1: 0,
                        2: 2,
                        3: 4,
                        4: 5,
                        5: 7,
                        6: 9,
                        7: 11
                    }
            },
        5:
            {
                "step":
                    {
                        0: 1,
                        2: 2,
                        4: 3,
                        5: 4,
                        7: 5,
                        9: 6,
                        10: 7
                    },

                "interval":
                    {
                        1: 0,
                        2: 2,
                        3: 4,
                        4: 5,
                        5: 7,
                        6: 9,
                        7: 10
                    }
            },
        6:
            {
                "step":
                    {
                        0: 1,
                        2: 2,
                        3: 3,
                        5: 4,
                        7: 5,
                        9: 6,
                        10: 7
                    },
                "interval":
                    {
                        1: 0,
                        2: 2,
                        3: 3,
                        4: 5,
                        5: 7,
                        6: 9,
                        7: 10
                    }
            },
        7:
            {
                "step":
                    {
                        0: 1,
                        1: 2,
                        3: 3,
                        5: 4,
                        6: 5,
                        8: 6,
                        10: 7
                    },

                "interval":
                    {
                        1: 0,
                        2: 1,
                        3: 3,
                        4: 5,
                        5: 6,
                        6: 8,
                        7: 10
                    }
            },
    }


# Should only need the two dictionaries above above
"""
# mode to quality is in the form
# chord quality:
#       steps: interval
modeStepsToInterval = {
    1:  {
        0: 1,
        2: 2,
        4: 3,
        5: 4,
        7: 5,
        9: 6,
        11: 7
        },

    2:  {
        0: 1,
        2: 2,
        3: 3,
        5: 4,
        7: 5,
        9: 6,
        10: 7
        },

    3:  {
        0: 1,
        1: 2,
        3: 3,
        5: 4,
        7: 5,
        8: 6,
        10: 7
        },

    4:  {
        0: 1,
        2: 2,
        4: 3,
        6: 4,
        7: 5,
        9: 6,
        11: 7
        },

    5:  {
        0: 1,
        2: 2,
        4: 3,
        5: 4,
        7: 5,
        9: 6,
        10: 7
        },

    6:  {
        0: 1,
        2: 2,
        3: 3,
        5: 4,
        7: 5,
        8: 6,
        10: 7
        },

    7:  {
        0: 1,
        1: 2,
        3: 3,
        5: 4,
        6: 5,
        8: 6,
        10: 7
        }
                }

# ExtensionDictionary is in the format
# ExtDict = {
#       quality of chord : {
#               highestNote in the chord : {
#                       interval : steps needed to be added to the highestNote } } }

# highestNote must be converted to a multiple of seven if it is higher

extensionDict = {
    # quality
    1: {
        # highest note
        1: {
            # interval : steps
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
        },

        2: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        3: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
        },

        4: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        5: {
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        6: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        7: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
            }
        },

    2: {
        # highest note
        1: {
            # interval : steps
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
        },

        2: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        3: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
        },

        4: {
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        5: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        6: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
            },

        7: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            }
        },

    3: {
        # highest note
        1: {
            # interval : steps
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
        },

        2: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        3: {
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
        },

        4: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        5: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
            },

        6: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        7: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            }
        },

    4: {
        # highest note
        1: {
            # interval : steps
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
        },

        2: {
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        3: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
        },

        4: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
            },

        5: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        6: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        7: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            }
        },

    5: {
        # highest note
        1: {
            # interval : steps
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
        },

        2: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        3: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
        },

        4: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        5: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        6: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        7: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            }
        },

    6: {
        # highest note
        1: {
            # interval : steps
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
        },

        2: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
            },

        3: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
        },

        4: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        5: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        6: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        7: {
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            }
        },

    7: {
        # highest note
        1: {
            # interval : steps
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 6
        },

        2: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        3: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
        },

        4: {
            -1: -2,
            1: 1,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            },

        5: {
            -1: -1,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        6: {
            -1: -2,
            1: 2,
            2: 0,
            3: 4,
            4: 5,
            5: 7
            },

        7: {
            -1: -2,
            1: 2,
            2: 0,
            3: 3,
            4: 5,
            5: 7
            }
        }
                } """