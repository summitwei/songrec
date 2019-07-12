import C_Ryan'sFUNCS
import Numpy as np
def Samples_to_Peaks(samples):
'''Takes in an array of numpy music sample and returns peaks
	Input()
	_______________
	SAMPLE
	
	Output()
	_______________
	(frequency , time)'''
	NumofSamp = lambda l:44100*len(l)
	frequency = np.arange(len(sample)//2+1/NumofSamp(sample))
	print (frequency)
	Spectrogram = (samples)#samples to Spectrogram
	
Samples_to_Peaks([[0,1,2,3,4,5,6],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6]])