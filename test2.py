# #webcam
# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from cvzone.ClassificationModule import Classifier
# import numpy as np
# import math
#
#
#
# cap=cv2.VideoCapture(0) # 0 is id no. for webcam
# detector=HandDetector(maxHands=1) # 1 hand
# classifier=Classifier("Model/keras_model.h5","Model/labels.txt")
#
# offset=20
# imgSize=300
#
# folder="Data/K"
# counter=0
# labels= ["A","B","C","K"]
#
# while True:                 #while loop for vid as vid is series of img
#     success,img=cap.read()  #success is bool...img is name given to vid(like a variable)
#     imgOutput=img.copy()
#     hands,img=detector.findHands(img)
#
#     # cropping hands
#
#     if hands:
#         hand = hands[0]
#         x, y, w, h =hand['bbox']
#
#         imgWhite=np.ones((imgSize,imgSize,3),np.uint8)*255  #matrix
#
#         imgCrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
#
#         #put image crop inside image white
#         imgCropShape=imgCrop.shape
#
#         aspectRatio =h/w
#         if aspectRatio>1:
#             k=imgSize/h
#             wCal=math.ceil(k*w)
#             imgResize=cv2.resize(imgCrop,(wCal,imgSize))
#             imgResizeShape=imgResize.shape
#             wGap=math.ceil((imgSize-wCal)/2)
#             imgWhite[:, wGap:wCal+wGap] = imgResize
#             prediction,index=classifier.getPrediction(imgWhite,draw=False)
#             print(prediction,index)
#
#
#         else:
#             k = imgSize / w
#             hCal = math.ceil(k * h)
#            # try:
#
#             imgResize = cv2.resize(imgCrop, (imgSize,hCal))
#            # except:
#                 #print("Exception!!")
#                 #print("imgCrop={}, imgSize={}, hCal={}", imgCrop, imgSize, hCal)
#
#             imgResizeShape = imgResize.shape
#             hGap = math.ceil((imgSize - hCal) / 2)
#             imgWhite[hGap:hCal + hGap,: ] = imgResize
#             prediction, index = classifier.getPrediction(imgWhite,draw=False)
#
#         cv2.rectangle(imgOutput, (x - offset, y - offset-50), (x - offset+90, y - offset-50+50), (0,0,0), cv2.FILLED)
#         cv2.putText(imgOutput,labels[index],(x,y-26),cv2.FONT_HERSHEY_COMPLEX,1.8,(255,255,255),2)
#         cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(0,0,0),4)
#
#         cv2.imshow("ImageCrop", imgCrop)
#         cv2.imshow("ImageWhite", imgWhite)
#
#     cv2.imshow("Image",imgOutput)
#     cv2.waitKey(1) #1sec delay
#
#

# webcam
def webcam1():
    import cv2
    from cvzone.HandTrackingModule import HandDetector
    from cvzone.ClassificationModule import Classifier
    import numpy as np
    import math

    cap = cv2.VideoCapture(0)  # 0 is id no. for webcam
    detector = HandDetector(maxHands=1)  # 1 hand
    classifier = Classifier(r"C:\Users\mcvan\PycharmProjects\ObjectDetection\Model\keras_model.h5", r"C:\Users\mcvan\PycharmProjects\ObjectDetection\Model\labels.txt")

    offset = 20
    imgSize = 300

    folder = "Data/K"
    counter = 0
    labels = ["A", "B", "C", "K"]

    success, img = cap.read()  # Get the first frame from the webcam
    while True:  # while loop for vid as vid is series of img
        # success,img=cap.read()  #success is bool...img is name given to vid(like a variable)
        imgOutput = img.copy()
        hands, img = detector.findHands(img)

        # cropping hands

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  # matrix

            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            # put image crop inside image white
            imgCropShape = imgCrop.shape

            aspectRatio = h / w
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                print(prediction, index)


            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                # try:

                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                # except:
                # print("Exception!!")
                # print("imgCrop={}, imgSize={}, hCal={}", imgCrop, imgSize, hCal)

                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)

            cv2.rectangle(imgOutput, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50), (0, 0, 0),
                          cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.8, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (0, 0, 0), 4)

            cv2.imshow("ImageCrop", imgCrop)
            cv2.imshow("ImageWhite", imgWhite)

        # cv2.imshow("Image",imgOutput)
        #  #1sec delay

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        cv2.imshow("Output", imgOutput)
        cv2.waitKey(1)
    cap.release()
