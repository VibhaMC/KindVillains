#webcam
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap=cv2.VideoCapture(0) # 0 is id no. for webcam
detector=HandDetector(maxHands=1) # 1 hand

offset=20
imgSize=300

folder="Data/K"
counter=0


while True:
    success,img=cap.read()
    hands,img=detector.findHands(img)

    # cropping hands

    if hands:
        hand = hands[0]
        x, y, w, h =hand['bbox']

        imgWhite=np.ones((imgSize,imgSize,3),np.uint8)*255#matrix

        imgCrop=img[y-offset:y+h+offset,x-offset:x+w+offset]

        #put image crop inside image white
        imgCropShape=imgCrop.shape

        aspectRatio =h/w
        if aspectRatio>1:
            k=imgSize/h
            wCal=math.ceil(k*w)
            imgResize=cv2.resize(imgCrop,(wCal,imgSize))
            imgResizeShape=imgResize.shape
            wGap=math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize,hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap,: ] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image",img)
    key=cv2.waitKey(1) #1sec delay
    if key==ord("a") : #save  when s is pressed
        counter+=1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)


