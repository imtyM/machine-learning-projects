import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import Queue
import math
import numpy as np

class KNN:

    def __init__(self, training_data_set='irisData/trainData.data',
                       sample_set ='irisData/testData.data',
                       training_labels='irisData/trainLabels.data',
                       sample_labels ='irisData/testLabels.data'):
        self.trainingDataSetFile = csv.reader(open(training_data_set))
        self.trainingDataSet = []
        self.sampleSetFile = csv.reader(open(sample_set))
        self.sampleSet = []
        self.trainingLabelsFile = csv.reader(open(training_labels))
        self.trainingLabels = []
        self.sampleLabelsFile = csv.reader(open(sample_labels))
        self.sampleLabels = []
        if self.trainingDataSetFile is not None:
            self.storeData()

    def storeData(self):
        self.storeTrainingData()
        self.storeSampleData()

    def storeTrainingData(self):
        for row in self.trainingDataSetFile:
            for i in range(len(row)):
                row[i] = float(row[i].strip())
            self.trainingDataSet.append(row)
        for row in self.trainingLabelsFile:
            for i in range(len(row)):
                row[i] = int(row[i])
            self.trainingLabels.append(row[0])  # there is only 1 label

    def storeSampleData(self):
        for row in self.sampleSetFile:
            for i in range(len(row)):
                row[i] = float(row[i].strip())
            self.sampleSet.append(row)
        for row in self.sampleLabelsFile:
            for i in range(len(row)):
                row[i] = int(row[i])
            self.sampleLabels.append(row[0])

    def plotData(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for dataSet, markerType, color, size in [(self.trainingDataSet, 'o', 'b', 50), (self.sampleSet, '^', 'r', 150)]:
            ax.scatter(self.getDataPoints(dataSet, point=0),
                       self.getDataPoints(dataSet, point=1),
                       self.getDataPoints(dataSet, point=2),
                       s=size, c=color, marker=markerType)

        ax.set_xlabel('sepal length (cm)')
        ax.set_ylabel('sepal width (cm)')
        ax.set_zlabel('petal length (cm)')

        plt.show()

    @staticmethod
    def getDataPoints(data_set, point):
        data_points = []
        for row in data_set:
            data_points.append(row[point])
        return data_points

    def kNN(self, k=1):
        error = 'Starting error is never 0'
        while error != 0:
            result = []
            for sample in self.sampleSet:
                result.append(self._kNN(sample, k=k))

            error = self.getError(result)
            self.printResults(result, error, k)
            k += 1

    def _kNN(self, sample, k=1):
        distancePriorityQueue = Queue.PriorityQueue()
        sampleNumber = 0
        for test in self.trainingDataSet:
            distancePriorityQueue.put((self.getEuclideanDistance(sample, test), self.trainingLabels[sampleNumber]))
            sampleNumber += 1
        return self.bestNeighbor(distancePriorityQueue, k)

    def getEuclideanDistance(self, sample, test):
        return math.sqrt((sample[0]-test[0])**2 +
                         (sample[1]-test[1])**2 +
                         (sample[2]-test[2])**2 +
                         (sample[3]-test[3])**2)

    def bestNeighbor(self, neighbors, k):
        k_closest_neighbors = []
        for i in range(k):
            k_closest_neighbors.append(neighbors.queue[i][1])
        frequencyCounter = np.bincount(np.array(k_closest_neighbors))
        return np.argmax(frequencyCounter)  # return the most frequent neighbor

    def getError(self, results):
        error = 0
        for i in range(len(results)):
            if results[i] != self.sampleLabels[i]:
                error += 1
        return error

    def printResults(self, results, error, k):
        print 'with k =  ',
        print k
        print 'results = ',
        print results
        print 'samples = ',
        print self.sampleLabels
        print 'Error = ',
        print error
        print
x = KNN()
x.kNN(1)
x.plotData()



