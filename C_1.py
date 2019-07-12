import C_RyanFUNCS as f
import numpy as np
import matplotlib.mlab as mlab
def Samples_to_Peaks(samples):
    '''Takes in a 2D array of numpy music sample and returns peaks
    Input()
    _______________
    SAMPLE

    
    Output()
    _______________
    (frequency , time)'''


    NumofSamp = lambda l:44100*len(l)
    Time = np.linspace(0,len(x),44100*len(x)) #This starts at 0, ends at what should be the time, len(x), break by frequency
    frequency = np.arange(len(samples[x])//2+1/NumofSamp(samples[x]))
    #print (frequency)
    Spectrogram, freqs, t = mlab.specgram(np.abs(np.fft.rfft(samples[x])), Time )#samples to Spectrogram
    peaks =f.local_peaks(np.log(Spectrogram), .77, 20)
    
    return(peaks)
        #print(Spectrogram)