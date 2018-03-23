import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *

class BackPropagation:

    def __init__(self):
        self.x_inputs = []
        self.targets = []
        self.inputWeights = []
        self.hiddenWeights = []
        self.maxEpochs = 0
        self.threshold = 0
        self.learningRate = 0
        self.w = []

    def back_propagation(self, x_inputs='Datasets/q2inputs.csv', target_inputs='Datasets/q2targets.csv', initial_input_weights_input=None,
                         initial_hidden_weights_input=None, max_epochs=None, threshold_error=None,
                         leaning_rate=None):
        H = 5
        f= lambda x:    1/(1+exp(-x))
        df = lambda x: 1/(1+exp(-x)) * (1-1./(1+exp(-x)))
        self.store(csv.reader(open(x_inputs)), csv.reader(open(target_inputs)))
        x_matrix = np.matrix(self.x_inputs[0],
                             self.x_inputs[1],
                             [1]*len(self.x_inputs[0]))
        self.inputWeights = np.matrix([0.5]*(H-1),
                                      )

        D1 = df((self.inputWeights.T, x_matrix))
        D1 = np.diag(D1[:,0])

        y = f((self.inputWeights.T, x_matrix))

    def store(self, x_inputs, target_inputs):
        self.x_inputs.append([])
        self.x_inputs.append([])
        i = 0
        for row in x_inputs:
            for col in row:
                self.x_inputs[i].append((float(col)/12.198))
            i += 1
        for row in target_inputs:
            for col in row:
                self.targets.append((float(col)/12.198))

    def plot(self):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X = np.arange(0, 21, 1)
        Y = np.arange(0, 21, 1)
        X, Y = np.meshgrid(X, Y)
        ax.plot_surface(X, Y, self.getZ(), rstride=1, cstride=1,cmap=plt.cm.coolwarm)
        ax.set_zlim(0, 2)

        ax.set_xlabel('input X1')
        ax.set_ylabel('input X2')
        ax.set_zlabel('Classifier')
        plt.show()

