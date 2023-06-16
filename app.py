from tensorflow import keras

# flask utils
from flask import Flask, render_template, redirect, url_for, request

# define a flask app
app = Flask(__name__)

# Load the model from the .h5 file
model = keras.models.load_model('model\model.h5')

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)
    return render_template("index.html", prediction_text = "{}").format(prediction)

if __name__== '__main__':
    app.run(port=3000, debug=True)