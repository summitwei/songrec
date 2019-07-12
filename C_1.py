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
    hello=0 #Just testing git
    x = samples
    NumofSamp = lambda l: 44100 * len(l)
    sampling_rate = 44100
    Time = np.linspace(0, len(x) / 44100,
                       len(x))  # This starts at 0, ends at what should be the time, len(x), break by frequency
    frequency = np.arange(len(samples) // 2 + 1 / NumofSamp(samples))
    # print (frequency)
    s = np.abs(np.fft.rfft(samples))
    Spectrogram, freqs, t = mlab.specgram(s, NFFT=4096, Fs=sampling_rate,
                                          window=mlab.window_hanning,
                                          noverlap=int(4096 / 2))  # samples to Spectrogram
    np.clip(Spectrogram, a_min=1E-20, a_max=None, out=Spectrogram)
    peaks = f.local_peaks(np.log(Spectrogram), .77, 20)

    return (peaks)
    # print(Spectrogram)