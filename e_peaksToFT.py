import numpy as np

def peaks_to_fp(peaks, songID):
    '''
    Takes spectrogram peaks and creates dictionary of nearest neighbors.


    Parameters:
    -----------
    peaks: List[Tuple[int, int]]
        Time and frequency index-values of local peaks in spectrogram,
        originally sorted by frequency and then time
    id: int
        The ID of the current song.

    Returns:
    --------
    Dictionary{Tuple[int, int, int], List[Tuple[int, float]]}
        A dictionary mapping values of (f_a, f_b, dt) to all matching song ID's and times.
    '''

    neighborCount = 5

    result = {}

    N = len(peaks)
    for i in range(N):
        for j in range(i+1, min(i+neighborCount+1, N)):
            fi = peaks[i][1]
            fj = peaks[j][1]
            dt = peaks[j][0] - peaks[i][0]
            ti = peaks[i][0]
            key = (fi, fj, dt)
            val = (songID, ti)
            if key not in result:
                result[key] = [val]
            else:
                result[key].append(val)

    return result