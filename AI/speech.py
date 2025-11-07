import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""
    try:
        with sr.Microphone() as mic:
            print("listeneing::::")
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'kodi' in cmd:
                cmd = cmd.replace('kodi', '')
                print(f"command after removing kodi :  {cmd}")
    except Exception as e:
        print(f"Error : {e}")
    return cmd

def run():
    cmd = hear()
    print(f"Received command : {cmd}")
    if 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak('playing ' + song)
        pk.playonyt(song)
    else:
        speak(f"Sorry i cannot understand {cmd}")

if __name__ == "__main__":
    run()