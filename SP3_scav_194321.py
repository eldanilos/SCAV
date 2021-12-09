import numpy as np
import cv2
import os

# Function that sends to the terminal the command
def runBash(command):
    os.system(command)

# EXERCISE 5
# Integrate all inside a class.
class SP3:
    def __init__(self, video480, video720, video360x240, video160x120, videoVP8, videoVP9):
        self.video1 = video480
        self.video2 = video720
        self.video3 = video360x240
        self.video4 = video160x120
        self.video5 = videoVP8
        self.video6 = videoVP9

    # EXERCISE 1
    # Convert the resized videos of the past lab into:
    # VP8, VP9, h265 & AV1.
    def formats(self):
        # 1) 480
        input480 = self.video1
        # 1.1) VP8
        str1_1 = "ffmpeg -i "+ input480 + " -c:v libvpx -b:v 1M -c:a libvorbis 480VP8.webm"
        runBash(str1_1)
        # 1.2) VP9
        str1_2 = "ffmpeg -i " + input480 + " -c:v libvpx-vp9 -b:v 2M 480VP9.webm"
        runBash(str1_2)
        # 1.3) h265
        str1_3 = "ffmpeg -i " + input480 + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k 480h265.mp4"
        runBash(str1_3)
        # 1.4) AV1
        str1_4 = "ffmpeg -i " + input480 + " -c:v libaom-av1 -cpu-used 8 -strict experimental 480AV1.mkv"
        runBash(str1_4)

        # 2) 720
        input720 = self.video2
        # 2.1) VP8
        str2_1 = "ffmpeg -i "+ input720 + " -c:v libvpx -b:v 1M -c:a libvorbis 480VP8.webm"
        runBash(str2_1)
        # 2.2) VP9
        str2_2 = "ffmpeg -i " + input720 + " -c:v libvpx-vp9 -b:v 2M 480VP9.webm"
        runBash(str2_2)
        # 2.3) h265
        str2_3 = "ffmpeg -i " + input720 + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k 480h265.mp4"
        runBash(str2_3)
        # 2.4) AV1
        str2_4 = "ffmpeg -i " + input720 + " -c:v libaom-av1 -cpu-used 8 -strict experimental 480AV1.mkv"
        runBash(str2_4)

        # 3) 360x240
        input360x240 = self.video3
        # 3.1) VP8
        str3_1 = "ffmpeg -i "+ input360x240 + " -c:v libvpx -b:v 1M -c:a libvorbis 480VP8.webm"
        runBash(str3_1)
        # 3.2) VP9
        str3_2 = "ffmpeg -i " + input360x240 + " -c:v libvpx-vp9 -b:v 2M 480VP9.webm"
        runBash(str3_2)
        # 3.3) h265
        str3_3 = "ffmpeg -i " + input360x240 + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k 480h265.mp4"
        runBash(str3_3)
        # 3.4) AV1
        str3_4 = "ffmpeg -i " + input360x240 + " -c:v libaom-av1 -cpu-used 8 -strict experimental 480AV1.mkv"
        runBash(str3_4)

        # 4) 160x120
        input160x120 = self.video4
        # 4.1) VP8
        str4_1 = "ffmpeg -i "+ input160x120 + " -c:v libvpx -b:v 1M -c:a libvorbis 480VP8.webm"
        runBash(str4_1)
        # 4.2) VP9
        str4_2 = "ffmpeg -i " + input160x120 + " -c:v libvpx-vp9 -b:v 2M 480VP9.webm"
        runBash(str4_2)
        # 4.3) h265
        str4_3 = "ffmpeg -i " + input160x120 + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k 480h265.mp4"
        runBash(str4_3)
        # 4.4) AV1
        str4_4 = "ffmpeg -i " + input160x120 + " -c:v libaom-av1 -cpu-used 8 -strict experimental 480AV1.mkv"
        runBash(str4_4)

    # EXERCISE 2
    # Export 2 video comparision (VP8 vs VP9)
    def comparision(self):
        inputVP8 = self.video5
        inputVP9 = self.video6
        str22 = "ffmpeg -i " + inputVP8 + " -i " + inputVP9 + \
                " -filter_complex \
                "[0:v]pad=iw*2:ih[int]; \
                [int][1:v]overlay=W/2:0[vid]" \
                -map "[vid]" \
                -c:v libx264 -crf 23 \
                splited.mp4"
        runBash(str22)

    # EXERCISE 3
    # Create a livestreaming of th BBB
    # You should broadcast it into an IP or URL
    def livestreaming(self):
        inputBBB = self.video2
        # EXERCISE 4
        # Choose the IP for the exercise 3
        print("Choose the IP for the livestreaming:")
        IP = input()
        str33 ="ffmpeg -f dshow -i video="+ inputBBB +" -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f mpegts udp://"+ IP
        runBash(str33)

sp3 = SP3("BBB480.mp4", "BBB720.mp4", "BBB360x240.mp4", "BBB160x120.mp4", "480VP8.webm", "480VP9.webm")
sp3.formats()
sp3.comparision()
sp3.livestreaming()
