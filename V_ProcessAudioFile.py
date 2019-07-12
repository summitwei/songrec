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

    :return: sample: array
    Will return the given files for the songs in their respective 441000 sampling rate with a bit depth of 16
    """
    local_song_path = str(Path(r""+mypath))
    samples, fs = librosa.load(local_song_path, sr=44100, mono=True)

    pass