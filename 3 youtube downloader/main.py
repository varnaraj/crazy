#import package
import imp
import os
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
my_video.download()
os.rename(my_video.title, "1"+my_video.title)

#check its live or not
print(my_video.is_live)


#download a play list
from pytube import Playlist

i=0
playlist= Playlist("https://www.youtube.com/playlist?list=PLW1yb8L3S1njNqzXgaxUAgAxscBef1RfV")

# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# for video in playlist.video_urls:
#     print(video)
#     my_video1=YouTube(video)
#     my_video1=my_video1.streams.get_lowest_resolution()
#     my_video1.download() #uncomment for download