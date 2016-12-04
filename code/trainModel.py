#!/usr/bin/env python

import os

'''
This file will act as a python module for Training CRF models using Stanford CRF classifiers and list of training files
'''

#Function to train model using files in directory
def train(list):
    #modify properties file
    modifyProp_train(list)
    
    #START TRAINING THE MODEL WITH PROPERTIES FILE CONTAINING FEATURE SPECIFICATION
    os.chdir("stanford-ner-2015-12-09")
    os.system('java -cp "stanford-ner.jar:lib/*" -mx4g edu.stanford.nlp.ie.crf.CRFClassifier -prop train.prop')
    os.chdir("..")
    
#delete already trained model file
def deleteTrain_model(filename):
    os.remove("stanford-ner-2015-12-09"+'/' +filename)
    
#modify properties file 
def modifyProp_train(list):
    
    #Specify filename
    filename = "stanford-ner-2015-12-09/train.prop"
    #clear contents of file
    os.remove(filename)
    
    #Open default-prop file to read
    with open("default.prop", "r+") as file:
           prop = file.readlines()
           prop2 = prop[0:]
    
    #Merge arguments
    prop1 = "trainFileList = " + extract(list)
    prop = prop1+"".join([str(i) for i in prop2])
    
    #Write everything back
    with open(filename, 'w') as file:
            file.writelines(prop)

#function to extract list
def extract(list):
    tokens = ""
    i = 0
    for element in list:
        token = element.split("/")
        t = "data/te3-platinum-col/inputCol/"+token[2]
        if(i > 0):
            tokens = tokens + "," + t
        else:
            tokens = tokens + t
        i = i+1
    tokens = tokens + "\n"
    return tokens 
    
