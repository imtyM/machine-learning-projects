# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:53:24 2016

@author: Imtiaz Mukadam
"""
import googlemaps
import Queue
import copy
class TSP_tree:
    'TSP tree used for Assignment 1'
    __locationList = ['Locations for the TSP',
                       'University of Pretoria, Pretoria',
                       'CSIR, Meiring Naude Road, Pretoria',
                       'Armscor, Delmas Road, Pretoria',
                       'Nellmapius Dr, Centurion, 0157',#Denel Dynamics
                       'West Gate, Hans Strydom Drive, Lyttelton, Centurion, 0157']#Airforce Base
    __gmaps = googlemaps.Client(key='AIzaSyD9ZEWpoOWXniUFtMmQvSlOf2fOt_Th28I')
    __treeCreated = False
    __goal = 0
    __DFS_Visited = []
    __BFS_Visited = []
    __DFS_goalRoute = []
    __BFS_goalRoute = []
    __que = Queue.LifoQueue()
    class TSP_node:
        'Nodes that make up the TSP tree structure'
        def __init__(self,cost=0,parent=None,location=0,children=[],route=[],isRoot = False,isLeaf = False):
            self.cost = cost
            self.parent = parent
            self.location = location
            self.children = children
            self.route = route

            self.isRoot = isRoot
            self.isLeaf = isLeaf
        
        
        
    def __init__(self):
        self.head = TSP_tree.TSP_node(0,None,1,[],[1], True,False);
        self.costList = []
        self.DFS_Visited = []
        self.BFS_Visited = []
        
    """Main createTree Function"""    
    def createTSP_Tree(self):
        self.head = self.buildTree(self.head)
        self.__treeCreated = True
        self.__goal = self.getGoal()

               
    """ createTree Helper Functions"""
    def buildTree(self, node):
        """

        :param node: initially node is the root, then BuildTree is recursively called on children nodes
        :return: returns the root node again with tree attached.
        """
        if node.isLeaf == False:
          self.addChildren(node)
          for child in node.children:
            if child.isLeaf == False:
              self.buildTree(child)
        return node
    def addChildren(self,node):
        if node.isRoot == True:
          self.addRootChildren(node)
        else:
          self.addLeafChildren(node)
    
    def addRootChildren(self, node):
        i = 2
        temp = []
        for locations in self.__locationList:
            temp = TSP_tree.TSP_node(self.getCost(node.location,i),node,i,[1,i],False,False)
            i += 1
        node.children = temp
    def addLeafChildren(self,node):
        for sibling in node.parent.children:
          if sibling.location != node.location:
            node.children.append(TSP_tree.TSP_node(node.cost+self.getCost(node.location,sibling.location),
                                                   node,sibling.location,[],node.route+[sibling.location],
                                                   False,False))
          if len(node.parent.children) == 1 :
            node.children.append(TSP_tree.TSP_node(node.cost+self.getCost(node.location,1),
                                                   node,1,[],node.route+[1],
                                                   False,True)) #back to UP
            self.costList.append(node.children[0].cost)
            print (node.children[0].route)
    
    def getCost(self,locationA,locationB):
      directions_result = self.__gmaps.distance_matrix(self.__locationList[locationA],
                                                    self.__locationList[locationB])
      return directions_result['rows'][0]['elements'][0]['distance']['value']
    def getGoal(self):
      return min(self.costList)

   
    """Main recursive DFS Function"""
    def DFS(self):
      if not self.__treeCreated:
        print ('There is no tree to search. Call createTSP_Tree().')
        return
      else:
        self.head = self.__DFS(self.head);
        self.__PrintDFS()
    """Helper DFS Function"""
    def __DFS(self,node):
      self.DFS_Visit(node)
      if node.cost != self.__goal:        
        for child in node.children:
           if child.isLeaf == False:
             self.__DFS(child)
           else:
             self.DFS_Visit(child)
      return node
    def DFS_Visit(self,node):
      self.__DFS_Visited.append(node.location)
      if node.cost == self.__goal:
        print ('DFS Nodes Visited: \n %r' %(self.__DFS_Visited))
        self.__DFS_goalRoute = node.route
        self.DFS_Visited = copy.copy(self.__DFS_Visited)
      return
    def __PrintDFS(self):
      for route in self.__DFS_goalRoute:
        print( 'Goal Found with route: \n ( %r ) %r -->' % (route , self.__locationList[route]))
        print (' Problem solved.')
