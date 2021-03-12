
import os
import sys
import re
import csv
import itertools
from collections import Counter

def main(argv):
    print(argv)
    trainFile = os.path.basename(sys.argv[1])
    testingFile = os.path.basename(sys.argv[2])

    openTrainFile = open(trainFile, "r")
    contentsTrain = openTrainFile.read().lower()

    openTestFile = open(testingFile, "r")
    contentsTest = openTestFile.read().lower()
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

    #use regex to get two groups
    #put groups in a dict
    # append to dict as you get more groups --> for loop

    trainDict = {}

    pattern = '(.*)/(.*)'

    splitFileList = trainFile.split()

    # for i in splitFileList:
    #     match = re.search(pattern,i)
    #     if match:
    #         key = match.group(1)
    #         value = match.group(2)
    #         trainDict[key]=value
    # print(trainDict)

    #uses regex to split it into two parts and adds to a list
    listOfLists = []
    justKeys = []
    for i in splitFileList:
        #sublist =[]
        match=re.search(pattern,i)
        if match:
            key=match.group(1)
            value=match.group(2)
            listOfLists.append([key,value])
            justKeys.append(key)
    print(listOfLists)

    

    #creates first frequency table 

    outputFrequency = {}

    for lis in listOfLists:
        outputFrequency.setdefault(tuple(lis), list()).append(1)
    for a,b in outputFrequency.items():
        outputFrequency[a]=sum(b)

    print(outputFrequency)

#########################################################
    keys=list(outputFrequency.keys()) #so the key is imbedded and value is just freq
    val = list(outputFrequency.values())
    #print(keys)
    listOfListFreq1 =[]

    for i,v in keys:
        #print(i) #gets you just the word
        #print(v) #gets you POS
        for va in val:
            listOfListFreq1.append([i,v,va])

    #print(val)
    print(listOfListFreq1)

    

    #print(justKeys)

    #DELETE
    #c = Counter(justKeys)
    # print(c.items())
    #DELETE



    #creating of second frequency table --> just words and freq

    frequency ={}
    frequency= freq(justKeys)
    #print(frequency)









    #DELETE#########
    #second frequncy table with just words and frequency 

    # frequencyWord ={}

    # for elem in justKeys:
    #     frequencyWord.setdefault(tuple(elem), list()).append(1)
    # for k,v in frequencyWord.items():
    #     frequencyWord[k]=sum(v)
    
    # print(frequencyWord)
    #DELETE#############



    

            





    #for key in trainDict:
     #   print(key, '->',trainDict[key])

 

        


    

    


    #Check: used to see if it was parsing correctly
    w = csv.writer(open("output.csv","w"))
    for key,val in trainDict.items():
        w.writerow([key,val])


    #check: used with sublist
    w = csv.writer(open("outputLists.csv","w"))
    for key,val in listOfLists:
        w.writerow([key,val])



    #Now that I have a dictionary, I need to combine words with the same key and value
    #do you divide by the freq of words in the training data when using the testing data?
    #Todo: create a frequency table with the dictionary
    #figure out a way to group the same key and value and count how many time it occurs
    #MAYBE create a dictionary per word, so based off slides:
    # she = {}
    # prp: 58, VBN:2, VBD:0

    #need to figure out a way to automatically make word dict 

    return trainDict

def freq(justKeys):
    wordfreq = [justKeys.count(p) for p in justKeys]
    #print(wordfreq)
    return dict(list(zip(justKeys,wordfreq)))

            









if __name__ == "__main__":
    print('---------------------------------------------------------------------------------------------')
    print('Basima Zafar')
    print('This program learns an N-gram language model from a randum number of text files.')
    print('It then generates a number of sentences based on the N-gram model and the number of sentances inputted through command line.')
    print('---------------------------------------------------------------------------------------------')
    main(sys.argv)