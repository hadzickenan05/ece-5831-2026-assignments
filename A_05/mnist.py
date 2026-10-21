import pickle
import numpy as np
from PIL import Image


class Mnist:
    def __init__(self, weightpath='sample_weight.pkl'):

        self.network = pickle.load(open(weightpath, 'rb'))


    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):

        e = np.exp(x)
        return e / np.sum(e)

    def predict(self, x):
        W1, W2, W3 = self.network['W1'], self.network['W2'], self.network['W3']
        b1, b2, b3 = self.network['b1'], self.network['b2'], self.network['b3']


        a1 = np.dot(x, W1) + b1
        z1 = self.sigmoid(a1)

        a2 = np.dot(z1, W2) + b2
        z2 = self.sigmoid(a2)

        a3 = np.dot(z2, W3) + b3
        y = self.softmax(a3)

        return y


    def loadimg(self, path):
        img = Image.open(path).convert('L')
        img = img.resize((28, 28))
        img = np.array(img, dtype=np.float32)

        #Invert color for black background as shown in lecture and Mnist
        if np.mean(img) > 127:
            img = 255.0 - img

        img = img / 255.0
        return img