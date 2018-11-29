import random

# takes in seed selection of interters
# outputs a selection of chords to be mutated based on seed
def CreateMutatedGraph(selection):
    chordSelectionList = [1, 2, 3, 4, 5, 6, 7]

    chordsToMutate = []
    add = []

    for num in range(0, len(selection)):

        # select chord
        chordsToMutate.append(chordSelectionList[selection[num] % len(chordSelectionList)])

        add = []
        # update chordSelectionList
        for value in chordSelectionList:
            if chordsToMutate[num] != value:
                add.append(value)
        chordSelectionList = chordSelectionList + add
        chordSelectionList.reverse()

    return chordsToMutate

if __name__ == "__main__":
    intlist = \
    [
        random.randint(0, 1000),
        random.randint(0, 1000),
        random.randint(0, 1000),
        random.randint(0, 1000),
        random.randint(0, 1000),
        random.randint(0, 1000),
        random.randint(0, 1000),
    ]
    print(CreateMutatedGraph(intlist))