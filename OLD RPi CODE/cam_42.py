import cv2
import numpy as np
import picamera
from picamera.array import PiRGBArray
import time
import FTPUpload as ftp
import os

camera = picamera.PiCamera()
camera.vflip = True
end = time.time() + 20

fFace1 = cv2.CascadeClassifier('/home/pi/Downloads/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_alt.xml')
fFace2 = cv2.CascadeClassifier('/home/pi/Downloads/opencv-3.0.0/data/haarcascades_cuda/haarcascade_frontalface_default.xml')

pFace = cv2.CascadeClassifier('/home/pi/Downloads/opencv-3.0.0/data/haarcascades_cuda/haarcascade_profileface.xml')

x=0
while time.time() < end:
    filename = 'image' + str(x) + '.jpg'
    camera.capture(filename)
    image = np.asarray(cv2.imread(filename))
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #numFaces = len(fFace1.detectMultiScale(grayScale, 1.2, 4))
    numFaces = len(fFace2.detectMultiScale(grayScale, 1.3, 4))
    #numFaces += len(pFace.detectMultiScale(grayScale, 1.1, 4))
    
    if numFaces > 0:
        ftp.Upload(filename)
        x+=1
    os.remove(filename)
    print(numFaces)

camera.close()

exit(0)
