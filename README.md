# flask_ocr_pytesseract
A python service that uses pytesseract wrapper for google tesseract to optically read images and return back detected values and fields, through the FLASK api.
The Api accepts Base64 encoded images as input, processes the image with Teseract and returns back detected text.
This project was meant to focus solely in detecting texts(fields and vlaues) in the govt. id cards like driving licence,pan card,aadhar card(samples for each in Images folder including the images,ther base64 encoding and screenshot for result/extracted text so obtained).

## Requirements/libraries: 
* Python 3
* [tesseract-ocr](https://github.com/tesseract-ocr/tesseract/wiki#installation)
* [Pytesseract](https://pypi.org/project/pytesseract/)
* [Pillow](https://github.com/python-pillow/Pillow)
* [Flask-web framework](http://flask.pocoo.org/)
* opencv
## Testing the application:
* clone or download the repo and move into the repo folder
* make sure all the requirements/installations are met.(activating an environment is suggested )
* run the app.py script: ```$ python3 app.py ```
* now encode the image to base64 (can use [Base64 image encoder](https://www.base64encode.net/base64-image-encoder)) or can try sample base64 urls present in the txt files in the images folder of the repo.
* Valid base64 input( "data:image/png;base64,"+ output from encoder (for PNG images)) will be processed and extracted text output will be displayed.(see sample image below)
<br></br>
![Sample IMage](https://github.com/Rahul30032/flask_ocr_pytesseract/blob/master/Images/ScreenShots/driving_license_screen.png)

## Tesseract 4.x installation 
If you're using ubuntu 16.04 or earlier version then by default tesseract 3 is installed using the commands in the official documentation.
I followed the follwing [link](https://orionfoysal.github.io/Installing-Tesseract4.0/) to install tesseract 4.x and corresponding version of leptonica(1.74 or higher).
[Link](https://github.com/tesseract-ocr/tessdata) to adding languages to tesseract 4.x 
You can also install through ppa:
```
$ sudo add-apt-repository ppa:alex-p/tesseract-ocr 
$ sudo apt-get update
$ sudo apt install tesseract-ocr
```
## Links to Resources followed :
* [Opencv import error(solution): ImportError: /opt/ros/kinetic/lib/python2.7/dist-packages/cv2.so: undefined symbol: PyCObject_Type
 ](https://komputervision.wordpress.com/2019/06/12/importerror-opt-ros-kinetic-lib-python2-7-dist-packages-cv2-so-undefined-symbol-pycobject_type/)
* [Base64 image encoder](https://www.base64encode.net/base64-image-encoder)
* [beginners guide to tesseract ocr using python](https://medium.com/better-programming/beginners-guide-to-tesseract-ocr-using-python-10ecbb426c3d)
* [PyTesseract: Simple Python Optical Character Recognition](https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/) ([Github link](https://github.com/ro6ley/python-ocr-example))
* [ocr with tesseract opencv and python](https://medium.com/@jaafarbenabderrazak.info/ocr-with-tesseract-opencv-and-python-d2c4ec097866) (Includes preprocessing of image using opencv)
* [opencv ocr and text recognition with tesseract](https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/)

## Possible Improvements/Changes:
* The tesseract model can be fine tuned and trained to specialise in a specific dataset/domain(like govt. IDs here)
* Can detect more than one language present in the image with small changes in the code. 
* Further improve on the aesthetics and appearances of the template and it's interaction with API.(For example can work on segregating fields and values from text outputs for better display in our case)
