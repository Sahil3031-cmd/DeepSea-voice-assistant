import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female

def speak(audio):
    print(f"DeepSea: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am DeepSea, Sir your assistant.What can I do for you today?.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except Exception as e:
            print(f"Microphone error: {e}")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand audio. Try again.")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')  # Replace with your email and app password
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

if __name__ == "__main__":
    print("Starting DeepSea Assistant...")
    wishMe()

    query = takeCommand()
    if query != "None":
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry, I couldn’t find anything on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Replace with your actual path
            try:
                os.startfile(codePath)
            except Exception:
                speak("Sorry, I couldn't open VS Code. Please check the path.")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"  # Replace with recipient's email
                if sendEmail(to, content):
                    speak("Email has been sent!")
                else:
                    speak("Failed to send the email.")
            except Exception as e:
                print(e)
                speak("Sorry, I was unable to send the email.")

        else:
            speak("Sorry, I didn't understand that command.")
    
    else:
        speak("No input detected. Please try again.")

    speak("Thankyou. Can you need any other help from Me!")
