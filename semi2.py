import numpy as np
import cv2

# Exercise 1
ffmpeg -i BBB.mp4 -ss 00:00:10 -t 00:10:24 -c copy BBB-10s.mp4


# Exercise 2
# Convert to YUV
ffmpeg -i BBB-10s.mp4 -c:v rawvideo -pix_fmt yuv420p BBBYUV.yuv
# YUV to mp4
ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 25 -i BBBYUV.yuv -c:v libx264 BBByuv.mp4
# Show it together:
ffmpeg -i BBB-10s.mp4 -i BBByuv.mp4 -filter_complex vstack=inputs=2 stackedBBB.mp4


# Exercise 3
#720p:
ffmpeg -i BBB.mp4 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 ~BBB720.mp4
#480p:
ffmpeg -i BBB.mp4 -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 ~BBB480.mp4
#360x240:
ffmpeg -i BBB.mp4 -s 360x240 -c:a copy BBB360x240.mp4
#160x120:
ffmpeg -i BBB.mp4 -s 160x120 -c:a copy BBB160x120.mp4


# Exercise 4
# Mono
ffmpeg -i BBB.mp4 -ac 1 BBBmono.mp4
# Codec h264
ffmpeg -i BBB.mp4 -vcodec h264 BBBcodec.mp4
