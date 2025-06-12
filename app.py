from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np
import pickle
from werkzeug.utils import secure_filename

import zipfile

app = Flask(__name__)


# Load the trained SVM model
MODEL_PATH = 'PetImages/SVM_CatDog_Model.pickle'
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

categories = ['Cat', 'Dog']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    resized = cv2.resize(img, (50, 50))
    flattened = resized.flatten().reshape(1, -1)
    return flattened

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            processed = preprocess_image(filepath)
            if processed is not None:
                prediction = model.predict(processed)[0]
                label = categories[prediction]
                return render_template('result.html', label=label, image_url=filepath)
            else:
                return "Error processing the image.", 400
        return redirect(request.url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
