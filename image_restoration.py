import numpy as np
import cv2
img = cv2.imread("C:\\Users\\gokul\\PycharmProjects\DIP\\tuberculosis.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edge_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,- 1,-1]])

sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
img = cv2.filter2D(grayscale, -1, sharpen_kernel)

# Smooth out image
# blur = cv2.medianBlur(img, 3)
blur = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow('img',img)
cv2.imwrite('img.png',img)
cv2.imshow('blur',blur)
cv2.waitKey(0)