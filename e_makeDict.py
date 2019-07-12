import pickle
import numpy as np
from pathlib import Path
from V_ProcessAudioFile import processSong
from C_1 import Samples_to_Peaks
from e_peaksToDict import peaks_to_fp

def make_dict(pathName):
    '''
    Creates a dictionary of nearest neighbor values.

    This function takes in a path to a folder and
    creates a pickle file containing a dictionary
    of neighbors. It also returns the dictionary.

    Parameters:
    -----------
    pathName: Valid string representing a path to a folder
        The folder which the songs will be taken out of (in MP3 format)
    
    Returns:
    --------
    Dictionary{Tuple[int, int, int], List[Tuple[int, int]]}
        A dictionary containing all of the nearest neighbor pairs.
    '''
    res = {}
    res2 = {}
    pathList = Path(pathName).glob('*.mp3')
    cnt = 0
    for fileName in pathList:
        fileStr = str(fileName)
        digSamp = processSong(fileStr)
        peaks = Samples_to_Peaks(digSamp)
        res = peaks_to_fp(peaks, cnt, res)
        res2[cnt] = fileName.stem
        cnt = cnt+1

    pickle_out = open("database.pickle", "wb")
    pickle.dump(res, pickle_out)
    pickle_out.close()
    pickle_out2 = open("codeToSong.pickle", "wb")
    pickle.dump(res, pickle_out2)
    pickle_out2.close()

    return res, res2