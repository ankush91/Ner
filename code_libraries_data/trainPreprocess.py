#!/usr/bin/env python
import os
import errno
import glob
import random

'''
This file will act as a python module for parsing Training Data in appropriate .col format in our experiments
'''

#Parse Path of directory into. col format
def parseTimeML(Path):
        os.system('python convertTimeMLToColumns.py '+Path+' -p stanford -o data/TE3-Silver-data/TE3-Silver-data-col')
    
#Select Relevant Columns for input
def inputCol(count):
    #For each line in file
    input = ""
    #Training Directory is here
    allFiles = glob.glob("data/TE3-Silver-data/TE3-Silver-data-col/*.col")
    
    int_count = int(count)
    
    #Select Training Set according to count
    if count > 0:
        randomFiles = random.sample(allFiles,  int_count)
    else:
        randomFiles = allFiles
    
    #Read Files one by one
    for colFile in randomFiles:
        
        colFile_name = nameFile(colFile)
        #do processing for single file
        with open(colFile) as f:
            next(f)
            input = ""
            for line in f:
                #Split columns on tab values
                columns = line.split("\t")
                
                #Split if columns are present
                if len(columns) >= 2:
                    #Add to input word, events and time-exps
                    if columns[0] == "2 1/2":
                        columns[0] = str(2.5)
                    if columns[0] == "204 1/3":
                        columns[0] = str(204.33)
                        
                    input = input + columns[0] + "\t"+parseEntity(columns[3],  columns[11]) +"\n"
                    
            #Write input to a file
            filename = 'stanford-ner-2015-12-09/data/silver-col/inputCol/'+ colFile_name
            
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

    return randomFiles
    
#parse Tag in apporpriate format
def parseEntity(event,  time):
    if event[0]=="e":
        c = "EVENT"
    elif time[0]=="t":
        c = "TIMEX3"
    else:
        c = "OTHERS"
    return c
    
#return name of the file   
def nameFile(file):
    file_name = file.split("/")
    return file_name[3]
