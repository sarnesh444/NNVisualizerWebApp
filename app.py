import requests #used to make a request to the server
import json
import numpy as np
import streamlit as st
import os
import matplotlib.pyplot as plt

URI = 'http://127.0.0.1:5000'

st.title('Neural Network Visualizer')
st.sidebar.markdown('# Input Image')
#enters if block only when button is clicked
if st.button('Get random predictions'):
    #response = requests.post(URI,data={})
    st.markdown("### The lighter the box higher is the chance that it is getting activated!")
    response=requests.post(URI)

#since json.dumps() throws a string it has to be converted back to original
#datastructure using json.loads()
    response = json.loads(response.text)

#response.get(param) param should match with key in key-val json returned
    preds = response.get('prediction')
    image = response.get('image')
#image is returned as a list now list has to be converted to an image
#returned:array of len 784 => rendered:image 28x28 so reshaped 784=>28x28
    image = np.reshape(image, (28, 28))

    st.sidebar.image(image, width=150)

    for layer, p in enumerate(preds):
        #to keep dimensions consistent squeezed
        numbers = np.squeeze(np.array(p))
#since 32 nodes per layer,this is the size of the entire plot
        plt.figure(figsize=(32, 4))
#layer==2 means it is the final layer(0-i/p layer(32) 1-hidden(32) 2-o/p layer(10))
#o/p layer has 10 labels 0to9 as output so 1 row and 10 col(1*10=10 nodes)
#for i/p and hidden layer there are 32 nodes(16 cols and 2 rows=16*2=32 nodes)
        if layer == 2:
            row = 1
            col = 10
        else:
            row = 2
            col = 16

        for i, number in enumerate(numbers):
            plt.subplot(row, col, i + 1)
#np.ones=gives a matrix of specified shape with every val as 1

#but if every val is 1 all the boxes will be white so

#number=has the val of the node of a layer returned it is
#multiplied with the number to the get val of a node for a layer

#since an array cannot be displayed as a box with varying color
#imshow is used to show it as an image
#dark being less probable and light being more probable
            plt.imshow((number * np.ones((8, 8, 3))).astype('float32'), cmap='binary')
            plt.xticks([])
            plt.yticks([])
#if it is the final/output layer only then target labels shown,all target labels shown
            if layer == 2:
                plt.xlabel(str(i), fontsize=40)
#used to adjust the sub-plots so that they are rightly placed
        plt.subplots_adjust(wspace=0.05, hspace=0.05)
        plt.tight_layout()
#displays the layer number
        st.text('Layer {}'.format(layer + 1), )
#used to plot a graph
        st.pyplot()
