# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:53:24 2016

@author: Imtiaz Mukadam
"""
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib
from random import randint

from matplotlib import cm
import Queue


class GeneticAlgorithm:

    def __init__(self):
        self.w = np.array([[9, 7, 1, 9, 8, 8, 2, 8, 9, 9, 8, 5, 3, 6, 9, 5],
                           [9, 2, 4, 9, 9, 0, 3, 8, 9, 8, 5, 3, 7, 8, 4, 7],
                           [4, 7, 8, 9, 0, 6, 0, 3, 8, 7, 4, 4, 7, 1, 2, 7],
                           [2, 2, 4, 0, 1, 7, 1, 8, 7, 1, 9, 3, 0, 4, 1, 2],
                           [0, 9, 0, 3, 3, 8, 1, 8, 9, 7, 7, 7, 8, 2, 2, 1],
                           [1, 1, 2, 1, 9, 5, 9, 9, 8, 5, 2, 5, 0, 5, 4, 9],
                           [9, 1, 0, 7, 2, 1, 0, 5, 8, 7, 3, 6, 7, 6, 1, 2],
                           [4, 0, 3, 8, 0, 4, 2, 6, 3, 2, 0, 8, 6, 1, 7, 9],
                           [1, 0, 1, 3, 3, 6, 7, 0, 4, 4, 0, 3, 8, 3, 4, 7],
                           [1, 7, 7, 0, 5, 7, 0, 1, 1, 5, 8, 3, 5, 1, 1, 0],
                           [3, 1, 2, 6, 7, 1, 8, 1, 4, 5, 2, 1, 9, 8, 3, 8],
                           [1, 3, 2, 7, 7, 6, 3, 0, 1, 3, 2, 6, 6, 2, 0, 8],
                           [6, 9, 4, 8, 1, 2, 5, 5, 0, 9, 2, 8, 7, 9, 4, 9],
                           [0, 7, 4, 3, 4, 4, 5, 2, 8, 7, 4, 6, 9, 5, 5, 3],
                           [9, 1, 8, 0, 7, 2, 2, 5, 5, 8, 3, 8, 4, 3, 7, 6],
                           [6, 0, 0, 5, 6, 0, 8, 1, 7, 4, 5, 0, 8, 8, 8, 7]])
        self.minCost = 100000
        self.minLocation = []
        self.numberOfGenerations = 10
        self.numberOfParents = 5
        self.mutationRate = 0.001

        self.GA_result = ()

    def getDistance(self, x_i, y_i, x_loc, y_loc):
        if self.inSameHalfOfMap(x_i, x_loc):
            return self.euclideanDistance(x_i, y_i, x_loc, y_loc)
        else:
            return self.findBridgedEuclideanDistance(x_i, y_i, x_loc, y_loc)

    def inSameHalfOfMap(self, x_i, x_loc):
        return (x_i < 8 and x_loc < 8) or (x_i > 7 and x_loc > 7)

    def euclideanDistance(self, x_i, y_i, x_loc, y_loc):
        x = x_i - x_loc
        y = y_i - y_loc
        return math.sqrt((x*x) + (y*y))

    def findBridgedEuclideanDistance(self, x_i, y_i, x_loc, y_loc):
        bridge_loc = self.findBridge(y_i)  # bridge_loc[0] is x & bridge_loc[1] is y
        offset = self.bridgeNeighborOffset(x_i)
        return self.euclideanDistance(x_i, y_i, bridge_loc[0], bridge_loc[1])\
            + self.euclideanDistance(bridge_loc[0] + offset, bridge_loc[1], x_loc, y_loc) \
            + self.euclideanDistance(bridge_loc[0], bridge_loc[1], bridge_loc[0]+offset, bridge_loc[1])

    def findBridge(self, y):
        if y < 6:
            return [7, 2]
        return [7, 9]

    def bridgeNeighborOffset(self,x):
        if x < 8:
            return 1
        return -1

    def costFunction(self, x, y):
        res = 0
        for i in range(16):
            for j in range(16):
                res += self.w[i][j] * self.getDistance(i, j, x, y)
        if res < self.minCost:
            self.minCost = res
            self.minLocation = [x, y]
        return res

    def plotCostFunction(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = y = np.arange(0, 16, 1)
        print x
        X, Y = np.meshgrid(x, y)
        zs = np.array([self.costFunction(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)

        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.RdGy,
                        linewidth=0, antialiased=False)

        ax.set_xlabel('X-Coordinate')
        ax.set_ylabel('Y-Coordinate')
        ax.set_zlabel('Cost')

        #plt.show()
        print self.minLocation

    def geneticAlgorithm(self):
        currentGen = self.initialGeneration()
        for i in range(self.numberOfGenerations):
            currentGen = self.performGeneticAlgorithm(currentGen)
        currentGen = self.getGenerationFitness(currentGen)
        self.GA_result = currentGen.get()
        self.printResults()

    def initialGeneration(self):
        initialGen = Queue.PriorityQueue()
        for i in range(50):
            initialGen.put((0,  self.randomChromosome()))
        return initialGen

    def randomChromosome(self):
        chromosome = []
        chromosome.append(self.getRandomBinary())
        chromosome.append(self.getRandomBinary())
        return chromosome

    def getRandomBinary(self):
        return '{0:04b}'.format(randint(0, 15))

    def performGeneticAlgorithm(self, currentGen):
        fittestChromosomes = []
        currentGen = self.getGenerationFitness(currentGen)

        for i in range(self.numberOfParents):
            fittestChromosomes.append(currentGen.get())

        return self.crossOver(fittestChromosomes)

    def getGenerationFitness(self, currentGen):
        for i in range(currentGen.qsize()):
            chromosome = currentGen.get()[1]
            currentGen.put((self.evaluateFitness(chromosome), chromosome))
        return currentGen

    def evaluateFitness(self, chromosome):
        x = int(chromosome[0], 2)
        y = int(chromosome[1], 2)
        return 2.5 + 4.4*self.getDistance(x, y, self.minLocation[0], self.minLocation[1])

    def crossOver(self, fitChromosomes):
        nextGen = Queue.PriorityQueue()
        for i in range(len(fitChromosomes)):
            nextGen.put((0, fitChromosomes[i][1]))
            for j in range(len(fitChromosomes)):
                if i != j:  # don't cross the same ones
                    nextGen.put((0, self.getCrossOver(fitChromosomes[i], fitChromosomes[j])))
                    nextGen.put((0, self.getCrossOver(fitChromosomes[j], fitChromosomes[i])))
        return nextGen

    def getCrossOver(self, chromosome_1, chromosome_2):
        chromosome = []
        if self.shouldMutate():
            chromosome.append(self.getRandomBinary())
        else:
            chromosome.append(chromosome_1[1][1])
        if self.shouldMutate():
            chromosome.append(self.getRandomBinary())
        else:
            chromosome.append(chromosome_2[1][1])
        return chromosome

    def shouldMutate(self):
        if randint(0, 100) <= self.mutationRate*100:
            return True
        return False

    def printResults(self):
        print "Goal location:",
        print self.minLocation
        print "Number of generations:",
        print self.numberOfGenerations
        print "Number of parents:",
        print self.numberOfParents
        print "Mutation rate:",
        print self.mutationRate*100,
        print "%"
        print "Optimal fitness: 2.5.\n"

        print "GA RESULTS"
        print "GA location found: [",
        print int(self.GA_result[1][0], 2),
        print ", ",
        print int(self.GA_result[1][1], 2),
        print " ]"
        print "GA goal chromosome fitness:"
        print self.GA_result[0]

x = GeneticAlgorithm()
x.plotCostFunction()
x.geneticAlgorithm()