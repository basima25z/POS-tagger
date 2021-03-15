
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

    #contentsTest=removeBrackets(contentsTest)

    trainedDict = {}
    trainedDict = scrape(contentsTrain, contentsTest)





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

def scrape(trainFile, testFile):

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

    # outputFrequency = {}

    # for lis in listOfLists:
    #     outputFrequency.setdefault(tuple(lis), list()).append(1)
    # for a,b in outputFrequency.items():
    #     outputFrequency[a]=sum(b)

    # print(outputFrequency)

    ##################BOTH OF THESE WORK^ but this one allows you to utilize the count?
    count = Counter(map(tuple,listOfLists))
    print(count)

    # for k,v in count.items():
    #     print(v)
    #     print(k) #k prints out (veto,n)  

    for (word,pos), v in count.items():
        print(word)
        print(word,pos)
    


    #for tuples in count.

#########################################################
    # keys=list(outputFrequency.keys()) #so the key is imbedded and value is just freq
    # val = list(outputFrequency.values())
    # #print(keys)
    # listOfListFreq1 =[]

    # for i,v in keys:
    #     #print(i) #gets you just the word
    #     #print(v) #gets you POS
    #     for va in val:
    #         listOfListFreq1.append([i,v,va])

    # #print(val)
    # print(listOfListFreq1)


    #count ={}
    #count = [dict(Counter(x)) for x in listOfLists]
    #print(count)

    # for lis in listOfLists:
    #     print(lis[0]) #gets words
    #     print(lis[1]) #gets POS


   

    

    #DELETE
    #c = Counter(justKeys)
    # print(c.items())
    #DELETE



    #creating of second frequency table --> just words and freq
##############################################
    frequency ={}
    frequency= freq(justKeys)
    print(frequency)
    ###########################################


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
    testFile=removeBrackets(testFile)

    tags(trainFile,testFile,count,frequency)

    return trainDict




def freq(justKeys):
    wordfreq = [justKeys.count(p) for p in justKeys]
    #print(wordfreq)
    return dict(list(zip(justKeys,wordfreq)))


def tags(trainFile, testFile, count, frequency):
    tagTestWords =[]
    #remove brackets before? --> removed in scrape method

    for line in testFile:
        for word in line.split():
            tagTestWords.append(word)

    trainWords=[]

    for line in trainFile:
        for word in line.split():
            trainWords.append(word)

    with open(sys.argv[3], "w+") as f:
        for word in tagTestWords:
            for (w,pos),v in count.items():
                if word == w:
                    tag=find_pos(word,count, frequency)
                    wordFin = word + "/" + tag
                    f.write(wordFin + "\n")
                else:
                    wordNoPosFound= word + "/NN"
                    f.write(wordNoPosFound + "\n")




def find_pos(word, count,frequency):
    key_max = max()



if __name__ == "__main__":
    print('---------------------------------------------------------------------------------------------')
    print('Basima Zafar')
    print('This program learns an N-gram language model from a randum number of text files.')
    print('It then generates a number of sentences based on the N-gram model and the number of sentances inputted through command line.')
    print('---------------------------------------------------------------------------------------------')
    main(sys.argv)