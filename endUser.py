import pickle
import V_ProcessMicrophone
import V_ProcessAudioFile
from C_1 import Samples_to_Peaks
from e_peaksToDict import peaks_to_fp
from collections import Counter
import numpy as np
import librosa
import sys
from pathlib import Path
def matchRecordToSong(recordedFingerprints,database):
    '''Take fingerprints from recorded sample and find matches in songs

    Paramaters:
    -----------------------------------
    recordedFingerprints: Any iterable with the recorded fingerprints from the 10 sec sample
    database: Dictionary of frequency patterns to song codes
    -----------------------------------
    Returns:
        Most popular song found or "No song found" '''
    arr=[]
    for a in recordedFingerprints:
        if a in database:
            for b in database[a]:
                arr.append(b[0])
    print(arr)
    counts=Counter(arr)#Make a counter of the number of matches
    print(counts)#Print debugging
    dicton={key:value for (key,value) in counts.items()}#Collections counter --> Dictionary
    orderedMatches=sorted(dicton, key=dicton.get,reverse=True)#Get sorted list of ordered matches
    print("Ordered Matches"+str(orderedMatches))
    orderedValues=sorted(list(dicton.values()),reverse=True)#Values sorted
    print("Ordered Values" +str(orderedValues))
    if orderedValues[0]>65:#If there are enough matches
        arr=[]
        counts={}
        dicton={}
        orderedValues=[]

        return orderedMatches[0]#return the song
    else:
        arr=[]
        counts={}
        dicton={}
        orderedValues=[]

        return "No song found"#If not enough matches, return no song found
def main():
    '''
    Allows user to record audio and matches audio to a song in the database
    ----------------------------------------------------------------------
    Parameters: None
    ----------------------------------------------------------------------
    Returns: String with song name or Song not found!!
    '''
    pickleName="database.pickle"#Name of big pickle
    pickleName2="codeToSong.pickle"#Name of code to song dict pickle
    print('Loading Song Database')#Inform user
    with open(pickleName,"rb") as file:#load pickle
        database=pickle.load(file)#load pickle
    print("Database Loaded")#inform user
    userWantsContinue=True#Variable for continuing to upload




    while (userWantsContinue): #While the user wants to go again

        userWantsContinue=False
        sampling_rate=44100
        bit_depth=16
        # local_song_path=str(Path(r"/Users/varundeb/Documents/BWSI/Some Songs/Hotel California.mp3"))
        # print("1")
        # samples,fs=librosa.load(local_song_path,sr=sampling_rate, mono=True)
        # print("2")
        # print("Samples"+str(samples))
        # rtn=samples*(2**bit_depth-1)
        # print("3")
        # print("rtn"+str(rtn))
        # rtn2=rtn[441000:882000]
        # print("rtn2"+str(rtn2))
        # print("4")
        digSamples = V_ProcessMicrophone.processAudio(10)
        peaks = Samples_to_Peaks(digSamples)
        # peaks = Samples_to_Peaks(rtn2)
        print("5")
        print("peaks"+str(peaks))
        fingerprints=peaks_to_fp(peaks)
        matchedSongInfo=matchRecordToSong(fingerprints,database)
        digSamples=[]
        peaks=[]
        fingerprints=[]
        if matchedSongInfo=="No song found":
            print(matchedSongInfo)
        else:
            with open(pickleName2, "rb") as file:
                randomLoadedSongDict = pickle.load(file)
            print("Song to Code:" + str(randomLoadedSongDict))
            matchedSongInfo=randomLoadedSongDict[matchedSongInfo]
            print(matchedSongInfo)
        matchedSongInfo=""

if __name__ == '__main__':
    main()