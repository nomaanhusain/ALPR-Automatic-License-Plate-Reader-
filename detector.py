import numpy as np
import cv2


img = cv2.imread("D:\\Projects_Code\\carnumber plate\\1.jpg")

cv2.imshow("img",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"D:\\Projects_Code\\carnumber plate\\car_number_plate.xml")
plates = plate_cascade.detectMultiScale(gray)


for (x,y,w,h) in plates:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)