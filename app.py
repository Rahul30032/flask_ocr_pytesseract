from flask import Flask,render_template,request
import os

from ocr_core import ocr_core



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def upload_page():
	if request.method == "POST":

		data = request.form['url']
		if data is None:
			return render_template('upload.html',msg='No files selected')
		
		file = data

		if file== '':	
			return render_template('upload.html',msg='No file selected')

		if file :
			extracted_text = ocr_core(file)
			return render_template('upload.html',
									msg='Succesfully processed',
									extracted_text = extracted_text,
									img_src = file)
	elif request.method == "GET":
		return render_template('upload.html')

if __name__ == '__main__':
	app.run(debug=True)