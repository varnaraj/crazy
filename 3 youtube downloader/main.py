#import package
import imp
from pytube import YouTube

url="https://www.youtube.com/watch?v=_6nKjFloSDs&ab_channel=AdityaMusic"
my_video=YouTube(url)
print("Video title")
print(my_video.title)
print("Video thumpnail")
print(my_video.thumbnail_url)

print("Video download video")

#set stream resolution
my_video=my_video.streams.get_lowest_resolution()
#my_video.download()

#check its live or not
print(my_video.is_live)

from pytube import Playlist
#download a play list
playlist= Playlist("https://www.youtube.com/playlist?list=PLkTq2HJgz1Ap8WRsoXQhdDkfryxOBpdxv")
for video in plagylist:
    video.streams.get_lowest_resolution().download()