import C_RyanFUNCS
import numpy as np
def Samples_to_Peaks(samples):
    '''Takes in a 2D array of numpy music sample and returns peaks
    Input()
    _______________
    SAMPLE

    
    Output()
    _______________
    (frequency , time)'''
    for x in range(len(samples)):
        NumofSamp = lambda l:44100*len(l)
        Time = np.arange(len(x)/)
        frequency = np.arange(len(samples[x])//2+1/NumofSamp(samples[x]))
        #print (frequency)
        Spectrogram = (np.log(np.abs(np.fft.rfft(samples[x]))), )#samples to Spectrogram
        print(Spectrogram)
Samples_to_Peaks([[0,1,2,3,4,5,6],[0,1,2,3,4,5,6],[0,1,2,3,4,5,6]])