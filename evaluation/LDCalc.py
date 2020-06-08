# install with pip3 install python-Levenshtein
from Levenshtein import distance
from collections import OrderedDict
import itertools
import sys


def reader(txtName):
    """Parse a submission file into a dictionary.

    The dictionary that is generated in this function is analyzed in a seperate
    function to determine the Levenshtein Word Score
    """
    with open(txtName) as txt:
        # Retrieve raw data from file
        dict = OrderedDict()
        keysAndValsOG = txt.readlines()
    keysAndValsOG = [x.lower() for x in keysAndValsOG]
    i = 0
    key = []
    val = []
    ii = 0
    semiPos = 0
    keysAndVals = keysAndValsOG

    while ii < len(keysAndValsOG[0]):
        # Loop converts one line default answer format to seperate lines
        if keysAndValsOG[0][ii] == ';':
            semiPos = ii
        elif keysAndValsOG[0][ii] == ':':
            if (semiPos != 0):
                keysAndVals[0] = keysAndValsOG[0][0:semiPos] + '|' \
                    + keysAndValsOG[0][(semiPos+1):]
        ii += 1
    keysAndVals = keysAndValsOG[0].split("|")

    while i < len(keysAndVals):
        # This loop seperates keys and values into a dictionary containing
        # the submission
        keyVal1st = keysAndVals[i].split(":")
        val1st = keyVal1st[1].split(";")
        keyVal = []
        keyVal.append(keyVal1st[0])
        for value in val1st:
            keyVal.append(value)
        key.append(keyVal[0].rsplit())
        innerValList = []
        j = 0
        for value in keyVal:
            if(j != 0):
                innerValList.append(value.rsplit())
            j += 1
        val.append(innerValList)
        i += 1
    for keyNow, value in zip(key, val):
        # Update dictionary with final listing
        keyNow = str(keyNow)
        dict.update({keyNow: value})
    return dict


def flatten(data):
    """Returns a flattened dictionary"""
    merged = list(itertools.chain(*data))
    return merged


# Method to calculate the distance between the values between two dictionaries
def distanceCalc(realATxtName, aTxtName):
    """Returns a final Levenshtein Word Score"""
    realADict = reader(realATxtName)
    aDict = reader(aTxtName)
    for key in aDict.keys():
        if aDict[key] == [[]]:
            aDict[key] = [[""]]

    frameAnsCombList = []
    for key in realADict:
        # This loop creates the combinations of all the different answers
        # for a given question
        allRealAnswers = flatten(realADict[key])
        allAnswers = flatten(aDict[key])
        for realAnswer in allRealAnswers:
            currFrame = []
            if allAnswers == []:
                # Check to account for case in which submission does not
                # generate an answer for a given question
                currFrame.append([realAnswer, ""])
                frameAnsCombList.append(currFrame)
                continue
            for answer in allAnswers:
                currFrame.append([realAnswer, answer])
            frameAnsCombList.append(currFrame)

    # Evaluating distance across frameAnsCombList into frameAnsScoreList
    frameAnsScoreList = []
    for i in range(len(frameAnsCombList)):
        # This loop evaluates the distance across the ground truth and the
        # submission. This loop generates a list of lists of the format
        # [["groundTruth", score], .....]
        groundTruth = frameAnsCombList[i][0][0]
        minScore = float("inf")
        for dataValue in frameAnsCombList[i]:
            # This loop generates the best Levenshtein distance for a given
            # answer
            lvDist = distance(groundTruth, dataValue[1])
            if lvDist < minScore:
                minScore = lvDist
        frameAnsScoreList.append([groundTruth, minScore])

    finalScore = finalScoreCalculator(frameAnsScoreList)
    return finalScore


def finalScoreCalculator(scoreList):
    """Returns final Levenshtein Word Score

    Iterates through all the scores for the various queries. Final score is
    calculated by averaging the ratio of the score with the word length of
    the ground truth. A given score is capped at 1.
    """
    finalScore = 0.0
    for item in scoreList:
        wordLength = len(item[0])
        currScore = item[1]
        currFinal = float(currScore / wordLength)
        if currFinal > 1:
            # Cap error score at 1
            currFinal = 1
        finalScore += currFinal
    return float(finalScore / len(scoreList))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        avgDist = distanceCalc(sys.argv[1], sys.argv[2])
        print("%f" % (1 - avgDist))
    else:
        print("Incorrect number of arguments. Found {:d}, expected 3"
              .format(len(sys.argv)))
