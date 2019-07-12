import pickle
import v_processMicrophone
import c_1
import e_peaksToDict
from collections import counter
import numpy as np
pickleName="database.pickle"
print('Loading Song Database')
with open(pickleName,"rb") as file:
    database=pickle.load(file)
print("Database Loaded")
userWantsContinue=True
def matchRecordToSong(recordedFingerprints):
    '''Take fingerprints from recorded sample and find matches in songs

    Paramaters:
    -----------------------------------
    recordedFingerprints: Any iterable with the recorded fingerprints from the 10 sec sample
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




while (userWantsContinue):
    digSamples=v_processMicrophone.processAudio(10)
    peaks=c_1.Samples_to_Peaks(digSamples)
    fingerprints=peaks_to_Dict(peaks)
    matchedSongInfo=matchRecordToSong(fingerprints)
    print(matchedSongInfo)
    answer="None"
    while answer.lower() not in ["Yes","No"]:
        answer=input("Type yes if you want to enter another recording or no if you're done")
        answer=answer.lower()
        if answer =="yes":
            userWantsContinue=True
        elif answer=="no":
            userWantsContinue=False
        else:
            answer="None"

