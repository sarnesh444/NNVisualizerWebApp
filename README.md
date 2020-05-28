# NNVisualizerWebApp

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## This webapp is used to visualize a Deep Neural Network.
The model is trained on MNSIT(hand written digits) using tf+keras in google colab and exported as h5 using Flask a backend code to handle get and post requests is written the front-end is entirely written in streamlit using which the user can send a post request server selects an image at random from the test set and returns the output of each layer.
#### The lighter the box higher is the chance that it is getting activated!

## Major tools used

* [Streamlit](https://docs.streamlit.io/en/latest/) a python package to create web applications for a machine learning ecosystem.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) a python back-end framework for web apps.

* [TensorFlow](https://www.tensorflow.org/) a python library to build machine/deep learning models.

## Prerequisites

This package assumes you use Python 3.7 or more.

### Dependencies
Install the dependencies using PIP the package manager for python
Make sure the streamlit version is above 0.49.0
```
pip install requirements.txt
```
## Steps to run:
* Firstly upgrade pip to the lateest version
* Install anaconda navigator and command prompt
* To install tensorflow without any hassle for CPU+3.7 rather than using pip use the following commands from anaconda prompt
* conda create -n tf tensorflow  conda activate tf
* After the env is activated clone this repository and navigate to the directory
* Start the server using the following command: "python ml-server.py"
* Open a new terminal navigate to the directory and run the command "streamlit run app.py"

## Contributing

If you found any mistakes in my code, or if you can enhance the quality of documention, please feel free to contribute!
Here are 3 steps to contributing.

1. [Fork](https://github.com/sarnesh444/IndianNumberPlateDetection/fork) this project.
2. Commit your changes.
3. Create a new Pull Request and link an [issue](https://github.com/sarnesh444/IndianNumberPlateDetection/issues/new) with it.

## Meta 

| Name | Github | LinkedIn | E-mail | Phone|
| --- | --- | --- | --- | --- |
| Saranesh ManiRatna.K | [@saranesh](https://github.com/sarnesh444) | [@saranesh](https://www.linkedin.com/in/saranesh-kanumuri-17a7a5181/) |[E-mail](mailto:sarnesh444@gmail.com) | [(+91) 8500717519](tel:+918500717519)

#### This project is NOT meant for production and hasn't been tested thoroughly.




### Sample
![alt text](https://github.com/sarnesh444/NNVisualizerWebApp/blob/master/sample.JPG)
