import AlphaBeta

class Game:

    def __init__(self, board=[], currentPlayer='X'):
        self.currentPlayer = currentPlayer
        if not len(board) == 9:
            self.board = [None for i in range(9)]
        else:
            self.board = board
        self.players = ('X', 'O')
        self.finishers = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6])

    def actions(self):
        actions = []
        for i in range(len(self.board)):
            if self.board[i] is None:
                actions.append(i)
        return actions

    def playerMoves(self, player):
        playermoves = []
        for i in range(len(self.board)):
            if self.board[i] == player:
                playermoves.append(i)
        return playermoves

    def move(self, position):
        self.board[position] = self.currentPlayer
        self.turn()

    def turn(self):
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        elif self.currentPlayer == 'O':
            self.currentPlayer = 'X'

    def isGameOver(self):
        if len(self.actions()) == 0 or self.findWinner() is not None:
            return True
        return False

    def utility(self):
        if self.findWinner() == 'X':
            return -1
        elif self.findWinner() == 'O':
            return 1
        return 0

    def findWinner(self):
        for player in self.players:
            playerMoves = self.playerMoves(player)
            for finishers in self.finishers:
                winnerExists = True
                for eachMove in finishers:
                    if eachMove not in playerMoves:
                        winnerExists = False
                if winnerExists:
                    return player
        return None

    def player(self):
        if self.currentPlayer == 'X':
            return 'MIN'
        return 'MAX'

    def terminalTest(self):
        return self.isGameOver()

    def result(self, action):
        self.move(action)
        return self

    def duplicateState(self):
        return Game(self.board, self.currentPlayer)

    def printBoard(self):
        j = 0
        for row in [self.board[i:i + 3] for i in range(0, len(self.board), 3)]:
            print "|",
            for element in range(3):
                j += 1
                if row[element] is None:
                    print " ",
                    print j,
                    print " ",
                else:
                    print " ",
                    print row[element],
                    print " ",
            print "|"

    def startGame(self):
        while not self.isGameOver():
            self.printBoard()
            self.promptPlayer()
            self.move(int(raw_input()) - 1)
        self.printVictory()

    def promptPlayer(self):
        print "Player ",
        print self.currentPlayer,
        print ", make your move: "

    def printVictory(self):
        self.printBoard()
        print "Player ",
        print self.findWinner(),
        print "WINS! awe."


