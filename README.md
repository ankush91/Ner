
# Named Entity Recognition: Event and Temporal Expressions
* We utilized CRF classifiers from Stanford CoreNLP for the Event and Temporal Span identification tasks of [TempEval-3](https://arxiv.org/pdf/1206.5333v2.pdf). The aim of the TempEval series was to advance research on temporal information processing. This project was conducted as part of graduate level course-work in Machine Learning (CS 613) taught at Drexel University in Fall, 2016.

## Research Findings
* We performed feature engineering as suggested in the Stanford NER system and utilized word-level, char-level and n-gram level features alongside certain positional features.
* We performed an ablation with respect to the size of the training data upto 2.5k train documents. 
	* Precision was stagnant after a mere 50 training samples. 
	* Controlling for these false positives, we found Recall to increase on a logscale with additional documents in steps of constant size (50 in our case). 
* We performed a qualitative assessment of the TempEval-3 task (News domain) and compared it to the SemEval-2016 task which was based on documents from the Clinical domain.
	* Temporal spans were easier to identify in TempEval-3 since News contains more absolute expressions such as `Last May`, `2010`, `eight years` etc. On the other hand, the Clinical domain is much harder for Temporal span identification due to complex relative expressions such as `a day before surgery` etc.
	* On the contrary, the Clinical domain is easier for Event extraction due to the higher density of standard events and operating procedures found in such a corpus.
* Kindly refer to our [paper](./paper/Conference%20Paper.pdf) for further detail.

## Organization
* [src](./src/) contains source code and instructions to install libraries (CoreNLP), datasets and existing models
* [paper](./paper/Conference%20Paper.pdf) is our conference-style paper generated using Latex
* [presentation](./presentation/Temporal%20Expression%20and%20Event%20Extraction%20using%20General%20Conditional%20Random%20Fields.pptx) is our final presentation which summarizes our key experiments

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
