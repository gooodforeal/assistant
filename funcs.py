import speech_recognition
import os
import random
import pyaudio
import requests
import lxml
import pyttsx3
from bs4 import BeautifulSoup


'''Creating class object'''
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
voice = pyttsx3.init()

'''Voice'''
def voice_output(text):
    voice.say(text)
    voice.runAndWait()

'''Getting users voice command'''
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source = mic, duration = 0.5)
            audio = sr.listen(source = mic)
            query = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return "[i] Не могу распознать вашу речь!"

'''Greeding'''
def welcome():
    voice_output("Привет пользователь!")
    return "[i] Привет пользователь!"

'''How are you'''
def how_are_you():
    voice_output("У меня все отлично, а как ваши дела?")
    return "[i] У меня все отлично, а как ваши дела?"

'''Appending note to a notebook'''
def create_task():
    print("[i] Скажите, что бы вы хотели добавить в записную книжку...")
    query = listen_command()
    with open("notebook/notebook.txt", "a") as file:
        file.write(f"* {query}\n")
    voice_output(f"Текст '{query}' добавлен в notebook")
    return f"[i] Текст '{query}' добавлен в notebook"

'''Connects music'''
def listen_music():
    files = os.listdir('music')
    random_file = f"G:\\MyProjects\\Python\\voice_assistant\\music\\{random.choice(files)}"
    os.startfile(random_file)
    return "[i] Песня играет..."

'''Switching off the music'''
def off_music():
    os.system('taskkill /f /im Music.UI.exe')
    voice_output("Музыка выключена")
    return "[i] Музыка выключена"

'''Finishing the program'''
def disconnect():
    voice_output("До свидания! Была рада вам помочь")
    return "[i] Завершение работы..."

'''Printing current time'''
def current_time():
    url = "https://time100.ru/"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    time = soup.find("h3", class_ = "display-time").find("span", class_ = "time").text.strip()
    voice_output(f"Текущее время - {time}")
    return f"[i] Текущее время - {time}"