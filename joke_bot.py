import requests
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def get_joke(label_text):
    url = "https://icanhazdadjoke.com"
    headers = {'Accept': 'application/json'}
    joke_time = requests.get(url, headers=headers).json().get('joke')
    label_text.set(joke_time)
    print(joke_time)

def start(master) -> None:
    label_text = tb.StringVar()
    label = tb.Label(master, textvariable=label_text, font=("Poppins", 16), bootstyle='default')
    label.pack(padx=5, pady=10)
    btn = tb.Button(master, text="Get Joke!", command=lambda: get_joke(label_text))
    btn.pack(padx=5, pady=10)

if __name__ == '__main__':
    app  = tb.Window(themename='darkly')
    app.title('Joke App')
    app.geometry('1280x900')
    start(app)
    app.mainloop()
    
