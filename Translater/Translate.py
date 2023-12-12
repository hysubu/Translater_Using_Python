import speech_recognition as sr       
from gtts import gTTS
import os
def text_to_speech(text, language, output_file='output.mp3'):
    # Create a gTTS object with the specified language
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech to an MP3 file
    tts.save(output_file)

    # Play the generated speech
    os.system(f'start {output_file}')  # Works on Windows. Modify for other platforms.



def listen(language):
    print(LANGUAGES)   
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        print("audio" , audio)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio , language=language)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not hear your request.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    
    
from googletrans import Translator , LANGUAGES
if __name__ == "__main__":
    spoken_text = listen(language="hi")
    if spoken_text:
        print(f"Text: {spoken_text}")
        translate = Translator()
        transs  = translate.translate(text=spoken_text , dest="or")
        print(transs.text)
        text_to_speech(transs.text , language="en")
