import cv2
import numpy as np
from watermarking import watermarking

image = cv2.imread("20190929_135314.jpg")
watermark = cv2.imread("sun-bear.png", cv2.IMREAD_UNCHANGED)
# Showing the result
final = watermarking(image, watermark)
cv2.imshow("Watermarked image",final)
cv2.waitKey(0)
cv2.destroyAllWindows()
