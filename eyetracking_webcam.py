
# import packages and libraries
from qyqresearch.eyetracker import EyeTracker
from qyqresearch import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True,
	help = "path to where the face cascade resides")
ap.add_argument("-e", "--eye", required = True,
	help = "path to where the eye cascade resides")
args = vars(ap.parse_args())

# Initialize the camera resoution and framerate
# PiRGBArray() produces a 3-dimensional (rows, columns, colors) array from BGR capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# et is one instance in the EyeTracker class
# 0.1 is the number of seconds execution to be suspended
et = EyeTracker(args["face"], args["eye"])
time.sleep(0.1)

for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # return an infinite iterator of images captured continuously from the camera
    # grab the raw numpy array representing the image
	frame = f.array

    # resize the frame using the resize function in imutils.py
    # convert frame color from RGB(Red, Blue, Red) to Grayscale(all gray)
    # store the color converted frame in variable 'gray'
	frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect eyes and faces in the image
    # rects list contains all faces and eyes rectangles coordinates
	rects = et.track(gray)

    # draw all face and eyes rectangles
    # rect[0], rect[1]), (rect[2], rect[3]) are two points of a rectangle
    # (0, 255, 0), first 0 represents Blue, 255 represents Green, the last 0 represents red
    # we use green line to draw eyes and face rectangles
    # 2 is the thickness of the line
	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

    # the frame with face and eye rectangles shown in the window named 'Tracking'
    # clear and empty the raw capture
	cv2.imshow("Tracking", frame)
	rawCapture.truncate(0)

    # stop the loop if the key 'q' is pressed
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


