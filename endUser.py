import pickle
import v_processMicrophone
import c_1
import e_peaksToDict
from collections import counter
import numpy as np
def matchRecordToSong(recordedFingerprints,database):
    '''Take fingerprints from recorded sample and find matches in songs

    Paramaters:
    -----------------------------------
    recordedFingerprints: Any iterable with the recorded fingerprints from the 10 sec sample
    database: Dictionary of frequency patterns to song codes
    -----------------------------------
    Returns:
        Most popular song found or "No song found" '''
    arr=np.array(recordedFingerprints)
    counts=Counter(arr[arr in database])
    print(counts)
    dict={key:value for (key,value) in counts}
    orderedMatches=sorted(A, key=A.get)
    orderedValues=list(dict.matches())
    if orderedValues[0]>15:
        return orderedMatches[0]
    else:
        return "No song found"
def main():
    '''
    Allows user to record audio and matches audio to a song in the database
    ----------------------------------------------------------------------
    Parameters: None
    ----------------------------------------------------------------------
    Returns: String with song name or Song not found!!
    '''
    pickleName="database.pickle"
    pickleName2="codeToSong.pickle"
    print('Loading Song Database')
    with open(pickleName,"rb") as file:
        database=pickle.load(file)
    print("Database Loaded")
    userWantsContinue=True




    while (userWantsContinue):
        digSamples=v_processMicrophone.processAudio(10)
        peaks=c_1.Samples_to_Peaks(digSamples)
        fingerprints=peaks_to_fp(peaks)
        matchedSongInfo=matchRecordToSong(fingerprints)
        if isinstance(matchedSongInfo,str):
            print(matchedSongInfo)
        else:
            with open(pickleName2, "rb") as file:
                randomLoadedSongDict = pickle.load(file)
            matchedSongInfo=randomLoadedSongDict[matchedSongInfo[0]]
            print(matchedSongInfo)
        answer="None"
        while answer.lower() not in ["yes","no"]:
            answer=input("Type yes if you want to enter another recording or no if you're done")
            answer=answer.lower()
            if answer =="yes":
                userWantsContinue=True
            elif answer=="no":
                userWantsContinue=False
            else:
                answer="None"
if __name__ == '__main__':
    main()