import numpy as np
from multilayer_perceptron import MultilayerPerceptron

model = MultilayerPerceptron()

inputs = [np.array([1.0, 0.5, -1.0]),
          np.array([0.0, 0.0, 0.0]),
          np.array([2.0, -1.0, 0.5]),
          np.array([-1.5, 2.0, 1.0])]
 
    
# forward propagation process for each input
for x in inputs:
    y = model.forward(x)
    print("input :", x)
    print("output:", np.round(y, 4))
    print()
 
