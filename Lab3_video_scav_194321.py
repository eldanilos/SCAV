import numpy as np
import cv2
import os
import subprocess

# Exercice 5
# Integrate everything inside a class.
class container:

    def runBash(self, command):
        os.system(command)

    # Exercice 1
    # Function that cut the video into 1 minute only video.
    def cut(self, input):
        output = "cuted_video.mp4"
        str = "ffmpeg -i" + input + "-ss 00:03:00 -t 00:04:00 -c copy" + output
        self.runBash(str)
        self.cuted = output         # Save the output to used as a new input
                                    # in the following functions and work
                                    # with a shorter video.

    # Function that export as a mono track.
    def mono(self):
        input = self.cuted
        output = "mono_video.mp4"
        str = "ffmpeg -i" + input + "-codec:v copy -ac 1 -ab 192k" + output)
        self.runBash(str)
        self.mono = output

    # Function that export the audio in lower bitrate.
    def lower_bitrate(self):
        input = self.cuted
        output = "lower_bitrate.mp4"
        # Constant Rate Factor (crf) wich lowers the average bit rate,
        #  but retains better quality:
        str = "ffmpeg -i" + input + "-vcodec libx264 -crf 20" + output
        self.runBash(str)
        self.lowrate = output


    # Function that add subtitles.
    def subtitles(self):
    input = self.cuted
    outuput = "subtitled.mp4"
    self.sub = "BBB.srt"            # "BBB.srt" contains the subtitles of the video code
                                    # we can download i"-i"t in the internet.
    str = "ffmpeg -i " + input + " -vf subtitles=" + self.sub + " " + output
    self.runBash(str)
    self.subtitles = output

    # Exercice 2
    # Automatize the creation of MP4 containers.
    def add_container(self):
        self.cut()
        self.mono()
        self.lower_bitrate()
        self.subtitles()
        output = "launch.mp4"

        # Send the command to the terminal.
        str = "ffmpeg -i" + self.name + "-i" + self.cuted + "-i" + self.mono \
            + "-i" + self.lowrate + "-i" + self.sub + "-i" + self.subtitles \
            " -ss 00:03:00 -t 00:04:00 -c copy" + outuput
        self.runBash(str)
        self.container = output         # Save it.


    # Exercice 3
    # Wich broadcasting standard would fit.
    # Error in case it doesn't fit.
    def broadcast(self,input)
        # Audio
        error = "ffprobe -v error -select_streams a:0 -show_entries \
                 stream=codec_name -of default=noprint_wrappers=1:nokey=1 " + input
        acodec = subprocess.check_output(error, shell=True)
        acodec = acodec.decode("uft-8")
        acodec = acodec[:len(acodec) - 1]

        # Video
        error = "ffprobe -v error -select_streams v:0 -show_entries \
                 stream=codec_name -of default=noprint_wrappers=1:nokey=1 " + input
        vcodec = subprocess.check_output(error, shell=True)
        vcodec = vcodec.decode("uft-8")
        vcodec = acodec[:len(vcodec) - 1]

        # Compare and see the errors:
        if (vcodec == "mpeg2") or (vcodec == "h264"):
            if acodec == "aac":
                print("Compatible with DVB,ISDB and DTMB.")
            if acodec == "ac3":
                print("Compatible with DVB,ATSC and DTMB.")
            if acodec == "mp3":
                print("Compatible with DVB and DTMB.")
            elif (vcodec == "avs") or (vcodec == "avs+"):
                if ((acodec == "dra") or (acodec == "aac")
                    or (acodec== "ac3") or (acodec == "mp2") or (acodec == "mp3")):
                        print("Compatible with DTMB")
                else:
                    print("ERROR, no compatiblity.")




    # Exercice 4
    # Testing script wich will generate containers to launch against exercise 3.
    def main():
        new = container("BBB.mp4")
        new.add_container()
        new.broadcasting("launch.mp4")

    # main call.
    main()
