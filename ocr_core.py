try:
	from PIL import Image
except ImportError:
	import Image
import pytesseract
# from pytesseract import Output #for image_to_data_implementation
import base64
import io
import numpy as np
# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 #for preprocessing
# sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

def ocr_core(fname):
	imgstring = fname.split('base64,')[-1].strip()
	pic = io.StringIO()
	image_string = io.BytesIO(base64.b64decode(imgstring))
	convert_and_save(imgstring)
	image = Image.open(image_string)

	img = cv2.imread("imageToSave.png")
	# image preprocessing
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscalling the image
	kernel = np.ones((5,5),np.uint8)
	cv2.dilate(img, kernel, iterations = 2) #dilation
	cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] #thresholding
	# cv2.Canny(img, 100, 200) # canny edge detection
	custom_config = r'--oem 2 --psm 12' # psm: 12 = sparse text with osd , oem: 2 = Legacy+LSTM engines
	text = pytesseract.image_to_string(img, config=custom_config, lang="eng+hin")
	# attempted implementation wih image_to_data
	# d = pytesseract.image_to_data(img, output_type=Output.DICT)
	# return d.keys()
	return text

def convert_and_save(b64_string):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(b64_string))

