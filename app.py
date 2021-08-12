# importing dependencies
from predictor import processImg
# import glob
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = "detectform"

Valid_ext = {'jpeg', 'png', 'jpeg'}


def valid_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Valid_ext


path = os.getcwd()
UploadFolder = os.path.join(path, 'uploads')
if not os.path.isdir(UploadFolder):
    os.mkdir(UploadFolder)

BASE_DIR = os.getcwd()
dir = os.path.join(BASE_DIR, "uploads")

for root, dirs, files in os.walk(dir):
    for file in files:
        path = os.path.join(dir, file)
        os.remove(path)

app.config['UPLOAD_FOLDER'] = UploadFolder

# Home Page


@app.route('/')
def index():
    return render_template('index.html')

# Prediction - Vehicle Details Page


@app.route('/result', methods=['POST'])
def upload_file():
    global ImgPath
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        imagePath = UploadFolder + "\\" + uploaded_file.filename
        uploaded_file.save(imagePath)
        print(imagePath)
    vehDetails = processImg(imagePath)
    print(f"vehDetails : {vehDetails}")

    # EMPTY UPLOAD FOLDER
    BASE_DIR = os.getcwd()
    dir = os.path.join(BASE_DIR, "uploads")

    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(dir, file)
            os.remove(path)

    carDesc = vehDetails["CarMake"]["CurrentTextValue"]
    carModel = vehDetails["CarModel"]["CurrentTextValue"]
    print(carModel)
    return render_template("/result.html", carDesc=carDesc, carModel=carModel, vehDetails=vehDetails)


if __name__ == '__main__':
    app.run(debug=True)
