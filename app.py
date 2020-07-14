from flask import Flask,render_template,request
import os

from ocr_core import ocr_core

Upload_file = '/static/uploads'

allowed_extns = set(['png','jpg','jpeg'])

app = Flask(__name__)

def allowed_file(fname):
	return '.' in fname and \
			fname.rsplit('.',1)[1].lower() in allowed_extns


@app.route('/')
def home_page():
	return render_template('index.html')
	# return "Hello"


@app.route('/upload',methods=['GET','POST'])
def upload_page():
	if request.method == "POST":
		if 'file' not in request.files:
			return render_template('upload.html',msg='No file selected')
		file = request.files['file']
		if file.filename == '':
			return render_template('upload.html',msg='No file selected')

		if file and allowed_file(file.filename):
			extracted_text = ocr_core(file)
			return render_template('upload.html',
									msg='Succesfully processed',
									extracted_text = extracted_text,
									img_src = Upload_file + file.filename)
	elif request.method == "GET":
		return render_template('upload.html')

if __name__ == '__main__':
	app.run()