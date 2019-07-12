import pickle
import V_ProcessMicrophone
import V_ProcessAudioFile
import C_1
from e_peaksToDict import peaks_to_fp
from collections import Counter
import numpy as np
import librosa
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
    if orderedValues[0]>15:#If there are enough matches
        return orderedMatches[0]#return the song
    else:
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

        answer = "None"
        while answer.lower() not in ["yes", "no"]:
            answer = input("Type yes if you want to enter another recording or no if you're done")
            answer = answer.lower()
            if answer == "yes":
                userWantsContinue = True
            elif answer == "no":
                sys.exit(0)
            else:
                answer = "None"
        sampling_rate=44100
        bit_depth=16
        local_song_path=str(Path(r"/Users/varundeb/Documents/BWSI/Some Songs/Hotel California.mp3"))
        samples,fs=librosa.load(local_song_path,sr=sampling_rate, mono=True)
        rtn=samples*[2**bit_depth-1]
        rtn2=rtn[44100:88200]

        peaks = C_1.Samples_to_Peaks(rtn2)
        fingerprints=peaks_to_fp(peaks)
        matchedSongInfo=matchRecordToSong(fingerprints,database)
        if matchedSongInfo=="No song found":
            print(matchedSongInfo)
        else:
            with open(pickleName2, "rb") as file:
                randomLoadedSongDict = pickle.load(file)
            matchedSongInfo=randomLoadedSongDict[matchedSongInfo]
            print(matchedSongInfo)

if __name__ == '__main__':
    main()