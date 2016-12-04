#!/usr/bin/env python
import trainPreprocess
import testPreprocess
import trainModel
import testRun
import testAnnotatePreprocess

def genericLoop():
    '''
    *****MAIN CONTROL LOOP FOR THE ML TASK*****
    '''
    
    #Train Preprocess - Parse in .col Format
    trainPreprocess.parseTimeML("data/TE3-Silver-data/TE3-Silver-data")
    list = trainPreprocess.inputCol();
    
    #Train Model using Stanford Core-nlp
    trainModel.train(list)
     
    #Preprocess Test Model in .txt format
    testPreprocess.preProcess()
    
    #Preprocess Test in .col format
    testAnnotatePreprocess.parseTimeML("data/te3-platinum-data")

    #run the learnt models on the Test-data
    testRun.test()
 
#-----------MAIN FUNCTION---------- 
def main():
    
    
    #****CALL to START CONTROL LOOP****
    genericLoop()
    

if __name__ == '__main__':
    main()
