
import os
import sys
import re
import csv

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

    trainedDict = {}
    trainedDict = scrape(contentsTrain)

    #pattern = '(.*)/(.*)'




def removeBrackets(trainFile):
    punc = '''[]'''
    for p in trainFile:
        if p in punc:
            trainFile=trainFile.replace(p,"")

    #delete commas and sentance enders etc. 
    # delete_list = ["./.",":/:",",/,","''/''","``/``", "--/:"]
    # #--/:
    # for word in delete_list:
    #     trainFile=trainFile.replace(word,"")
    return trainFile

def scrape(trainFile):

    #
    #use regex to get two groups
    #put groups in a dict
    # append to dict as you get more groups --> for loop

    trainDict = {}

    pattern = '(.*)/(.*)'

    splitFileList = trainFile.split()

    for i in splitFileList:
        match = re.search(pattern,i)
        if match:
            key = match.group(1)
            value = match.group(2)
            trainDict[key]=value
    print(trainDict)


    w = csv.writer(open("output.csv","w"))
    for key,val in trainDict.items():
        w.writerow([key,val])


    # for line in trainFile:
    #     match = re.search(pattern,line)

    #     if match:
    #         key = match.group(1)
    #         value = match.group(2)
    #         trainDict[key]=value

    # print(trainDict)

    return trainDict


            









if __name__ == "__main__":
    print('---------------------------------------------------------------------------------------------')
    print('Basima Zafar')
    print('This program learns an N-gram language model from a randum number of text files.')
    print('It then generates a number of sentences based on the N-gram model and the number of sentances inputted through command line.')
    print('---------------------------------------------------------------------------------------------')
    main(sys.argv)