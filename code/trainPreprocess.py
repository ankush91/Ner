#!/usr/bin/env python
import os
import errno
import glob

'''
This file will act as a python module for parsing Training Data in appropriate .col format in our experiments
'''

#Parse Path of directory into. col format
def parseTimeML(Path):
        os.system('python convertTimeMLToColumns.py '+Path+' -p stanford -o data/te3-platinum-col')
      
#Select Relevant Columns for input
def inputCol():
    #For each line in file
    input = ""
    #Training Directory is here
    allFiles = glob.glob("data/te3-platinum-col/*.col")
    
    #Read Files one by one
    for colFile in allFiles:
        
        colFile_name = nameFile(colFile)

        #do processing for single file
        with open(colFile) as f:
            next(f)
            
            for line in f:
                #Split columns on tab values
                columns = line.split("\t")
                
                #Split if columns are present
                if len(columns) >= 2:
                    
                    #Add to input word, events and time-exps
                    input = input + columns[0] + "\t" +parseEvent(columns[3]) + "\t"  + parseTmx(columns[11]) +"\n"
                    
        #Write input to a file
        filename = "stanford-ner-2015-12-09/data/te3-platinum-col/inputCol/"+colFile_name
        
        #Create Directory Structure (if does not exist) and write input Colfile to it
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                    
        #write output to file            
        with open(filename, "w") as file:
            file.write(input)
            file.write(input)
            file.close()

    return allFiles
    
#parse event in appropriate formate
def parseEvent(word):
        if word[0]=="e":
            return "e"
        else:
            return "O"
    
#parse time in apporpriate format
def parseTmx(word):
    if word[0]=="t":
        return "t"
    else:
        return "O" 
   
#return name of the file   
def nameFile(file):
    file_name = file.split("/")
    return file_name[2]



