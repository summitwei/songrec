import C_RyanFUNCS as f
import numpy as np
import matlobthing
def Samples_to_Peaks(samples):
    '''Takes in a 2D array of numpy music sample and returns peaks
    Input()
    _______________
    SAMPLE

    
    Output()
    _______________
    (frequency , time)'''
    l=[]
    for x in range(len(samples)):
        NumofSamp = lambda l:44100*len(l)
        Time = np.arange(len(x)/)
        frequency = np.arange(len(samples[x])//2+1/NumofSamp(samples[x]))
        #print (frequency)
        Spectrogram = matlabthing (np.log(np.abs(np.fft.rfft(samples[x]))), Time )#samples to Spectrogram
        fin=f.spec
        l.append(fin)
        #print(Spectrogram)
Samples_to_Peaks([[0,1,2,3,4,5,6],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6]])