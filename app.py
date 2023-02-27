import os 
import json
from flask import Flask, render_template, jsonify, request
from create import create_captcha
import io
from base64 import encodebytes
from flask import after_this_request
import time
import base64
from flask import send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return {"Welcome to": "Captcha Generating API", "creator": "Abdul Rehman Kalsekar (arkalsekar)", "email":"abdulrehmankalsekar10@gmail.com", "Endpoints": "/getCaptcha"}



@app.route('/getCaptcha/', methods=['GET'])
def get_image():
    if request.method == "GET":
        captcha = create_captcha()

    else:
        return "Sorry some Internal Error Occured"
    
    # return send_file(filename, mimetype='image/png')
    return {"Captcha": captcha[1], "Bytes": captcha[0]}

 


app.run(debug=True)