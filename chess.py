
import cv2
import numpy as np

img = np.zeros((400,400,3))

for i in range(0,8):
    for j in range(0,8,2):
        if(i%2==0):     
            img[50*i:50*(i+1), 50*j:50*(j+1)] = 255,255,255
        else:
            img[50*i:50*(i+1), 50*(j+1):50*(j+2)] = 255,255,255

cv2.imshow('CHESS BOARD', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
