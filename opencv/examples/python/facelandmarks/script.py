"""
https://pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
https://stackoverflow.com/questions/43938207/face-aligment-check-with-dlib
python script.py #--shape-predictor shape_predictor_68_face_landmarks.dat
"""
# import the necessary packages
from imutils.video import VideoStream
import time
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", 
    "--shape-predictor", 
    required=False,
    nargs='?', 
    default='shape_predictor_81_face_landmarks.dat',
	help="path to facial landmark predictor",
    )
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# time.sleep(2.0)

while True:
    # grab the frame from the threaded video stream, resize it to
    # have a maximum width of 400 pixels, and convert it to
    # grayscale
    frame = vs.read()
    frame = imutils.resize(frame, width=1200)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # loop over the face detections
    for rect in rects:
        print(f"rect {rect}")

        # # determine the facial landmarks for the face region, then
        # # convert the facial landmark (x, y)-coordinates to a NumPy
        # # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        print(f"shape {shape}")

        # # loop over the (x, y)-coordinates for the facial landmarks
        # # and draw them on the image
        for (x, y) in shape:
            print(f"x y {x, y}")
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)
            cv2.putText(frame, "Face landmarks", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # show the frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q pressed")
        break

