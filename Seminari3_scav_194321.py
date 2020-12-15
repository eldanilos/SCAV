import os

def runBash(command):
  os.system(command)


# Function that cut the video into 1 minute only video.
# That make our program faster because is easier to work with it.
def cut(input):
        output = "cuted_video.mp4"
        str = "ffmpeg -i" + input + "-ss 00:03:00 -t 00:04:00 -c copy" + output
        print("Video cuted succesfully.")

# Function to resize our video fragment.
def resize(input, w, h, output):
    # Send the ffmpeg command made up of the parameters of the function.
    str = "ffmpeg -i " + input + " -vf scale=" + w + ":" + h + " " + output
    runBash(str)
    print("Resize completed succesfully.")

# EXERCICE 1
# Function to convert our resized fragment to the 4 given codecs.

def new_codecs(input,w,h)
    # VP8
    vp8 = "ffmpeg -i" + input + "-c:v libvpx -c:a libvorbis -vf scale=" + w +\
            "x" + h + "vp8.webm"
    runBash(vp8)
    # VP9
    vp9 = "ffmpeg -i" + input + "-c:v libvpx -c:a libvorbis -vf scale=" + w +\
            "x" + h + "vp9.webm"
    runBash(vp9)
    # H265
    h265 = "ffmpeg -i" + input + "-c:v libvpx -c:a libvorbis -vf scale=" + w +\
            "x" + h + "h265.webm"
    runBash(h265)
    # AV1
    av1 = "ffmpeg -i" + input + "-c:v libvpx -c:a libvorbis -vf scale=" + w +\
            "x" + h + "av1.webm"
    runBash(av1)

    # EXERCICE 2
    # Here we create a video as the one of the 4 videos at the same time.

    collage = 'ffmpeg -i' + input1 + '-i' + input2 + '-i' + input3 + '-i' + input4 + \
          '-filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"' \
          '-map "[v]" montage.mp4'
    runBash(collage)

# EXERCICE 3
# Create a live streaming of the BBB Video.
def live_streaming(input)
        # Broadcast into an IP adress locally
        broad = "ffmpeg -i" + input +" -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000"
        runBash(broad)
        # Open this IP inside VLC Media Player
        cast = "ffplay udp://127.0.0.1:23000"
        runBash(cast)

# EXERCICE 4
# Main that enable/activate the online live_streaming
def main():
        # MENÚ that allows to pich wich option (exercice) we want to choose.
        print("Wich exercice do you want to execute?")
        print("1 - Change codecs")
        print("2 - Broadcasting")
        opt = int(input())

        # OPTION 1 - Change codecs.
        if opt == 1:
            # Name of the input.
            print("Wich video do you want to resize?")
            input = str(input())
            input2 = cut(input)                # Cuted video
            # Width of the image.
            print("Choose a width")
            w = str(input())
            # Height of the image.
            print("Choose a height")
            h = str(input())
            # Name of the output.
            print("New name plus the format?")
            output = str(input())
            resize(input2, w, h, output)
            new_codecs(output,w,h)

        # OPTION 2 - Broadcasting.
        if opt == 2:
            # Name of the input.
            print("Wich video do you want to resize?")
            input = str(input())
            input2 = cut(input)             # Cuted video.
            live_streaming(input2)

main()
