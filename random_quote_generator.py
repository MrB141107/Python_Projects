#pip install ttkbootstrap
#pip install requests

import requests
import ttkbootstrap as ttk

#API to fetch quote data
URL = "https://api.quotable.io/random"

#function to fetch a quote from the API above
def fetch_quote():
    response = requests.get(URL) #send a HTTP GET request
    data = response.json() #Parse JSON into a dictionary

    #Extract quote and author data
    quote = data["content"] 
    author = data["author"]
    return quote, author

#Function to update displayed quote and author with another fetched data
def update_quote():
    quote,author = fetch_quote() #call the fetch_quote function to get new data
    quote_label.config(text=quote) #Update the text of the quote label
    author_label.config(text=f"~{author}") #Update the author of the quote label

#Create a GUI window 
root=ttk.Window(themename="pulse")
root.title("Quotes generator")
#Set ttitle and window size
root.geometry("700x250")

#Create a frame within the window
frame = ttk.Frame(root)
frame.pack(padx=30, pady=40)

#Create a label to display the quote
quote_label = ttk.Label(frame, text="", font=("Helvetica", 16), wraplength=650)
quote_label.pack()

#Create a label to display the author
author_label = ttk.Label(frame, text="", font=("Helvetica", 12))
author_label.pack(pady=10)

#Create a button widget that calls the update_quote function
ttk.Button(frame, text="Get Quote", command=update_quote).pack(pady=20)

#Start the main loop to run the GUI
root.mainloop()

