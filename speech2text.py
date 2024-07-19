import speech_recognition as sr #-sr is for nickname of speech recognition
def speech_to_text():
    r=sr.Recognizer() #- r will help to recognise speech from diff sources
    with sr.Microphone() as source: #-microphone ko as a source use kia gaya hai
        audio=r.listen(source) #-source(microphone) me se audio ko capture krega aur audio object me store krega 
    try:
       voice_data= ""
       voice_data=r.recognize_google(audio)#-captured audio ko google ke sr api me send krega and convert to text aur wo text voice_data me store hoega
       print(voice_data)
       return voice_data
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError:
        print("RequestError")
    




speech_to_text()