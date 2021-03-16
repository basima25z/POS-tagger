

#from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
#import sklearn
import os
import sys
import re

###########################################################
# Basima Zafar
# CMSC: 416 - Natural Language Processing
# March 16th, 2021
# Programming Assignment 3
# This is a utility program that compares the output from tagger.py to the key provided to us
# The purpose of this program is to see how accuracte tagger.py is at classifying a word to a pos
# We can see accuracy and precision with the confusion matrix and the accuracy score
# The input through the command line requires two files: pos-test-with-tags.txt and pos-test-key.txt
# The first file is the result of tagger.py 
# The output file will be utilizing STDOUT, so the > symbol along with a file name is needed in the command line,
# so that the output knows where to be printed
# To run this program in the command line: python3.8 scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-tagging-report.txt
# It is not necceasry to add the 3.8 after python unless you're IDE defaults to the python 2.7 interpretor
############################################################

########################################################
# Function: Main
# Parameters: argv
# The main method takes in two files, the first being the outputfile from tagger.py and the second being the test-key provided
# It opens up the two files and removes the brackets by calling the removeBracket method and sending it the file
# It then splits the two files and uses regex to just obtain the POS from both the test and the key provieded
#########################################################

def main(argv):
    testFile = os.path.basename(sys.argv[1])
    keyFile = os.path.basename(sys.argv[2])

    openTestFile = open(testFile, "r")
    contentsTest = openTestFile.read().lower()

    openKeyFile = open(keyFile, "r")
    contentsKey = openKeyFile.read().lower()
    

    
    contentsTest= removeBrackets(contentsTest)
    contentsKey=removeBrackets(contentsKey)

   

    splitFileKey = contentsKey.split()
  

    splitFileTest = contentsTest.split()
    

    y_pred = splitFileTest #this is used if we want to compare word/pos from test to word/pos in key
    y_act = splitFileKey #word/pos in key

  
    ###########################################################################
    # Below is used to create the Confusion Matrix with just POS
    # Using regex to just obtain the pos by first looking at each index (word/pos) in the testFile
    # If there is a match of the word/pos in the testFile to word/pos in the keyFile, then it appends the second group matched 
    # (which is the pos) to a list called posTest
    # The regex also checks to see if the pos matched contains a '|', if it does, it just appends the first group (ignoring the second pos attached)
    # This algorithm is used first to obtain the pos from the testFile and then again to obtain pos from the keyFile
    #################################################################
    posTest =[]
    pattern = '(.*)/(.*)'
    posReg = '(.*)|(.*)'
    for i in splitFileTest:
        
        match=re.search(pattern,i)
        if match:
            key=match.group(1)
            pos=match.group(2)
            posRegMatch=re.search(posReg,pos)
            if posRegMatch:
                pos= posRegMatch.group(1)
                posTest.append(pos)

    posKey =[]
    pattern = '(.*)/(.*)'
    posReg = '(.*)|(.*)'
    for i in splitFileKey:
        match=re.search(pattern,i)
        if match:
            key=match.group(1)
            pos=match.group(2)
            posRegMatch=re.search(posReg,pos)
            if posRegMatch:
                pos = posRegMatch.group(1)
            posKey.append(pos)


    ##############Confusion Matrix of POS only####################################
    # Using pandas to create a confusion matrix for pos only
    # Assigning the list posKey and posTest list that was created above and set it to Series (1-d Array)
    # Labeling the y_actKey as Actual and y_predTest as Predicted
    # Using crosstab method to create a confusion matrix 
    # Using accuracy_score method to find the accuracy and multipling it by 100 to get a whole number
    ###############################################################################
   

    y_actKey = pd.Series(posKey, name='Actual')
    y_predTest= pd.Series(posTest, name='Predicted')

    df_conf = pd.crosstab(y_actKey, y_predTest)
    pd.set_option("expand_frame_repr", False)

    print("\n%s" % df_conf)
    acc = accuracy_score(y_actKey, y_predTest)
    print("Accuracy: ", acc *100)
    

    #############Confusion Matrix of word/pos#############
    #The assignment wasn't clear on how the confusion matrix should look, whether it was just comparing pos
    # or if it was word/pos, so I made this prior to doing POS only, however, based off the number of columns and rows
    # I just assumed, this isn't what was required, so I left it here just in case and if you'd like to see it just uncomment the print line
    ####################################################
    y_actWord = pd.Series(y_act, name='Actual')
    y_predWord= pd.Series(y_pred, name='Predicted')

    df_conf = pd.crosstab(y_actWord, y_predWord)
    pd.set_option("expand_frame_repr", False)

    #print("\n%s" % df_conf)

    
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



if __name__ == "__main__":
    main(sys.argv)