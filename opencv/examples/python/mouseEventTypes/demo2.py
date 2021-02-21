#!/usr/bin/python
# -*- coding: utf-8 -*-
## Written by Andrew Cutts
### Script to draw a point on each click and connect a line on an (satellite) image using opencv

import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, param):
	if event == cv.EVENT_LBUTTONDOWN:
		### Put text of x,y location
		strtext = str(x) + "," + str(y) 
		font = cv.FONT_HERSHEY_SIMPLEX
		cv.putText(img,strtext,(x,y), font, 1.5, (255,255,255),2)
		### Place a point on the location of click
		cv.circle(img,(x,y), 10, (0,0,255), 5)	
		point.append((x,y))
		### draw a line on the image once we have 2 or more points in point list
		if len(point) >= 2:
			cv.line(img,point[-1],point[-2],(0,0,0),2)	
		cv.imshow('original', img)
				
img = cv.imread('usgs.jpg')
cv.imshow('original', img)
point = []
cv.setMouseCallback("original", click_event)
cv.waitKey(0)
cv.destroyAllWindows
