
# Named Entity Recognition: Event and Temporal Expressions
This project is part of the graduate level course-work in Machine Learning (CS 613) carried out at Drexel University in Fall, 2016. The goal of the project is to extract temporal and event expressions from unstructured text documents using Conditional Random Fields.

## Organization:
* 

## Software Environment 
* Our code requires Ubuntu Linux (or any comparable POSIX compliant environment) to run
* The codebase uses `Java 8` and `Python 2.7`, so both of these languages must be installed
* Our code can be run with default parameters from `src` using `python control.py`

## Optional Run-time Parameters
* It also supports some command line flags:-
	* `-pre_train_skip` skips preprocessing of the TimeML training set into COL format. Use if COL files are already present
	* `-train_skip` skips training and creation of the NER model. Since this process can require hours, it is advisable to use a pretrained model for inference
	* `-test_skip` skips the testing process. This can be used if only model training is needed
	* `-train_n <number>` allows to train on a sample of randomly chosen training files, since training on the entire dataset is time consuming

## Hardware Configurations
* It is advisable to use a machine with at least 8 GB of RAM. It will run with less memory, but performance will suffer.	
* Our project (+CoreNLP) is hardcoded to use 4 GB of RAM, but this can be changed. Inability to allocate at least the specified memory 8 GB will cause an OS crash.
* Our project requires approximately 500 MB of disk space, but allowing at least 1 GB is advisable.

## Licensing Information
* Stanford NER licensed under the GNU GPL (v2 or later)
* Stanford CoreNLP licensed under the GNU GPL (v3 or later)

## Full Code Base
	https://www.dropbox.com/s/6uylvx80ece0zfr/Israney%2C%20Ramakrishna%20-%20Temporal%20Expression%20and%20Event%20Extraction.zip?dl=0

#### Notes
* Our last trained model used train data size = 100. 
* To train model with full training set, run: `python control.py`
