# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:53:24 2016

@author: Imtiaz Mukadam
"""


class Map:
    """Map class to just hold information about the state
       State information is based on input parameters to
       class methods. Parameters will be location of state """
    def __init__(self):
        self.___defaultMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
                              [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                              [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                              [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                              [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                              [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def visit(self, state):
        self.___defaultMap[state[0]][state[1]] = 8

    def getAllMoves(self, state):
        moves = [[state[0]+1, state[1]],
                 [state[0]-1, state[1]],
                 [state[0], state[1]+1],
                 [state[0], state[1]-1],
                 [state[0]+1, state[1]+1],
                 [state[0]+1, state[1]-1],
                 [state[0]-1, state[1]+1],
                 [state[0]-1, state[1]-1]]
        moves = self.__validateMoves(moves)
        return moves

    def getSideMoves(self, state):
        moves = [[state[0]+1, state[1]],
                 [state[0]-1, state[1]],
                 [state[0], state[1]+1],
                 [state[0], state[1]-1]]
        moves = self.__validateMoves(moves)
        return moves

    def getDiagonalMoves(self, state):
        moves = [[state[0]+1, state[1]+1],
                 [state[0]+1, state[1]-1],
                 [state[0]-1, state[1]+1],
                 [state[0]-1, state[1]-1]]
        moves = self.__validateMoves(moves)
        return moves

    def __validateMoves(self, moves):
        invalidMoves = []
        for state in moves:
            if self.__stateIsInvalid(state) or self.__stateIsBlocked(state):
                invalidMoves.append(state)
        return self.__removeInvalidMoves(moves, invalidMoves)

    def __removeInvalidMoves(self, moves, invalidMoves):
        for removables in invalidMoves:
            moves.remove(removables)
        return moves

    def __stateIsInvalid(self, state):
        if state[0] > 11 or state[0] < 0 or state[1] > 11 or state[1] < 0:
            return True
        else:
            return False

    def __stateIsBlocked(self, state):
        if self.___defaultMap[state[0]][state[1]] == 1 or self.___defaultMap[state[0]][state[1]] == 8:
            return True
        else:
            return False

    def getMap(self):
        return self.___defaultMap

    def toggleWall(self):
        self.___defaultMap[7][0] = 1