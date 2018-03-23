import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import numpy.linalg as la


class LinearRegression:

    def __init__(self, data_set='eyesightData/signdist.data', learning_rate=0.00001, threshold=0.001):
        self.dataSetFile = csv.reader(open(data_set))
        self.sampleAge = []
        self.sampleDistance = []
        if self.dataSetFile is not None:
            self.store_data()
        self.slope = 0
        self.intercept = 0
        self.learningRate = learning_rate
        self.threshold = threshold
        self.weights = None

    def store_data(self):
        for row in self.dataSetFile:
            self.sampleAge.append(float(row[0]))
            self.sampleDistance.append(float(row[1]))

    def plot(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(self.sampleAge,
                self.sampleDistance, 'g',
                marker='o', markersize=15, linestyle='None'
                )
        ax.plot(np.arange(0, 100, 2),
                self.straightLinePoints(),
                'r', markersize=30)

        ax.set_xlabel('Age')
        ax.set_ylabel('Seeing Distance (m)')
        plt.show()

    def plot2(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(self.sampleAge,
                   self.sampleDistance,
                   marker='o', s=20)
        ax.surface()

    def straightLinePoints(self):
        points = []
        for i in range(0, 100, 2):
            points.append(self.weights.item(0)*i+self.weights.item(1))
        return points

    def linear_regression(self):
        self.weights = self._linear_regression()
        self.plot()
        self.questions()

    def _linear_regression(self):
        y_matrix = np.mat(self.sampleDistance).T
        x_matrix = np.mat([self.sampleAge,
                          [1]*len(self.sampleDistance)])
        weights = self.initialize_weights()
        error = 0.5*((y_matrix - x_matrix.T*weights).T*(y_matrix - x_matrix.T*weights))
        converged = False
        iterations = 0
        while not converged :
            iterations += 1
            gradient = x_matrix*(y_matrix - x_matrix.T*weights)
            weights += self.learningRate*gradient
            current_error = 0.5*((y_matrix - x_matrix.T*weights).T*(y_matrix - x_matrix.T*weights))
            print abs(current_error.item(0) - error.item(0))
            print iterations
            if abs(current_error - error) < self.threshold :
                return weights
            error = current_error



    def initialize_weights(self):
        """
        guess initial weights using the gradient of 2 samples
        :return: initial weight guesses
        """

        # Y2-Y1/X2-X1
        slope = (self.sampleDistance[len(self.sampleDistance)-1]-self.sampleDistance[0]) /\
                (self.sampleAge[len(self.sampleAge)-1]-self.sampleAge[0])
        intercept = self.closest_sample_to_origin()
        return np.mat([slope, intercept]).T

    def closest_sample_to_origin(self):
        return self.sampleDistance[self.sampleAge.index(min(self.sampleAge))]

    def questions(self):
        print 'Weight vector = ',
        print self.weights
        print 'Using the resulting function Y = wX + C :'
        print 'The expected distance a 16 year old can see is ',
        print self.weights.item(0)*16+self.weights.item(1)
        print 'The expected distance a 90 year old can see is ',
        print self.weights.item(0)*90+self.weights.item(1)
# x = LinearRegression()
# x.plot()






