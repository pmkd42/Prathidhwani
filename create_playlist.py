# Import everything needed to edit video clips
from moviepy.editor import *

f = open("playlist.txt","r")
# clip list
clips = []
for line in f:
    clips.append(VideoFileClip(line))

# concatenating both the clips
final = concatenate_videoclips(clips)
final.to_videofile("output.mp4", fps=24, remove_temp=False)

