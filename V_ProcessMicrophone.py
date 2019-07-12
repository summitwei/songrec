from microphone import record_audio
import numpy as np


def processAudio(t):
    """
    This function will process a manually-recorded microphone analog sound into digital

    :param t: int
    Duration of time for which to record

    :return: rtn: numpy.array
    Will return the given files for the songs in their respective 441000 sampling rate with a bit depth of 16
    """
    listen_time = t  # seconds
    frames, sample_rate = record_audio(listen_time)

    # Saving the digitized audio data as a numpy array
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    time = np.arange(len(audio_data)) * sample_rate  # corresponding time (sec) for each sample

    return audio_data