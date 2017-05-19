
# import cv2 library
import cv2

class EyeTracker:
	def __init__(self, faceCascadePath, eyeCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
		self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

	def track(self, image):
        # detect faces and find face rectangles
        # 'faceRects' stores face region rectangles arrays in the form of (a,b,c,d)
        # a and b are initial points of rectangle, c and d are the width and height
        # initialize rects list, it will contain all faces and eyes rectangles coordinates
		faceRects = self.faceCascade.detectMultiScale(image,
			scaleFactor = 1.1, minNeighbors = 5,
			minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
		rects = []

        # loop over the face region rectangles (fX, fY, fW, fH)
        # (fX,fY) is initial point of face rectangle, (fW,fH) is width and height
        # extract the 'faceROI' which is the face region of image
        # update the rects list, (fX, fY) and (fX + fW, fY + fH) are the initial
        # and final points of the rectangle
		for (fX, fY, fW, fH) in faceRects:
			faceROI = image[fY:fY + fH, fX:fX + fW]
			rects.append((fX, fY, fX + fW, fY + fH))
			
            # detect eyes in the faceROI and find eye rectangles
			eyeRects = self.eyeCascade.detectMultiScale(faceROI,
				scaleFactor = 1.1, minNeighbors = 10, minSize = (20, 20),
				flags = cv2.CASCADE_SCALE_IMAGE)

            # update the rects list,(fX + eX, fY + eY) and (fX + eX + eW, fY + eY + eH)
            # are the initial and final points of the rectangle
			for (eX, eY, eW, eH) in eyeRects:
				rects.append(
					(fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))
    
        # return rects list, it will contain all faces and eyes rectangles coordinates
        # its form: [(fX, fY, fX + fW, fY + fH),(fX + eX, fY + eY, fX + eX + eW, fY + eY + eH),...]
		return rects

