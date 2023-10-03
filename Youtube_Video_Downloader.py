# Import Pytube 
import pytube  # pip install pytube

# Import YouTube from PyTube
from pytube import YouTube  

# Getting URL from the User
video_url = input("Enter The Url of Video You Want To Download")

# Getting Video Using PyTube
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first()  

# Downloading Video to Downloading Folder( Remember to Change the Path Here :)
video.download('C:\Users\YourUser\Downloads')

# Print the Info About Dowloading Status
print("Downloding....")   
print("Downloding...")   
print("Downloding....")   
print("Downloding...")   
print("Downloding..")   
print("Downloding.")
print("Done Video Downloaded Successfully")   