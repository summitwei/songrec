import pickle
from pathlib import Path

def make_song_id_file(pathName):
    '''
    Creates a dictionary of file IDs and names.

    This function takes in a path to a folder and
    creates a pickle file containing a dictionary
    that maps song ID to song name.

    Parameters:
    -----------
    pathName: Valid string representing a path to a folder
        The folder which the songs will be taken out of (in MP3 format)
    
    Returns:
    --------
    '''
    res = {}
    pathList = Path(pathName).glob('*')
    cnt = 0
    for fileName in pathList:
        fileStr = str(fileName)
        res[cnt] = fileStr
        cnt = cnt+1

    pickle_out = open("codeToSong.pickle", "wb")
    pickle.dump(res, pickle_out)
    pickle_out.close()
    
    return res