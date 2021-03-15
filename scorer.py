

#from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
#import sklearn
import os
import sys
import re
#os.system('sudo pip install scikit-learn')


def main(argv):
    testFile = os.path.basename(sys.argv[1])
    keyFile = os.path.basename(sys.argv[2])

    openTestFile = open(testFile, "r")
    contentsTest = openTestFile.read().lower()

    openKeyFile = open(keyFile, "r")
    contentsKey = openKeyFile.read().lower()
    #print(trainFile)
    #print(testingFile)

    
    contentsTest= removeBrackets(contentsTest)
    contentsKey=removeBrackets(contentsKey)

    # print("-----TRAIN------")
    # print(contentsTest) # one word in each line
    # print("------TEST------")
    # print(contentsKey) #keys are jumbled, more than one word in a line

    #use regex to split into word plus pos --> or we can just put the whole thing in as a word 
    #and split into y_pred = ["word/pos", "word/pos", "word/pos"]
    #y_act = ["word/pos", "word/pos"]
    # compare the two with confusion matrix

    splitFileKey = contentsKey.split()
    #print(splitFileKey)

    splitFileTest = contentsTest.split()
    #print(splitFileTest)

    y_pred = splitFileTest
    y_act = splitFileKey

    # print("Len y_pred", len(y_pred))
    # print("Len y_act", len(y_act))

    with open('y_pred.txt', 'w') as f:
        for item in y_pred:
            f.write("%s\n" % item)

    with open('y_act.txt', 'w') as f:
        for item in y_act:
            f.write("%s\n" % item)
    
    label =[]
    pattern = '(.*)/(.*)'
    for i in splitFileKey:
        #sublist =[]
        match=re.search(pattern,i)
        if match:
            key=match.group(1)
            pos=match.group(2)
            #listOfLists.append([key,value])
            label.append(pos)

    #print(label)

    s=set(label)
    #print(s)
    labelFin = []
    labelFin = s
    #print(labelFin)
    #{'wdt', "''", 'nn', 'pos', 'dt', 'prp$', 'vb', 'md', 'rb|jj', 'wp', ')', '$', '(', 'nns', '.', ':', 'pdt', 'cc', 'ls', 'vbg|nn', 'vbd', 'rp', 'in', 'jjr|rbr', 'rb', 'nnp', 'vbn', 'jjs', ',', '``', 'rbr', 'uh', 'vbp', 'rbr|jjr', 'jj|in', 'wrb', 'jj', 'sym', 'vbg', 'vbn|jj', 'jjr', '#', 'nnps', 'vbz', 'rbs', 'ex', 'wp$', 'cd', 'fw', 'to', 'prp'}
    

    #print(splitFileKey)
    ####CONFUSION MATRIX OF WORD/POS
    #np.set_printoptions(threshold=sys.maxsize)
    #pd.set_option('display.expand_frame_rpr', False)
    # pd.set_option('display.expand_frame_repr', False)
    # la = np.unique(splitFileKey)
    # a= confusion_matrix(y_act,y_pred,labels=la)
    # print(pd.DataFrame(a, index=la, columns=la))
    # print(accuracy_score(y_act,y_pred))


 ########CONFUSION MATRIX FOR WORD/POS#########
    y_actWord = pd.Series(y_act, name='True')
    y_predWord= pd.Series(y_pred, name='Predicted')

    df_conf = pd.crosstab(y_actWord, y_predWord)
    pd.set_option("expand_frame_repr", False)

    #print("\n%s" % df_conf)

##############################################

    


    #confusion matrix of just pos
    posTest =[]
    pattern = '(.*)/(.*)'
    for i in splitFileTest:
        #sublist =[]
        match=re.search(pattern,i)
        if match:
            key=match.group(1)
            pos=match.group(2)
            #listOfLists.append([key,value])
            posTest.append(pos)

    posKey =[]
    pattern = '(.*)/(.*)'
    for i in splitFileKey:
        #sublist =[]
        match=re.search(pattern,i)
        if match:
            key=match.group(1)
            pos=match.group(2)
            #listOfLists.append([key,value])
            posKey.append(pos)

    # print("----POS TEST----")
    # print(posTest)

    # print("----POS KEY----")
    # print(posKey)



  

    y_actKey = pd.Series(posKey, name='True')
    y_predTest= pd.Series(posTest, name='Predicted')

    df_conf = pd.crosstab(y_actKey, y_predTest)
    pd.set_option("expand_frame_repr", False)

    print("\n%s" % df_conf)
    acc = accuracy_score(y_actKey, y_predTest)
    print("Accuracy: ", acc)
    #print("Accuracy: ", accuracy_score(y_actKey,y_predTest))


    #la = np.unique(label)
    #a= confusion_matrix(y_act,y_pred,labels=la)
    #print(pd.DataFrame(a, index=la, columns=la))

    #print(confusion_matrix(y_act,y_pred),labels=['wdt', "''", 'nn', 'pos', 'dt', 'prp$', 'vb', 'md', 'rb|jj', 'wp', ')', '$', '(', 'nns', '.', ':', 'pdt', 'cc', 'ls', 'vbg|nn', 'vbd', 'rp', 'in', 'jjr|rbr', 'rb', 'nnp', 'vbn', 'jjs', ',', '``', 'rbr', 'uh', 'vbp', 'rbr|jjr', 'jj|in', 'wrb', 'jj', 'sym', 'vbg', 'vbn|jj', 'jjr', '#', 'nnps', 'vbz', 'rbs', 'ex', 'wp$', 'cd', 'fw', 'to', 'prp'])
   # print(accuracy_score(y_act,y_pred))

    


def removeBrackets(trainFile):
    punc = '''[]'''
    for p in trainFile:
        if p in punc:
            trainFile=trainFile.replace(p,"")
            
    return trainFile














if __name__ == "__main__":
    print('---------------------------------------------------------------------------------------------')
    print('Basima Zafar')
    main(sys.argv)