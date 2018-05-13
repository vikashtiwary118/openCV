# -*- coding: utf-8 -*-
import numpy as np
import cv2

img=cv2.imread('1.jpg',0)
print(img)

cv2.imshow('image',img)
cv2.waitKey(0)
#cv2.imWrite('dogImage.png',img)
cv2.destroyAllWindows()
