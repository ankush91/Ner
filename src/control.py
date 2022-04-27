#!/usr/bin/env python
import trainPreprocess
import testPreprocess
import trainModel
import testRun
import testAnnotatePreprocess
import sys, getopt

#printing usage for command line options and exit
def printUsage():
    print ('----USAGE----')
    print ('python control.py -pre_train_skip -train_skip -test_skip -n_train <number>')
    sys.exit(2)

#Command Line options for System
def command_line_opts(argv):
    #Try if options are present
    
    list = []
    
    #Iterate through list of arguments (Only these arguments would be matched if size of list is <=6
    if len(argv) <= 6:
        for id,  arg   in enumerate(argv):
            if arg == '-pre_train_skip':
                list.append(arg)
            elif arg == '-train_skip':
                list.append(arg)
            elif arg ==  '-test_skip':
                list.append(arg)
            elif arg == '-train_n' :
                list.append('-train_n')
                if str(argv[id+1]).isdigit():
                    list.append(argv[id+1])
                else:
                    printUsage()
                    sys.exit(2)
    
    #Return List
    return list
    
#Parse Training_set count
def parse_train_count(options):
    if "-train_n" in  options:
        ind = options.index("-train_n")
        number = options[ind+1] 
    else:
        number = -1
    return number
                
def genericLoop(argv):
    
   #*****MAIN CONTROL LOOP FOR THE ML TASK*****
   
   #get Command Line Options
    options = command_line_opts(argv)
    count = parse_train_count(options)
        
    #Train Preprocess - Parse in .col Format
    if "-pre_train_skip" not in options:
        trainPreprocess.parseTimeML("data/TE3-Silver-data/TE3-Silver-data")
    
    if "-train_skip" not in options:
        list = trainPreprocess.inputCol(count);
        #Train Model using Stanford Core-nlp
        trainModel.train(list)
    
    if "-test_skip" not in options:
        #Preprocess Test Model in .txt format
        testPreprocess.preProcess()
        #Preprocess Test in .col format
        testAnnotatePreprocess.parseTimeML("data/te3-platinum-data")
        #run the learnt models on the Test-data
        testRun.test()
    
 
#-----------MAIN FUNCTION---------- 
def main(argv):
    #****CALL to START CONTROL LOOP****
    genericLoop(argv)
    

if __name__ == '__main__':
    main(sys.argv[1:])


    
