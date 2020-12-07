import numpy as np
import cv2
import os

class container:

    def runBash(self, command):
        os.system(command)

    # Initialization function.
    def init(self, input):
        self.name = input

    # Exercice 1
    # Function that cut the video into 1 minute only video.
    def cut(self, input):
        input = self.name
        output = "cuted_video.mp4"
        str = "ffmpeg -i" + input + "-ss 00:03:00 -t 00:04:00 -c copy" + output
        self.runBash(str)
        self.cuted = output

    # Function that export as a mono track
    def mono(self, input):
        input = self.cuted
        output = "mono_video.mp4"
        str = "ffmpeg -i" + input + "-codec:v copy -ac 1 -ab 192k" + output)
        self.runBash(str)
        self.mono = output

    # Function that export the audio in lower bitrate
    def lower_bitrate(self,input):
        input = self.cuted
        output = "lower_bitrate.mp4"
        # Constant Rate Factor (crf) wich lowers the average bit rate,
        #  but retains better quality:
        str = "ffmpeg -i" + input + "-vcodec libx264 -crf 20" + output
        self.runBash(str)
        self.lowrate = output


    # Function that add subtitles
    def subtitles(self,input):
    input = self.cuted
    outuput = "subtitled.mp4"
    self.sub = "BBB.srt"
    str = "ffmpeg -i " + input + " -vf subtitles=" + self.sub + " " + output
    self.runBash(str)
    self.subtitles = output


    # Automatize the creation of MP4 containers



    # Exercice 3
    # Wich broadcasting standard would fit
    # Error in case it doesn't fit
    # More pijadas


    # Exercice 4
    # Testing script wich will generate containers to launch against exercise 3.
