import text2speech
import speech2text
import datetime
import webbrowser
import weather
import os

def action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
       text2speech.text_to_speech("my name is virtual assistant")
       return "my name is virtual assistant"

    elif "hello" in user_data or "hii" in user_data:
       text2speech.text_to_speech("hey sir how can i help you?")
       return "hey sir how can i help you?"

    elif "good morning" in user_data:
       text2speech.text_to_speech("good morning sir/mam")
       return "good morning sir/mam"

    elif "time now" in user_data:
       current_time=datetime.datetime.now()
       Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"Minute"
       text2speech.text_to_speech(Time)
       return Time

    elif "shutdown" in user_data:
       text2speech.text_to_speech("ok sir")
       return "ok sir"
    

    elif "play music" in user_data:
       webbrowser.open("https://gaana.com")
       text2speech.text_to_speech("gaana.com is now ready for you")
       return "gaana.com is now ready for you"

    elif "youtube" in user_data:
       webbrowser.open("https://youtube.com")
       text2speech.text_to_speech("youtube is ready for you")
       return "youtube is ready for you"

    elif "google" in user_data:
       webbrowser.open("https://google.com")
       text2speech.text_to_speech("google is ready for you")
       return "google is ready for you"

    elif "weather" in user_data:
       ans=weather.weather()
       text2speech.text_to_speech(ans)
       return ans
    
    elif 'music from my laptop' in user_data:
        
        url = "C:\\Users\\Manvi\\OneDrive\\Desktop\\sajni.mp3"
        songs = os.startfile(url)
        os.startfile(os.path.join(url, songs[0]))
        text2speech.text_to_speech("songs playing...")
        return "songs playing..." 

    else:
       text2speech.text_to_speech("I am not able to understand")
       return "I am not able to understand"
