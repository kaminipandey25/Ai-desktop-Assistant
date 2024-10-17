# importing necessary packages
import speech_recognition as sr 
import pyttsx3
import datetime
import os
import wikipedia
import webbrowser
import pygame
import time
import subprocess                  # To open files
from tkinter import *              # For the graphics
import pyjokes                     # For some really bad jokes
from playsound import playsound    # To playsound
import keyboard                    # To get keyboard

name_file = open("Assistant_name", "r")
name_assistant = name_file.read()

# initializing the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# function to speak out the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to wish according to the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!How can I help you?")
    elif hour>=12 and hour<18:
        speak("Good afternoon!How can I help you?")
    else:
        speak("Good evening!How can I help you?")

# function to take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #if user does not speak out anythingor if doesn't recognise
        print("Say that again please...")
        return "None"
    return query

def play_music():
    pygame.init()
    pygame.mixer.init()
    # Load the MP3 file
    pygame.mixer.music.load("C:/Users/srpandey/Music/Kesariya - Brahmastra.mp3")
    # Play the audio
    pygame.mixer.music.play()
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1)
    # Close the mixer and pygame
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

# calling the function
def Process_audio():
  if __name__=="__main__":
    wishMe()
    while True:

        query = takeCommand().lower()  # converting the command to lower case
        # logic for executing tasks

        if "hello" in query or "hi" in query:
            wishMe()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Youtube open now")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Google Chrome open now")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            speak("Stack Overflow open now")

        elif 'play music' in query:
            # music_dir = 'C:\\Users\\srpandey\\Music'
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))
            # song_path = "C:\\Users\\srpandey\\Music\\Kesariya - Brahmastra.mp3"
            play_music()

        elif 'open gmail' in query:
            webbrowser.open_new_tab("mail.google.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'open netflix' in query:
            webbrowser.open_new_tab("netflix.com/browse")
            speak("Netflix open now, Happy watching")

        elif 'open prime video' in query:
            webbrowser.open_new_tab("primevideo.com")
            speak("Amazon Prime Video open now, Happy watching")
            time.sleep(5)

        elif 'open word' in query:
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
            #subprocess.Popen(r'\Microsoft Office Word 2007.lnk)
            speak("Microsoft office Word is opening now")

        elif 'open powerpoint' in query:
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
            speak("Microsoft office PowerPoint is opening now")

        elif 'open excel' in query:
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
            speak("Microsoft office Excel is opening now")

        elif 'open zoom' in query:
            os.startfile(r"C:\Users\srpandey\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom.lnk")
            speak("Zoom is opening now")

        elif 'open notepad' in query:
            os.startfile(r"C:\Users\srpandey\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk")
            speak("Notepad is opening now")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\srpandey\\SymptomDbImpl.java"
            os.startfile(codePath)

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/chennai")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        elif 'cricket' in query:
            news = webbrowser.open_new_tab("cricbuzz.com")
            speak('This is live news from cricbuzz')
            time.sleep(6)

        elif 'corona' in query:
            news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
            speak('Here are the latest covid-19 numbers')
            time.sleep(6)

        elif 'date' in query:
            date()

        elif 'who are you' in query or 'what can you do' in query:
            speak(
                'I am your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Sri Meenakshi Pandey & S Sindu")

        elif 'make a note' in query:
            query = query.replace("make a note", "")
            note(query)

        elif 'quit' in query:
            speak("Bye, have a good day!")
            exit()


def change_name():
    name_info = name.get()

    file = open("Assistant_name", "w")

    file.write(name_info)

    file.close()

    settings_screen.destroy()

    screen.destroy()


def change_name_window():
    global settings_screen
    global name

    settings_screen = Toplevel(screen)
    settings_screen.title("Settings")
    settings_screen.geometry("300x300")
    settings_screen.iconbitmap('app_icon.ico')

    name = StringVar()

    current_label = Label(settings_screen, text="Current name: " + name_assistant)
    current_label.pack()

    enter_label = Label(settings_screen, text="Please enter your Virtual Assistant's name below")
    enter_label.pack(pady=10)

    Name_label = Label(settings_screen, text="Name")
    Name_label.pack(pady=10)

    name_entry = Entry(settings_screen, textvariable=name)
    name_entry.pack()

    change_name_button = Button(settings_screen, text="Ok", width=10, height=1, command=change_name)
    change_name_button.pack(pady=10)


def info():
    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')

    creator_label = Label(info_screen, text="Created by Sri Meenakshi Pandey & S Sindu")
    creator_label.pack()

    Age_label = Label(info_screen, text=" at the age of 22")
    Age_label.pack()

    for_label = Label(info_screen, text="For Final Year Project")
    for_label.pack()


keyboard.add_hotkey("F4", Process_audio)


def wikipedia_screen(text):
    wikipedia_screen = Toplevel(screen)
    wikipedia_screen.title(text)
    wikipedia_screen.iconbitmap('app_icon.ico')

    message = Message(wikipedia_screen, text=text)
    message.pack()


def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("100x250")
    screen.iconbitmap('app_icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="assistant_logo.png")
    microphone_button = Button(image=microphone_photo, command=Process_audio)
    microphone_button.pack(pady=10)

    settings_photo = PhotoImage(file="settings.png")
    settings_button = Button(image=settings_photo, command=change_name_window)
    settings_button.pack(pady=10)

    info_button = Button(text="Info", command=info)
    info_button.pack(pady=10)

    screen.mainloop()


main_screen()