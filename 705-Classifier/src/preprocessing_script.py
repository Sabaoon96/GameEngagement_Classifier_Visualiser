import pandas as pd
import json
import numpy as np
import os
import sys
from scipy import stats
from scipy.interpolate import interp1d

def pSpectrum(vector):
	A = np.fft.fft(vector)
	ps = np.abs(A)**2
	# if len(ps) > 1:
		# splice = int(len(ps)/2)
		# ps = ps[:splice]
	return ps
	
def get_readings(path):
	dataArr = []
	data = pd.read_json(path)
	print(path)
	for item in data['raw_values']:
		dataArr.append(item)
	return dataArr

def binnedPowerSpectra (pspectra,nbin):
	l = len(pspectra)
	array = np.zeros([l,nbin])
	for i,ps in enumerate(pspectra):
		x = np.arange(1,len(ps)+1)
		f = interp1d(x,ps)#/np.sum(ps))
		array[i] = f(np.arange(1, nbin+1))

	index = np.argwhere(array[:,0]==-1)
	array = np.delete(array,index,0)
	return array	
	
def avgPowerSpectrum (arrayOfPowerSpectra, modifierFn):
    return modifierFn(np.mean(arrayOfPowerSpectra, 0))
	
def makeFeatureVector (readings, bins): 
  return avgPowerSpectrum(
    binnedPowerSpectra(pSpectrum(readings), bins)
    , np.log10)	

def main(category, maxSubjectNum):
	full_path = os.path.realpath(__file__)
	path, filename = os.path.split(full_path)
	
	
	maxSubjectNum += 1 #Account for 0 index
	for subject in range(maxSubjectNum):
		data_dir = path[:-3] + "raw_data/" + category + "/" + str(subject) + "/"
		data_files = os.listdir(data_dir)
		pspectra = []
		for jsonFile in data_files:
			path_to_json = data_dir + jsonFile
			pspectra.append(get_readings(path_to_json))
	
		json_data = json.dumps(makeFeatureVector(pspectra,100).tolist())
		
		out_path = path + "/output/" + category + "/" + str(subject) + ".json"

		with open(out_path, 'w') as outfile:
			print("Processed file created at: " + out_path)
			json.dump({'power_spectra': json_data}, outfile)		

main(sys.argv[1], int(sys.argv[2]))