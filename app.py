from flask import Flask, render_template, request, jsonify
from predict import fruit

# flask utils
from flask_cors import CORS, cross_origin
from utils.utils import decodeImage

import os

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# define a flask app
app = Flask(__name__)


class ClientApp:
    def __init__(self):
        self.filename = "logo.png"
        self.classifier = fruit(self.filename)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.fruitCheck()
    return jsonify(result)

if __name__== '__main__':
    clApp = ClientApp()
    app.run(port=3000, debug=True)