import numpy as np
from PIL import Image
import cv2
import tensorflow as tf

class fruit:
    def __init__(self,filename):
        self.filename =filename


    def fruitCheck(self):

        model_path = "model/model.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        imagename = self.filename
        image = cv2.imread(imagename)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((150, 150))
        expand_input = np.expand_dims(resize_image,axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        pred = loaded_model.predict(input_data)
        result = pred.argmax()

        if result == 0:
            prediction = 'FreshApple'
            return [{"image": prediction}]
        elif result == 1:
            prediction = 'FreshBanana'
            return [{"image": prediction}]
        elif result == 2:
            prediction = 'FreshGrape '
            return [{"image": prediction}]
        elif result == 3:
            prediction = 'FreshGuava'
            return [{"image": prediction}]
        elif result == 4:
            prediction = 'FreshJujube'
            return [{"image": prediction}]
        elif result == 5:
            prediction = 'FreshOrange'
            return [{"image": prediction}]
        elif result == 6:
            prediction = 'FreshPomegranate'
            return [{"image": prediction}]
        elif result == 7:
            prediction = 'FreshStrawberry'
            return [{"image": prediction}]
        elif result == 8:
            prediction = 'RottenApple'
            return [{"image": prediction}]
        elif result == 9:
            prediction = 'RottenBanana '
            return [{"image": prediction}]
        elif result == 10:
            prediction = 'RottenGrape'
            return [{"image": prediction}]
        elif result == 11:
            prediction = 'RottenGuava'
            return [{"image": prediction}]
        elif result == 12:
            prediction = 'RottenJujube'
            return [{"image": prediction}]
        elif result == 13:
            prediction = 'RottenOrange'
            return [{"image": prediction}]
        elif result == 14:
            prediction = 'RottenPomegranate'
            return [{"image": prediction}]
        elif result == 15:
            prediction = 'RottenStrawberry'
            return [{"image": prediction}]
        else:
            return [{"ERROR": "Please select another image"}]

