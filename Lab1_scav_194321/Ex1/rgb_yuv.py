import numpy as np
import cv2

print("RGB -> YUV -> RGB")

# Load sample image
rgb = cv2.imread("Lena.png")
cv2.imshow("Original",rgb)
cv2.waitKey(0)

# RGB to YUV
yuv = cv2.cvtColor(rgb, cv2.COLOR_BGR2YUV)
cv2.imshow("Converted",yuv)
cv2.waitKey(0)


# YUV to RGB
# Nos proporcionara una imagen casi identica a la original
rgb2 = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
cv2.imshow("Reconverted",rgb2)
cv2.waitKey(0)

# Print the mean and difference in the reconversion
diff = rgb.astype(np.int16) - rgb2
print("mean/stddev diff (RGB => YUV => RGB)", np.mean(diff), np.std(diff))
