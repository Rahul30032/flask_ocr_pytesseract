try:
	from PIL import Image
except ImportError:
	import Image
import pytesseract

def ocr_core(fname):
	text = pytesseract.image_to_string(Image.open(fname))
	return text
print(ocr_core('/home/rahul/Pictures/py_ocr_test_13072020.png'))



# try:
# 	from PIL import Image
# except ImportError:
# 	import Image
# import pytesseract
# import base64
# import io
# import cv2 #for preprocessing
# def ocr_core(fname):
# 	imgstring = fname.split('base64,')[-1].strip()
# 	pic = io.StringIO()
# 	image_string = io.BytesIO(base64.b64decode(imgstring))
# 	image = Image.open(image_string)
# 	# Overlay on white background
# 	bg = Image.new("RGB", image.size, (255,255,255))
# 	bg.paste(image,image)
# 	img = cv2.imread(bg)
# 	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	img = cv2.medianBlur(img,5)
# 	text = pytesseract.image_to_string(img)
# 	return text
# # print(ocr_core('/home/rahul/Pictures/py_ocr_test_13072020.png'))