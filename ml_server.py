import json
import tensorflow as tf
import numpy as np
import os
import random
import string

from flask import Flask, request

app = Flask(__name__)

model = tf.keras.models.load_model(r'C:\Users\saran\Desktop\guided_project\NNVisualizer\heroku\NNVisualizerWebApp\models\model.h5')

#since we want the output of all the layers to visualize we rewire the model
# to get the output of each layer instead of just the final output
#model.inputs=so the input remains the same
#[layer.output for layer in model.layers]=gives the output of each layer in the model
feature_model = tf.keras.models.Model(model.inputs, [layer.output for layer in model.layers])

#collecting only x_test and normalizing
#a random image is picked from x_test itself
_, (x_test, _) = tf.keras.datasets.mnist.load_data()
x_test = x_test / 255.

def get_prediction():
    index = np.random.choice(x_test.shape[0]) #random index of some image
    image = x_test[index,:,:] #image at random index
    image_arr = np.reshape(image, (1, 784)) #unpacking image at random index
    return feature_model.predict(image_arr), image
#returning image and the prediction label for the randomly selected input

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        preds, image = get_prediction() #since returns pred of an image and image
        final_preds = [p.tolist() for p in preds]
#since the response is rendered in json and it does not suppport numpy array
#but supports only a list so prediction has to be converted to a list
        #json dump converts response to be rendered into a string
        #image is also coverted to a list and returned
        return json.dumps({'prediction': final_preds, 'image': image.tolist()})
    #if a get request encountered
    return 'Welcome to the ml server'

if __name__ == '__main__':
    app.run()
