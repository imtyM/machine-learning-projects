# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:53:24 2016

@author: Imty
"""
import Queue
import Map
import math


class Maze:
    """Maze class with various search methods"""
    __uniformGoal = None
    __uniformNumberOfNodesVisited = 0
    __uniformMap = None

    __greedyMap = None
    __GreedyGoal = None
    __greedyNumberOfNodesVisited = 0

    __A_starMap = None
    __A_StarGoal = None
    __A_StarNumberOfNodesVisited = 0

    class Node:
        """Node class specific to the class Maze"""
        def __init__(self, state=[0, 0], cost=0, path=[[0, 0]]):
            self.state = state
            self.cost = cost
            self.path = path

    def __init__(self):
        self.map = Map.Map()
        self.head = Maze.Node()

        self.que = Queue.PriorityQueue()
        self.que.put((self.head.cost, self.head))

    def uniformSearch(self):
        self.__resetTree()
        while self.que:
            self.__peruseUniform(self.que.get()[1])  # extract low priority node
        self.printUniform()

    """Uniform Search helpers"""
    def __peruseUniform(self, node):
        self.__uniformNumberOfNodesVisited += 1
        if self.__isGoal(node):
            self.__uniformGoal = node
            self.__uniformMap = self.map.getMap()
            self.__stopSearch()
        else:
            self.__expandTreeUniformly(node)

    def __expandTreeUniformly(self, node):  # Only g(n)
        for childState in self.map.getSideMoves(node.state):
            self.__addChildrenToQue(childState, node, 1)
        for childState in self.map.getDiagonalMoves(node.state):
            self.__addChildrenToQue(childState, node, math.sqrt(2))

    def greedySearch(self):
        self.__resetTree()
        while self.que:
            self.__peruseGreedy(self.que.get()[1])
        self.printGreedy()

    """Greedy search helpers"""
    def __peruseGreedy(self, node):
        self.__greedyNumberOfNodesVisited += 1
        if self.__isGoal(node):
            self.__GreedyGoal = node
            self.__greedyMap = self.map.getMap()
            self.__stopSearch()
        else:
            self.__expandTreeGreedy(node)

    def __expandTreeGreedy(self, node):  # only h(n)
        for childState in self.map.getAllMoves(node.state):
            self.__addChildrenToQue(childState, node, self.__getHueristic(childState))

    def __getHueristic(self, state):
        x = state[0] - 9
        y = state[1] - 9
        return math.sqrt((x*x)+(y*y))

    def A_starSearch(self):
        self.__resetTree()
        while self.que:
            self.__peruseStar(self.que.get()[1])
        self.printA_Star()

    def __peruseStar(self,node):
        self.__A_StarNumberOfNodesVisited += 1
        if self.__isGoal(node):
            self.__A_StarGoal = node
            self.__A_starMap = self.map.getMap()
            self.__stopSearch()
        else:
            self.__expandTreeStar(node)

    def __expandTreeStar(self, node):  # both g(n) and h(n) as costs
        for childState in self.map.getSideMoves(node.state):
            self.__addChildrenToQue(childState, node, 1 + self.__getHueristic(childState))
        for childState in self.map.getDiagonalMoves(node.state):
            self.__addChildrenToQue(childState, node, math.sqrt(2) + self.__getHueristic(childState))

    def __addChildrenToQue(self, state, node, cost):
        self.que.put((node.cost+cost, Maze.Node(state, node.cost+cost, node.path+[state])))

    def __isGoal(self, node):
        self.map.visit(node.state)
        if node.state == [9, 9]:
            return True
        else:
            return False

    def __stopSearch(self):
        self.que = []

    def printUniform(self):
        print "Uniform search complete.\n Total cost for Uniform Search:",
        print self.__uniformGoal.cost
        print "Number of nodes visited:",
        print self.__uniformNumberOfNodesVisited
        print "Path to goal node:",
        print self.__uniformGoal.path
        print "number of nodes in path:",
        print len(self.__uniformGoal.path)

    def printGreedy(self):
        print "Greedy search complete.\n Total cost for Uniform Search:",
        print self.__GreedyGoal.cost
        print "Number of nodes visited:",
        print self.__greedyNumberOfNodesVisited
        print "Path to goal node:",
        print self.__GreedyGoal.path
        print "number of nodes in path:",
        print len(self.__GreedyGoal.path)

    def printA_Star(self):
        print "A* search complete.\n Total cost for Uniform Search:",
        print self.__A_StarGoal.cost
        print "Number of nodes visited:",
        print self.__A_StarNumberOfNodesVisited
        print "Path to goal node:",
        print self.__A_StarGoal.path
        print "number of nodes in path:",
        print len(self.__A_StarGoal.path)

    def __resetTree(self):
        self.que = None
        self.que = Queue.PriorityQueue()
        self.que.put((self.head.cost, self.head))

        self.map = None
        self.map = Map.Map()

    def toggleWall(self):
        self.map.toggleWall()


