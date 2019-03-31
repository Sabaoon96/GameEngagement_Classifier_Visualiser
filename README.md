# Group 5C
- Assessment of user engagement through a brain-computer interface: Neurosky Mindwave.
- Our project assesses rates of engagement in players while they play different rated video games.
- The key aspects of this project are the experiment design, data collection, and data analysis.
- As part of the implementation, we've recorded Mindwave data from participants to train the SVM classifier created. Also, data visualisation scripts have been included for a visual understanding of brainwave signals.
- Data has been recorded using the Openvibe Acquisition Server (a tool designed to communicate with various hardware signal acquisition devices). This stores the data in multiple formats including CSV, EDF and GDF, which we then format and analyse.

## Research Question:
Can a single channel Electroencephalography (EEG) differentiate between engagement levels in video games that users love, feel neutral about and hate?

## User Study Details:
To answer our research question, the overarching objectives of our user study would be to: 
- Define a standard metric for 'user engagement' 
- Categorize raw EEG data such that it is obvious as to whether the data came from a highly, average or lowly rated game
- Identify whether differently rated games correlate to the level of engagement of users

#### Justification & Implementation Features to Meet the Objectives:
**Define a standard metric for 'user engagement':**
The NeuroSky MindWave headset is an EEG device that we'll be using to measure user engagement levels of users. The built-in engagement level in combination with a formula to calculate enjoyment will be our metric for 'user engagement'. This is required in order for us to compare and evaluate raw data against a standardised metric for all users in the second part of our implementation.

**Categorize Raw EEG data:**
We will implement our own, and train a Support Vector Machine (SVM) to understand and predict whether the user is playing a badly rated, average rated or highly rated game. By feeding training data into the classifier, it can learn which category of game rating a new vector (new raw EEG data) belongs in. 

Ultimately, if our classifier can correctly predict which game rating category (high, average, low) a new piece of raw EEG data came from, then EEG data itself is sufficient to conclusively differentiate between highly rated/average rated/low rated racing games (and therefore directly addresses/answers our research question).

**Identify Correlation between EEG-based Engagement and User-Perceived Engagement:**
Our second part of the implementation includes a data visualisation tool hosted on Jupyter Notebook. This tool will help visualise the different (if there are any) levels of user engagement across games. Additionally, this tool will allow us to map the 'calculated' engagement from EEG data and user-perceived engagement collected from the user studies.

This part of the implementation aims at answering whether the highest rated game correlates to highest levels of engagement, or the lowest rated games correlate to lowest level of enjoyment, and so on. 

## Implementation: Project File Structure:
- 705-Classifier (Includes the SVM classifier and training datasets)
- 705-Visualisation (Includes visualisation scripts, CSV data and graphical outputs)

- - - -

# Using the Classifier
To use the classifier, the SVM script will require preprocessed data files.
This has been done for you (in /705-Classifier/src/output/), so you can simply go to 'Using the SVM classifier section'

(Optional) If you would like to create your own preprocessed data files, refer to the 'How to use the preprocessing script' section.

## Classifier Setup:

For the SVM script to run, you will need:
- Python v3.7.0
- Python dependencies: numpy, sklearn

For the preprocessing script (not necessarily to use the classifier), you will need:
- Python v3.7.0
- Python dependencies: numpy, scipy, pandas


#### Installing missing dependencies
To check if you have Python installed, open a command line interface and type `python --version`
If not installed, download Python [here](https://www.python.org/downloads/), and follow the installation instructions.

Python uses pip to install packages. In order to download missing dependencies for this project, you will need pip. To check your version of pip, type `pip --version` in your command line.
You can find the installation instructions for pip [here](https://packaging.python.org/tutorials/installing-packages/)

Once pip is installed, use the command `pip install <name_of_missing_dependency>` to install the missing dependencies.
For example, `pip install numpy`.

### Using the SVM Classifier

The SVM classifier uses data created from the preprocessing script (src/output/..). This has already been done for you, so you
will not need to use the preprocessing script if you do not want to.

To make a prediction using this SVM, open your command terminal to the /705-Classifier/src/ directory and type:

`python svm.py <path_to_preprocessed_json_to_predict.json>`

where `<path_to_preprocessed_json_to_predict.json>` is a unique vector. 

An example unique auditory vector has been provided for you, in /705-Classifier/src/uniqueVector/uniqueVector.json)

So for example, running:
`python svm.py A:/Users/Andon/workspace/project-5-c/705-Classifier/src/uniqueVector/uniqueVector.json` should predict the data to be of ['auditory'] category.

#### How to use the preprocessing script:

The preprocessing script is used to set up data to train the SVM. The preprocessing script not necessary to run the SVM,
but normalizes and transforms the data such that it can be used by the SVM. *This has been done for you.*

However, in any case, if you would like to use the script, navigate to the location of (705-Classifier/src/preprocessing_script.py) and use the command:

`python preprocessing_script.py <task> <maxSubjects>`

where task is the category to process, and maxSubjects is the number of subjects you wish the script to process.

Please delete the JSON files of from 4.json to 19.json in the folder location of
* /705-Classifier/raw_data/auditory/0

* /705-Classifier/raw_data/auditory/1


An example: `python preprocessing_script.py auditory 1` will generate 2 transformed files in (705-Classifier/src/output/auditory/), one for each subject. You will need to create the auditory file if it doesn't exist in /705-Classifier/src/output/

The contents of the output directory are the files used to train the SVM.


- - - -

# Viewing Data Visualisation
### Download the repository and open the "EEG Analysis.html" file in any browser to view.

- The visualisation scripts have been written in Python using the Jupyter Notebook.
- The executed scripts yield three files types: .ipynb, .html, and .py files.
- Downloading the repository and opening the EEG Analysis.html file would be the best way to view the visualisations as it includes the dependencies and modules.
- The files with the .py and .ipynb extensions can be used to run the scripts on your own data.
- Running the scripts on your own would require Python3, Jupyter Notebook, and the following modules including plotly, numpy, and pandas. 
- Moreover, running the plotly module would require creating an account at https://plot.ly/ to set credentials.


#### The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.
To run the notebook yourself, you'll need to download and setup:
- Jupyter Notebook on your system
- Install the required modules using conda (plotly, numpy, and pandas)
- Open the .ipynb in Jupyter and run it

