import numpy as np
import cv2
import os

# Function that sends to the terminal the command
def runBash(command):
    os.system(command)

# EXERCISE 5
# Integrate all inside a class.
class Container:
    def __init__(self, video1, video2, video3):
        self.cuted = video1
        self.original = video2
        self.trailer = video3


    # EXERCISE 1
    # Output a video that will show the macroblocks and the motion vectors.
    def motion_vectors(self):
        input = self.cuted
        str = "ffmpeg -flags2 +export_mvs -i " + input + " -vf codecview=mv=pf+bf+bb  BBBmot_vec.mp4"
        runBash(str)

    # EXERCISE 2
    # Create a new BBB container
    # 1- Cut BBB into 1 minute only video.
    # 2- Export BBB(1min) audio as MP3 stereo track.
    # 3- Export BBB(1min) audio in AAC w/ lower bitrate.
    # 4- Package everything in a .mp4 with FFMPEG!!
    def package(self):
        input = self.original
        # 1:
        str = "ffmpeg -i " + input + " -ss 00:00:50 -t 00:01:00 -c copy BBB_minute.mp4"
        runBash(str)
        # 2:
        str2 = "ffmpeg -i BBB_minute.mp4 -q:a 0 -map a BBBstereo.mp3"
        runBash(str2)
        # 3:
        str3 = "ffmpeg -i BBBstereo.mp3 -codec:a aac BBB_ACC.aac"
        runBash(str3)
        # 4:
        str4 = "ffmpeg -i BBB_minute.mp4 -i BBB_ACC.aac -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 BBB_package.mp4"
        runBash(str4)

    # EXERCISE 3
    # Reads the tracks from an MP4 container, and it’s able to say:
    # 1- Which broadcasting standard would fit.
    # 2- ERROR in case it doesn’t fit any.
    # 3- Any more “pijada” you could think (be creative!)
    def read_container(self):
        input = self.original
        str = "ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 " + input + "> codec.txt 2>&1"
        runBash(str)
        f = open("codec.txt", "r")
        print("Video codec:")
        c = f.read()
        print(c)
        print("Broadcasting:")
        if c == "mpeg2\n":
            print("DVB/ISDB/ATSC/DTMB")
        elif c == "h264\n":
            print("DVB/ISDB/ATSC/DTMB")
        elif c == "avs\n":
            print("DTMB")
        else:
            print("Unknown codec")



    # EXERCISE 4
    # Download subtitles, integrate them and output a video
    # with printed subtitles (this means, it will form part of the video track).
    def subtitles(self):
        input = self.trailer
        str = "ffmpeg -i " + input +" -vf subtitles=subtitles.srt BBB_trailer_subtitled.mp4"
        runBash(str)


# Create the container:
s2 = Container("BBB_cuted.mp4", "BBB.mp4", "BBB_trailer.mov")
# 1)
s2.motion_vectors()
# 2)
s2.package()
# 3)
s2.read_container()
# 4)
s2.subtitles()
