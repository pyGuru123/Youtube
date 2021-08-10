# Read QR code with python

# pip install opencv-python
# download opencv : https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

import cv2

img = cv2.imread('QRtest.png')
detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
	print(data)

	n_lines = len(bbox)
	for i in range(n_lines):
		point1 = tuple(bbox[i][0])
		point2 = tuple(bbox[(i+1) % n_lines][0])
		cv2.line(img, point1, point2, color=(255,0,0), thickness=2)

# display the result
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()