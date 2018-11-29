import random

# Mutate Tree will look something like this
# Layer 0: start <-- start will go to any one option on layer 1
# Layer 1: fiveToFour, fiveToSix, add3rd, add4th, add5th
# Layer 2: invert, add3rd, add4th, and5th
# Layer 3: and so on.
# Layer 4: end

# NO randomness in path selection.  Path is a seeded
# a random sequence can be created to seed.

# pathSelection is a list of ints that determines the path taken
def determinePath(pathSelection):
    path = []

    layerOne = ["fiveToFour", "fiveToFour", "fiveToFour", "fiveToSix", "fiveToSix", "fiveToSix", "addThirdAbove",
                "addThirdAbove", "addThirdAbove", "addFourthAbove", "addFourthAbove", "addFourthAbove", "addFifthAbove",
                "addFifthAbove", "addFifthAbove", "nothing", "nothing"]

    # take the first entry in pathSelection and determine the first step
    path.append(layerOne[pathSelection[0] % len(layerOne)])

    layerTwo = ["addThirdAbove", "addThirdAbove", "addThirdAbove", "addFourthAbove", "addFourthAbove", "addFourthAbove",
                "addFifthAbove", "addFifthAbove", "addFifthAbove", "nothing", "nothing", "nothing", "nothing"]

    # these two delete a note so give a chance to add another note to them
    if path[0] == "fiveToFour" or path[0] == "fiveToSix":
        path.append(layerTwo[pathSelection[1] % len(layerTwo)])

    #
    layerThree = ["invertChord", "invertChord", "nothing", "nothing", "nothing", ]
    path.append(layerThree[pathSelection[2] % len(layerThree)])

    return path

if __name__ == "__main__":
    intlist = \
    [
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
    ]
    print(determinePath(intlist))