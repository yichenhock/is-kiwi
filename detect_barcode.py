# # import the necessary packages
# import numpy as np
# import argparse
# import imutils
# import cv2
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
# 	help = "path to the image file")
# args = vars(ap.parse_args())

# # load the image and convert it to grayscale
# image = cv2.imread(args["image"])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # compute the Scharr gradient magnitude representation of the images
# # in both the x and y direction using OpenCV 2.4
# ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
# gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
# gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
# # subtract the y-gradient from the x-gradient
# gradient = cv2.subtract(gradX, gradY)
# gradient = cv2.convertScaleAbs(gradient)

# # blur and threshold the image
# blurred = cv2.blur(gradient, (9, 9))
# (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

# # construct a closing kernel and apply it to the thresholded image
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
"""
:D
"""
# import the necessary packages
from pyimagesearch import simple_barcode_detection
from imutils.video import VideoStream
import argparse
import time
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())
# if the video path was not supplied, grab the reference to the
# camera
if not args.get("video", False):
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
# otherwise, load the video
else:
	vs = cv2.VideoCapture(args["video"])

# keep looping over the frames
while True:
	# grab the current frame and then handle if the frame is returned
	# from either the 'VideoCapture' or 'VideoStream' object,
	# respectively
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
 
	# check to see if we have reached the end of the
	# video
	if frame is None:
		break
	# detect the barcode in the image
	box = simple_barcode_detection.detect(frame)
	# if a barcode was found, draw a bounding box on the frame
	if box is not None:
		cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
	# show the frame and record if the user presses a key
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# if we are not using a video file, stop the video file stream
if not args.get("video", False):
	vs.stop()
# otherwise, release the camera pointer
else:
	vs.release()
# close all windows
cv2.destroyAllWindows()