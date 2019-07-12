import pickle
import V_ProcessMicrophone
import C_1
from e_peaksToDict import peaks_to_fp
from collections import Counter
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
    arr=[]
    for a in recordedFingerprints:
        if a in database:
            arr.append(recordedFingerprints[a[0]])
    counts=Counter(arr)#Make a counter of the number of matches
    print(counts)#Print debugging
    dict={key:value for (key,value) in counts}#Collections counter --> Dictionary
    orderedMatches=sorted(dict, key=dict.get)#Get sorted list of ordered matches
    orderedValues=sorted(list(dict.values()))#Values sorted
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
                userWantsContinue = False
            else:
                answer = "None"

        digSamples=V_ProcessMicrophone.processAudio(10)
        peaks=C_1.Samples_to_Peaks(digSamples)
        fingerprints=peaks_to_fp(peaks)
        matchedSongInfo=matchRecordToSong(fingerprints,database)
        if isinstance(matchedSongInfo,str):
            print(matchedSongInfo)
        else:
            with open(pickleName2, "rb") as file:
                randomLoadedSongDict = pickle.load(file)
            matchedSongInfo=randomLoadedSongDict[matchedSongInfo[0]]
            print(matchedSongInfo)

if __name__ == '__main__':
    main()