#!/usr/bin/python
# -*- coding: utf-8 -*-
## Written by Andrew Cutts

import cv2 as cv

def click_event(event, x, y, flags, param):
	if event == cv.EVENT_RBUTTONDOWN:
		print(x, y)
	if event == cv.EVENT_LBUTTONDOWN:
		red = img[y,x,2]
		blue = img[y,x,0]
		green = img[y,x,1]
		print(red, green, blue)
		strRGB = str(red) + "," + str(green) + "," +str(blue)
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(img,strRGB,(x,y), font, 1.5, (255,255,255),2)
		cv.imshow('original', img)	
		
img = cv.imread('usgs.jpg')
cv.imshow('original', img)

cv.setMouseCallback("original", click_event)
cv.waitKey(0)

cv.destroyAllWindows
