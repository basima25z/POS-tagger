
import os
import sys
import re

def main(argv):
    print(argv)
    trainFile = os.path.basename(sys.argv[1])
    testingFile = os.path.basename(sys.argv[2])

    openTrainFile = open(trainFile, "r")
    contentsTrain = openTrainFile.read()

    openTestFile = open(testingFile, "r")
    contentsTest = openTestFile.read()
    #print(trainFile)
    #print(testingFile)

    print("-----TRAIN------")
    print(contentsTrain)
    #print("------TEST------")
    #print(contentsTest)
    


    #removeBrackets 
    contentsTrain = removeBrackets(contentsTrain)
    print(contentsTrain)

def removeBrackets(trainFile):
    punc = '''[]'''
    for p in trainFile:
        if p in punc:
            trainFile=trainFile.replace(p,"")

    #delete commas and sentance enders etc. 
    delete_list = ["./.",":/:",",/,","''/''","``/``", "--/:"]
    #--/:
    for word in delete_list:
        trainFile=trainFile.replace(word,"")
    return trainFile

def scrape(trainFile):
    



if __name__ == "__main__":
    print('---------------------------------------------------------------------------------------------')
    print('Basima Zafar')
    print('This program learns an N-gram language model from a randum number of text files.')
    print('It then generates a number of sentences based on the N-gram model and the number of sentances inputted through command line.')
    print('---------------------------------------------------------------------------------------------')
    main(sys.argv)