import cv2 as cv
import numpy as np


def nothing():
    pass

img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("image")

#create teackbars
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

#create switch
switch = '0 : OFF\n1 :ON'
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # get the current pos of four trackbars
    r= cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')


    if s == 0 :
        img[:] = 0

    else:
        img [:] = [b,g,r]


cv.destroyAllWindows()



