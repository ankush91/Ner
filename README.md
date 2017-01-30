
# Information-Retrieval--Machine-Learning
Machine Learning Techniques for Temporal Information Extraction and Normalization

-> As mentioned in our paper, our code requires Ubuntu Linux (or any comparable POSIX compliant environment) to run. Our project uses Java 8 and Python 2.7, so both of these languages must be installed.

-> Our code can be run with default parameters using the command "python control.py"

->However, it also supports some command line flags:-

	->'-pre_train_skip' skips preprocessing of the TimeML training set into COL format. Use if COL files are already present
	->'-train_skip skips' training and creation of the model. Since this process can require hours, it is advisable to use this if only testing is desired.
	->'-test_skip' skips the testing process. This can be used if only model generation is desired.
	->'-train_n <number>' allows selection of a limited number of randomly chosen training files, since training on the entire set can require hours.

->It is advisable to use a machine with at least 8 GB of RAM. It will run with less memory, but performance and accuracy will suffer.
	->Our project is hardcoded to use 4 GB of RAM, but this can be changed. Inability to allocate at least the specified memory 8 GB will cause a crash.
	->Our project requires approximately 500 MB of disk space, but allowing at least 1 GB advisable.
	->Control+Z interrupts execution at any point.

#NOTE:
->Our last training set was of size less than 100. Therfore it isn't the fully trained model. If the full model has to be trained first then use 'python control.py'

#Licensing Information For Packages: 
	Stanford NER is licensed under the GNU GPL (v2 or later)
	Stanford CoreNLP licensed under the GNU GPL (v3 or later)

#Full Code Base
	https://www.dropbox.com/s/6uylvx80ece0zfr/Israney%2C%20Ramakrishna%20-%20Temporal%20Expression%20and%20Event%20Extraction.zip?dl=0


