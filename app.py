from flask import Flask, render_template, request
# from keras.applications import ResNet50
import cv2
import numpy as np
import pandas as pd
import imageio
import demo

app = Flask(__name__)

# resnet = ResNet50(weights='imagenet',input_shape=(224,224,3),pooling='avg')
print("+"*50, "Model is loaded")



@app.route('/')
def index():
	return render_template(r"index.html", data="hey")


@app.route("/prediction", methods=["POST"])
def prediction():

	img = request.files['img']

	img.save("img.jpg")

	image = imageio.imread("img.jpg")

	link = demo.halua(image,"crop")

	return render_template("prediction.html", data=link)


if __name__ == "__main__":
	app.run(debug=True)