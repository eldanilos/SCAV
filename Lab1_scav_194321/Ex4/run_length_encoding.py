import numpy as np
# import cv2

# RLE is a basic form of data compression that converts consecutive identical
# values into a code consisting of the character and the number marking the
# length of the run. The more similar values there are, the more values can
# be compressed.

# Message to codify:
message = 'wwwaaadexxx'


encoded_message = ""
i = 0
# We go through every bit to compute the codification bit by bit.
while (i <= len(message)-1):
    count = 1
    ch = message[i]
    j = i
    while (j < len(message)-1):
        # If the two consecutive values are the same
        if (message[j] == message[j+1]):
            count = count+1
            j = j+1
        else:
            # If the consecutive values stop being equals, pass to the next.
            break
    encoded_message = encoded_message+str(count)+ch
    i = j+1
    print(encoded_message)
# We can verify the codification of the codification result,
# it indicates the number of times that the letter is repeated and the letter
# in that order.
