from audio_sampling import analog_to_digital, song_to_digital, turn_off_ticks
import numpy as np
import librosa
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from pathlib import Path


def processSong(mypath):
    """
    This function will process the local audio files.

    :param mypath: path directory
    Example Path below: "/Users/varundeb/Documents/BWSI/Some Songs/Hotel California.mp3"
    **NOTE: the function adds the r prefix to read the files safely. Do not manually add in path name.

    :return: tonpy: numpy.array
    Will return the given files for the songs in their respective 441000 sampling rate with a bit depth of 16
    """
    sampling_rate = 44100
    bit_depth = 16

    local_song_path = str(Path(r""+mypath))
    samples, fs = librosa.load(local_song_path, sr=sampling_rate, mono=True)

    rtn = samples * (2**bit_depth-1) # Convert to a 16-bit file

    # duration = len(samples)/sampling_rate
    #
    # time = np.linspace(0, duration, duration * 44100)  # play sample duration
    # skip = int(len(samples) / (duration * sampling_rate))
    # sampling_signal = samples[::skip]
    #
    # quantizing_levels = 2 ** (bit_depth - 1)
    # quantizing_step = 1. / quantizing_levels
    #
    # quantizing_signal = np.round(sampling_signal / quantizing_step) * quantizing_step
    #
    # # create a new signal as if it was sampled at `sampling_rate` frequency
    # # try changing this and playing the audio again
    # new_l = len(time) / len(quantizing_signal)
    #
    # new_y = []
    # for i in range(len(quantizing_signal)):
    #     new_y += [quantizing_signal[i]] * int(new_l)

    return rtn