import numpy as np
import cv2
import os

# Function that sends to the terminal the command
def runBash(command):
    os.system(command)

# EXERCICE 1
# Function that mark 3 relevant data from the container.
def analyze(input, output):
    file = open(input, 'r')    # Open the file with all the video information.
    data = ("Duration")        # Data we want to analyze
    # Find relevant information related to the duration:
    for line in file:
        if data in line:
            output.write(line)  # Copy the information
            break
    print("Information document created succesfully.")

# EXERCICE 2
# Function to rename.
def rename(input, output):
    src = os.getcwd() + "/" + input     # Actual directory of the file.
    dst = os.getcwd() + "/" + output    # New name and directory of the file.
    # Rename the file:
    os.rename(src, dst)
    print("Source path renamed to destination path successfully.")

# EXERCICE 3
# Function to resize.
def resize(input, w, h, output):
    # Send the ffmpeg command made up of the parameters of the function.
    str = "ffmpeg -i " + input + " -vf scale=" + w + ":" + h + " " + output
    runBash(str)
    print("Resize completed succesfully.")

# EXERCICE 4
# Function that transcode the input into an output with another codec.
def codec_change(name, output, audio, video):
    # Send the ffmpeg comand made up of the parameters of the function.
    str = "ffmpeg -i " + input + " -c:v " + video + " -c:a " + audio + " " + output
    runBash(str)
    print("Transcode completed succesfully.")

# EXERCICE 5
# Allows the user to choose which variables of the input you would like to change.
# Always that ask for a name it refers to the file name plus the format.
def main():

    # MENÚ that allows to pich wich option (exercice) we want to choose.
    print("Wich exercice do you want to execute? (1 to 4)")
    print("1 - Relevant data")
    print("2 - Rename")
    print("3 - Resize")
    print("4 - Transcode")
    opt = int(input())

    # OPTION 1 - Relevant data.
    if opt == 1:
        # analysis(BBB.mp4, "BBB.txt")-> in the exercice one we have to call
        # this function for BBB.mp4 video but we change our funtion to
        # analyze any video that the user needs.
        # Name of the input.
        print("Wich video do you want to analyze?")
        input = str(input())
        # Name of the output.
        print("Name for the data document (.txt)?")
        output = str(input())
        analyze(input, output)

    # OPTION 2 - Rename.
    if opt == 2:
        # Name of the input.
        print("Wich video do you want to rename?")
        input = str(input())
        # Name of the output.
        print("New name plus the format?")
        output = str(input())
        rename(input, output)

    # OPTION 3 - Resize.
    if opt == 3:
        # Name of the input.
        print("Wich video do you want to resize?")
        input = str(input())
        # Width of the image.
        print("Choose a width")
        w = str(input())
        # Height of the image.
        print("Choose a height")
        h = str(input())
        # Name of the output.
        print("New name plus the format?")
        output = str(input())
        resize(input, w, h, output)

    # OPTION 4 - Transcode.
    if opt == 4:
        # Name of the input.
        print("Wich video do you want to apply codec change?")
        input = str(input())
        # Audio codec
        print("Introduce the new audio codec")
        audio = str(input())
        # Video codec
        print("Introduce the new video codec")
        video = str(input())
        # Name of the output.
        print("New name plus the format?")
        output = str(input())
        codec_change(name, output, audio, video)


main()
