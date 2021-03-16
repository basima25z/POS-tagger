
import os
import sys
import re
import csv
import itertools
from collections import Counter

################################################################
# Basima Zafar
# CMSC: 416 - Natural Language Processing
# March 16th, 2021
# Programming Assignment 3
# This is a POS tagger program, the purpose of this program is to train your POS tagger with the
# training file and then utilize what your training file has learned on the testing file. 
# The testing file only has words and our goal is to accurately predict the POS based off the highsest probability, this acts as a baseline
# The input of the command line requires two files: tagger.py pos-train.txt pos-test.txt
# The output utilies STDOUT, so in the command line, following the two files, use '>' along with the filename.txt that you would like to output to
# To run this program in the terimnal the command are: python3.8 tagger.py pos-train.txt pos-test.txt > pos-test-with-tags.txt
# It is not necceasry to add the 3.8 after python unless you're IDE defaults to the python 2.7 interpretor
################################################################

################################################################
# Fucntion: Main
# Parameter: command line arguments
# The purpose of the main method is to read two files from the command line
# The program outputs to STDOUT, hence when the '>' is typed in following a filename.txt anything that 
# prints in the program will output directy to that file (within the same directory)
# After the files are read, the method removeBrackets() is called to remove the brackets of the training file
# After the brackets are removed, the method scrape is called where our frequency tables are created
###############################################################




def main(argv):
    trainFile = os.path.basename(sys.argv[1])
    testingFile = os.path.basename(sys.argv[2])

    openTrainFile = open(trainFile, "r")
    contentsTrain = openTrainFile.read().lower()

    openTestFile = open(testingFile, "r")
    contentsTest = openTestFile.read().lower()
   
    


    #removeBrackets 
    contentsTrain = removeBrackets(contentsTrain)
    
    scrape(contentsTrain, contentsTest)



##############################################################
# Function: removeBrackets
# Parameter: file
# The method traverses through each word (or index) in the training file, and if it has a bracket, it
# removes it by using the replace method 
# It then returns the file without brackets
#############################################################


def removeBrackets(trainFile):
    punc = '''[]'''
    for p in trainFile:
        if p in punc:
            trainFile=trainFile.replace(p,"")

    return trainFile

####################################################################
# Fucntion: Scapre
# Parameter: file, file
# The purpose of this function is to first use regex to split the word/pos into two parts and append it
# to a sublist of lists. It also appends just the key(word) to a list called JustKeys
# After the lists of lists is made and the justKeys list is made, I use counter to create the first 
# frequency table which holds the word, pos and the number of occurance
# For example, the listOfLists could look like this: [[veto,nn],[veto,nn],[apart,nn]]
# After using Counter, it would look like this: (veto,nn):2, (apart,nn):1
# The second frequency table is created with justKeys, 
# justKeys could look like this: (veto, veto, apart) and using the frequency method after, it would look
# like: {veto:2, apart:1}
# After both the tables are created, testFile is sent to removeBrackets prior to being sent over to be tagged
#####################################################################


def scrape(trainFile, testFile):

    #use regex to get two groups
 

    pattern = '(.*)/(.*)'
    posReg = '(.*)|(.*)'

    splitFileList = trainFile.split()

   

    #uses regex to split it into two parts and adds to a list
    listOfLists = []
    justKeys = []
    for i in splitFileList: #for each jumpled word (word/pos) or each index 
        match=re.search(pattern,i) #search if the pattern exist 
        if match: #if it does exist
            key=match.group(1) #key is equal to the first match, in this case the word
            value=match.group(2) #value is equal to the second match, in this case the POS
            posRegMatch=re.search(posReg,value) #This check if the value (pos) has a '|' if it does
            if posRegMatch:
                value = posRegMatch.group(1) #only takes the first part of the pos 

            listOfLists.append([key,value]) #appends key,value to the list of lists
            justKeys.append(key) #appends only keys to list
    

    #creation of the first frequency matrix
    count = Counter(map(tuple,listOfLists))
    


    #creating of second frequency table --> just words and freq

    frequency ={}
    frequency= freq(justKeys)
    
    #calls removeBrackets method and sends it testFile, have to do this here because right after it is sent to tag
    testFile=removeBrackets(testFile)

###########################################################################
# Tags is the baseline method where tag is based off of the highest probability of it occuring
# Tags1 correlates to rule 1
# Tags2 correlates to rule 2
# Tags3 correlates to rule 3
# Tags4 correlates to rule 4
# Tags5 correlates to rule 5
# As you can see, as the rules became more ambigous, the accuracy degraded
####################################################################################

    tags(trainFile,testFile,count,frequency) #Accuracy: 83
    #tags1(trainFile,testFile,count,frequency) #Accuracy: 80
    #tags2(trainFile,testFile,count,frequency) #Accuracy: 78
    #tags3(trainFile,testFile,count,frequency) #Accuracy: 79
    #tags4(trainFile,testFile,count,frequency) #Accuracy: 79
    #tags5(trainFile,testFile,count,frequency) #Accuracy:78


###############################################
# Function: Freq
# Parameter: list (justKeys)
# The purpose of this method is to count the frequency of each word occuring and to return it in a dictionary
###############################################


def freq(justKeys):
    wordfreq = [justKeys.count(p) for p in justKeys]
    return dict(list(zip(justKeys,wordfreq)))

####################################################
# Function: find_pos
# Parameter: str, counter, dict
# The purpose of this method is to find the pos that correlates to the word being sent over from the tag method
# The pretense of this is the tag method and that a word in the training file matches a word in the test file
# That word is then sent over as the first parameter 
# It then traverses through the counter which looks like this: (veto,nn):2, (apart,nn):1
# If the word sent in (variable w) is equal to a word in count, then it creates a mini dictionary of 
# words and the pos that match the word 
# For example, if the word that matched was 'no' the mini dictionary would have every option POS of no
# It would look like this: (no,dt):50, (no,rb):2
# It then finds the max frequency occurrance and then since our key is embeded like this: (no,dt)
# I then just sent the first index back which correlates to the pos
# The pos is returned 
# The reason for max frequency instead of probability is because when you do the math, whatever has the 
# highest frequency will have the highest probability
########################################################################


def find_pos(w,count,frequency):

    matchingDict ={} #creation of a mini dictionary
    for(word,pos),v in count.items(): #goes through count 
        if w==word: #if word sent it (that we know matches) matches a word in count
            matchingDict[word,pos]=v #embedds the word,pos as key and the value (frequency) as v
            

    max_key = max(matchingDict, key =matchingDict.get) #baseline, gets you the key with the max frequency
    
    pos = max_key[1] #GETS YOU POS THAT WE NEED TO RETURN, since the key is embedded (looks like (veto,nn)), by doing max_key[1] we only get the POS

    return pos #return POS


###############################################################################
# Function: tags
# Parameters: file, file, counter, dict
# The purpose of this method is to see if any words match in the training file and testing file, if it does
# it calls the find_pos method which returns the pos
# Once the pos is returned it appends it to the word and prints it to STDOUT
###############################################################################
    



def tags(trainFile, testFile, count, frequency):
    tagTestWords =[]
    splitFileTest = testFile.split()

    #The testFile only contains the words, the brackets are removed prior to the file being sent here
    # as an argument, so the method first splits in on whitespace, then it traverses through a for loop
    # and appends each word to a list called tagTestWords
    for i in splitFileTest:
        tagTestWords.append(i)

    #This is a for loop to see if a word in the tagTestWords matches a word in count
    #found acts as a flag, so it initally is set to False
    #If there is a match, it sends the word to find_pos which returns the pos associated with the word
    #It then appends the word to the tag with a '/' in between and prints it to STDOUT and sets found = True
    #When there isn't a match between the train and test, found = False and it appends the word + \nn and print it
    for word in tagTestWords: 
        found=False
        for (w,pos),v in count.items():
            if (word == w): #if a word from the tagTestWords (testFile) matches a word found in count
                tag=find_pos(word,count, frequency) #baseline rule - it sends the matches word, count, and freq dict to find_pos which returns the pos
                wordFin = word + "/" + tag #concatenates the word matches + '/' + pos that is returned from find_pos
                print(wordFin + "\n") #prints to STDOUT 
                
                found=True #found is set to true, so then it will continue in this for loop until found = False
                break

        if found==False: #if found == False, this means that there is no word that matches from the train and test
            wordNoPosFound= word + "/nn" #it concatenates the word + /nn
            print(wordNoPosFound + "\n") #prints to STDOUT

##############################################################################################
# Method: rule1
# Parameters: (str, count, dict)
# tag1 is associated with rule1
# each rule has its own method and tags method
# Rule 1 is if the pos is 'vbd' then set pos = 'vbn' instead and return that as your pos
# The accuracy achieved with rule1 is = 80
# This was found by having each rule run one at a time to print out to the file
# and running that file individually through scocer.py
################################################################################################

def rule1(w,count,frequency):

    matchingDict ={}
    for(word,pos),v in count.items():
        if w==word:
            matchingDict[word,pos]=v
            

    max_key = max(matchingDict, key =matchingDict.get) 
    pos = max_key[1] 

    if(pos=='vbd'):
        pos='vbn'

    return pos

    
############################################################
# Method: tags1
# Parameter: (file,file,count,dict)
# This is similar to tags (baseline), but instead of calling find_pos, it calls rule1 
############################################################

def tags1(trainFile, testFile, count, frequency):
    tagTestWords =[]
    splitFileTest = testFile.split()

    for i in splitFileTest:
        tagTestWords.append(i)

    
    for word in tagTestWords:
        found=False
        for (w,pos),v in count.items():
            if (word == w):
                tag=rule1(word,count, frequency) 
                wordFin = word + "/" + tag
                print(wordFin + "\n")
                
                found=True
                break

        if found==False:
            wordNoPosFound= word + "/nn"
            print(wordNoPosFound + "\n")

##############################################################################################
# Method: rule2
# Parameters: (str, count, dict)
# tag2 is associated with rule2
# Rule 2 is if the pos is 'nnp' then set pos = 'nn' instead and return that as your pos
# The accuracy achieved with rule2 is = 78
# This was found by having each rule run one at a time to print out to the file
# and running that file individually through scocer.py
################################################################################################

def rule2(w,count,frequency):

    matchingDict ={}
    for(word,pos),v in count.items():
        if w==word:
            matchingDict[word,pos]=v
            
    max_key = max(matchingDict, key =matchingDict.get) 
    pos = max_key[1] 

    if(pos=='nnp'):
        pos='nn'

    return pos

    
############################################################
# Method: tags2
# Parameter: (file,file,count,dict)
# This is similar to tags (baseline), but instead of calling find_pos, it calls rule2
############################################################


def tags2(trainFile, testFile, count, frequency):
    tagTestWords =[]
    splitFileTest = testFile.split()

    for i in splitFileTest:
        tagTestWords.append(i)


    
    for word in tagTestWords:
        found=False
        for (w,pos),v in count.items():
            if (word == w):
                tag=rule2(word,count, frequency) 
                wordFin = word + "/" + tag
                print(wordFin + "\n")
                
                found=True
                break

        if found==False:
            wordNoPosFound= word + "/nn"
            print(wordNoPosFound + "\n")

##############################################################################################
# Method: rule3
# Parameters: (str, count, dict)
# tag3 is associated with rule3
# Rule 3 is if the pos is 'jj' then set pos = 'nnp' instead and return that as your pos
# The accuracy achieved with rule3 is = 79
# This was found by having each rule run one at a time to print out to the file
# and running that file individually through scocer.py
################################################################################################

def rule3(w,count,frequency):

    matchingDict ={}
    for(word,pos),v in count.items():
        if w==word:
            
            matchingDict[word,pos]=v
        
    max_key = max(matchingDict, key =matchingDict.get)
    pos = max_key[1] 

    if(pos=='jj'):
        pos='nnp'

    return pos

############################################################
# Method: tags3
# Parameter: (file,file,count,dict)
# This is similar to tags (baseline), but instead of calling find_pos, it calls rule3
############################################################


def tags3(trainFile, testFile, count, frequency):
    tagTestWords =[]
    splitFileTest = testFile.split()

    for i in splitFileTest:
        tagTestWords.append(i)


    for word in tagTestWords:
        found=False
        for (w,pos),v in count.items():
            if (word == w):
                tag=rule3(word,count, frequency) 
                wordFin = word + "/" + tag
                print(wordFin + "\n")
                
                found=True
                break

        if found==False:
            wordNoPosFound= word + "/nn"
            print(wordNoPosFound + "\n")

##############################################################################################
# Method: rule4
# Parameters: (str, count, dict)
# tag4 is associated with rule4
# Rule 4 is if the pos is 'to' then set pos = 'in' instead and return that as your pos
# The accuracy achieved with rule4 is = 79
# This was found by having each rule run one at a time to print out to the file
# and running that file individually through scocer.py
################################################################################################

def rule4(w,count,frequency):

    matchingDict ={}
    for(word,pos),v in count.items():
        if w==word:
      
            matchingDict[word,pos]=v

    max_key = max(matchingDict, key =matchingDict.get)
    pos = max_key[1] 

    if(pos=='to'):
        pos='in'

    return pos

############################################################
# Method: tags4
# Parameter: (file,file,count,dict)
# This is similar to tags (baseline), but instead of calling find_pos, it calls rule4
############################################################

def tags4(trainFile, testFile, count, frequency):
    tagTestWords =[]
    splitFileTest = testFile.split()

    for i in splitFileTest:
        tagTestWords.append(i)


    for word in tagTestWords:
        found=False
        for (w,pos),v in count.items():
            if (word == w):
                tag=rule4(word,count, frequency)
                wordFin = word + "/" + tag
                print(wordFin + "\n")
                
                found=True
                break

        if found==False:
            wordNoPosFound= word + "/nn"
            print(wordNoPosFound + "\n")

##############################################################################################
# Method: rule5
# Parameters: (str, count, dict)
# tag5 is associated with rule5
# Rule 5 is if the pos is 'nns' then set pos = 'rb' instead and return that as your pos
# The accuracy achieved with rule5 is = 78
# This was found by having each rule run one at a time to print out to the file
# and running that file individually through scocer.py
################################################################################################

def rule5(w,count,frequency):

    matchingDict ={}
    for(word,pos),v in count.items():
        if w==word:
            
            matchingDict[word,pos]=v
            
    max_key = max(matchingDict, key =matchingDict.get) 

    pos = max_key[1] 

    if(pos=='nns'):
        pos='rb'

    return pos

############################################################
# Method: tags5
# Parameter: (file,file,count,dict)
# This is similar to tags (baseline), but instead of calling find_pos, it calls rule5
# Overall, as rules were individually added and testesd, the accuracy would degrade
# If the rules worked in conjunction, the accuracy would be consdierably low
############################################################



def tags5(trainFile, testFile, count, frequency):
    tagTestWords =[]
    
    splitFileTest = testFile.split()

    for i in splitFileTest:
        tagTestWords.append(i)

    
    for word in tagTestWords:
        found=False
        for (w,pos),v in count.items():
            if (word == w):
               
                tag=rule5(word,count, frequency) 
                wordFin = word + "/" + tag
                print(wordFin + "\n")
                
                found=True
                break

        if found==False:
            wordNoPosFound= word + "/nn"
            print(wordNoPosFound + "\n")




if __name__ == "__main__":
    #print('---------------------------------------------------------------------------------------------')
    #print('Basima Zafar')
    main(sys.argv)