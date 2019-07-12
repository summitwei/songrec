import pickle
import numpy as np
from pathlib import Path
from V_ProcessAudioFile import processSong
from C_1 import Samples_to_Peaks
from e_peaksToDict import peaks_to_fp

def make_dict(pathName):
    '''
    Creates a dictionary of nearest neighbor values.

    This function takes 

    Parameters:
    -----------
    pathName: Valid string representing a path to a folder
        The folder which the songs will be taken out of (in MP3 format)
    
    Returns:
    --------
    Dictionary{Tuple[int, int, int], List[Tuple[int, int]]}
    '''
    res = {}
    pathList = Path(pathName).glob('**/*.asm')
    cnt = 0
    for fileName in pathList:
        fileStr = str(fileName)
        digSamp = processSong(fileStr)
        peaks = Samples_to_Peaks(digSamp)
        res = peaks_to_fp(peaks, cnt, res)

    pickle_out = open("database.pickle", "wb")
    pickle.dump(res, pickle_out)
    pickle_out.close()

    return res