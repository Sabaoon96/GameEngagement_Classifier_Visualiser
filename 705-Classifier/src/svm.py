import json
import math
import numpy
import os
import sys
from sklearn import svm

def loadVector(task, subject):
	full_path = os.path.realpath(__file__)
	path, filename = os.path.split(full_path)
	
	json_data = path + "/output/" + task + "/" + str(subject)
	preprocessed_data = json.load(open(json_data, 'rb'))
	V = json.loads(preprocessed_data['power_spectra'])
	return V #Need to replace all NaN with 0
	
def assembleTrainingData(tasks, subject_to_classify):
    X = []
    y = []
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    for task in tasks:
        subjects = []
        data_dir = path + "/output/" + task + "/"
        data_files = os.listdir(data_dir)
        for json_file in data_files:
            if json_file!=subject_to_classify:
                subjects.append(json_file)
        for subject in subjects:
                v = loadVector(task, subject)
                X.append(v)
                y.append(task)
    return numpy.array(X,list), y

def main(novel_vector_path):
	subject_to_classify = novel_vector_path.split("/")[-1] 
	two_tasks = ['BigRigs(low)', 'GTR2(high)']
	three_tasks = ['BigRigs(low)', 'GTR2(high)', 'NFS(avg)']
		
	#print(subjects2)
	#As per the results, specify whether to use data for two or three tasks.
	X1, y1 = assembleTrainingData(two_tasks, subject_to_classify)
	X2, y2 = assembleTrainingData(three_tasks, subject_to_classify)
	
	clf1 = svm.SVC() #Classifier trained on two datasets (high and low rated)
	clf2 = svm.SVC() #Classifier trained on all three datasets
	
	clf1.fit(X1, y1)
	clf2.fit(X2, y2)
	
	
	preprocessed_data = json.load(open(novel_vector_path, 'rb'))
	v = [json.loads(preprocessed_data['power_spectra'])]
	
	print(subject_to_classify, ".Two tasks:",clf1.predict(v), ",Three tasks:",clf2.predict(v))	
	
main(str(sys.argv[1]))