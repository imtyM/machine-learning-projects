class AlphaBeta:

    @staticmethod
    def minimax(game, player):
        game.printBoard()
        if game.isGameOver():
            print "Terminal with utility: ",
            print game.utility(),
        print

        finalMoveScore = 0
        if game.terminalTest():
            return game.utility()

        for actions in game.actions():
            proposedMove = AlphaBeta.minimax(game.result(actions), game.player())

            if player == 'MAX' and proposedMove > finalMoveScore:
                finalMoveScore = proposedMove
            elif player == 'MIN' and proposedMove < finalMoveScore:
                finalMoveScore = proposedMove
        return finalMoveScore

