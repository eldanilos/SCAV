import numpy as np
import cv2
import os

# Function that sends to the terminal the command
def runBash(command):
    os.system(command)

# EXERCISE 1
# Cut N seconds of the BBB video, user input
def cut_video(input, output):
    # file = open(input,'r')  # Open the file
    # file = BBB.mp4
    # n = seconds             # idk
    str = "ffmpeg -i" + input + "-ss 00:00:50 -t 00:01:02 -c copy" + output
    runBash(str)
    # Verification
    print("Video cuted succesfully.")


# EXERCISE 2
# Convert to YUV
def yuv(input):
    # file = open(input,'r')  # Open the file
    str = "ffmpeg -i" + input + "-c:v rawvideo -pix_fmt yuv420p BBBYUV.yuv"
    runBash(str)
    # YUV to mp4
    str2 = "ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 25 -i BBBYUV.yuv -c:v libx264 BBByuv.mp4"
    runBash(str2)
    # Show it together:
    str3 = "ffmpeg -i" + input + "-i BBByuv.mp4 -filter_complex vstack=inputs=2 stackedBBB.mp4"
    runBash(str3)
    # Verification
    print("Converted to YUV succesfully.")


# EXERCISE 3 - Resize.
def resize(input):
    # file = open(input,'r')  # Open the file
    #720p:
    str = "ffmpeg -i" + input + "-s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 ~BBB720.mp4"
    runBash(str)
    #480p:
    str2 = "ffmpeg -i" + input + "-s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 ~BBB480.mp4"
    runBash(str2)
    #360x240:
    str3 = "ffmpeg -i" + input + "-s 360x240 -c:a copy BBB360x240.mp4"
    runBash(str3)
    #160x120:
    str4 = "ffmpeg -i" + input + "-s 160x120 -c:a copy BBB160x120.mp4"
    runBash(str3)
    # Verification
    print("Video resized succesfully.")

# EXERCISE 4 - Change video into mono and a different audio codec.
def mono_h264(input):
    # file = open(input,'r')  # Open the file
    # Mono
    str = "ffmpeg -i" + input + "-ac 1 BBBmono.mp4"
    runBash(str)
    # Codec h264
    str2 = "ffmpeg -i"+ input + "-vcodec h264 BBBh264.mp4"
    runBash(str2)
    # Verification
    print("Completed succesfully.")

# EXERCISE 5
# Allows the user to choose wich variables of the input you would like to change.
# Always that ask for a name it refers to the input file name plus the format.
def main():

    # MENU that allows to pick wich option (exercise) we want to choose.
    print("Wich exercice do you want to execute? (1 to 4)")
    print("1 - Cut video")
    print("2 - YUV")
    print("3 - Resize")
    print("4 - Mono and H264 codecs")
    opt = int(input())

    if opt == 1:
        # Name of the input.
        print("Wich video do you want to cut?")
        input = str(input())
        # Name of the output.
        print("Name for the data document (.txt)?")
        output = str(input())
        cut_video(input, output)

    if opt == 2:
        # Name of the input.
        print("Wich video do you want to analyze?")
        input = str(input())
        yuv(input)

    if opt == 3:
        # Name of the input.
        print("Wich video do you want to resize?")
        input = str(input())
        resize(input)

    if opt == 4:
        # Name of the input.
        print("Wich video do you want to resize?")
        input = str(input())
        resize(input)
    else:
        print("Invalid selection")
main()
