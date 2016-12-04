#!/usr/bin/env python
import trainPreprocess
import testPreprocess
import trainModel
def genericLoop():
    '''
    *****MAIN CONTROL LOOP*****
    '''
    
    #Train Preprocess - Parse in .col Format
    #trainPreprocess.parseTimeML("data/te3-platinum")
    #list = trainPreprocess.inputCol();
    
    #Train Model using Stanford Core-nlp
    #trainModel.train(list)
     
    #Preprocess Test Model in .txt format
    testPreprocess.preProcess()
    
    
def main():
    
    
    #****CALL to START CONTROL LOOP****
    genericLoop()
    

if __name__ == '__main__':
    main()
