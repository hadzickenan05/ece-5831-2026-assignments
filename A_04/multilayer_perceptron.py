import numpy as np

class MultilayerPerceptron:

    def __init__(self):
        self.network = {}

        self.network["W1"] = np.array([[ 0.1,  0.3,  0.5, -0.2,  0.4],
                                       [ 0.2, -0.4,  0.6,  0.3, -0.1],
                                       [-0.3,  0.5,  0.1,  0.4,  0.2]])
        self.network["b1"] = np.array([0.1, 0.2, -0.1, 0.3, 0.1])
        
        # hidden layer 1 (5) -> hidden layer 2 (5)
        self.network["W2"] = np.array([[ 0.2, -0.1,  0.4,  0.3, -0.2],
                                       [ 0.5,  0.2, -0.3,  0.1,  0.4],
                                       [-0.4,  0.3,  0.2,  0.5,  0.1],
                                       [ 0.1,  0.4, -0.2, -0.3,  0.3],
                                       [ 0.3, -0.5,  0.1,  0.2,  0.2]])
        self.network["b2"] = np.array([0.1, -0.1, 0.2, 0.1, -0.2])
 
        # hidden layer 2 (5) -> hidden layer 3 (2)
        self.network["W3"] = np.array([[ 0.9, -1.2],
                                       [-0.6,  1.5],
                                       [ 1.2,  0.3],
                                       [ 0.3, -0.9],
                                       [-1.5,  0.6]])
        self.network["b3"] = np.array([0.1, -0.1])
 
        # hidden layer 3 (2) -> output layer (2)
        self.network["W4"] = np.array([[1.0, -2.0],
                                       [2.0,  3.0]])
        self.network["b4"] = np.array([-1.0, -0.2])

    def sigmoid(self, s):
        return 1 / (1 + np.exp(-s))

    def relu(self, s):
        return np.maximum(0,s)


    def forward(self, s):

        w1 = self.network["W1"]
        b1 = self.network["b1"]
        a1 = np.dot(s, w1) + b1
        z1 = self.sigmoid(a1)

        w2 = self.network["W2"]
        b2 = self.network["b2"]
        a2 = np.dot(z1, w2) + b2
        z2 = self.sigmoid(a2)

        w3 = self.network["W3"]
        b3 = self.network["b3"] 
        a3 = np.dot(z2, w3) + b3
        z3 = self.sigmoid(a3)

        w4 = self.network["W4"]
        b4 = self.network["b4"] 
        a4 = np.dot(z3, w4) + b4
        output = self.relu(a4)

        return output

