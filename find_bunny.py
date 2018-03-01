import cv2
import numpy as np
from matplotlib import pyplot as plt

file_path = "C:\\Users\\reina\\Documents\\Bunny Detection\\bunny.jpg"
img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)

if img is not None:
	print("Read sucessful!")
else:
	print("Read failed")

#show image
cv2.imshow("Image", img)

# exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()

#do stuff...
