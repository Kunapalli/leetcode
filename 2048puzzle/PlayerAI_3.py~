from random import randint
from BaseAI import BaseAI
 
class PlayerAI(BaseAI):
    def __init__(self):
        self.previous_max_score = 0
        self.previous_min_score = float('inf')
        
    def getMove(self, state):
        print("in PlayerAI::getMove ENTER")        
        #moves = grid.getAvailableMoves()
        #return moves[randint(0, len(moves) - 1)] if moves else None
        (child, _) = self.maximize(state, float('-inf'), float('inf'))
        print("in PlayerAI::getMove, child = ", child)
        return child

    
    def eval(self, state):
        free_cell_bonus = len(state.getAvailableCells()) * 10.0
        edge_bonus = 0
        m = max(max(state.map[1][1], state.map[1][2]), max(state.map[2][1], state.map[2][2]))
        for x,y in [(0,0), (0,1), (0,2), (0,3), (1,0), (1,3), (2,0), (2,3), (3,0), (3,1), (3,2), (3,3)]:
            for v in range(1,13,1):
                if state.map[x][y] > (2**v)*m:
                    edge_bonus += v

        total_score = free_cell_bonus + edge_bonus
        print("total_score = ", total_score)
        return total_score

    def maximize(self, state, alpha, beta):

        if alpha == float('-inf') and beta == float('inf'):
            pass
        else:
            score = self.eval(state)
            if score > 2*self.previous_max_score:
                self.previous_max_score = score
                return (0, alpha)

        (maxChild, maxUtility) = (None, float('-inf'))
        for dir in state.getAvailableMoves():
            print("**************************dir is ", dir)
            child = state.clone()
            if child.move(dir):
                (_, utility) = self.minimize(child, alpha, beta)
                
                if utility > maxUtility:
                    (maxChild, maxUtility) = (dir, utility)

                if maxUtility >= beta:
                    break

                if maxUtility > alpha:
                    alpha = maxUtility

        return (maxChild, maxUtility)


    def minimize(self, state, alpha, beta):

        score = self.eval(state)
        if score < self.previous_min_score:
            return (0, beta)

        (minChild, minUtility) = (None, float('inf'))
        for dir in state.getAvailableMoves():
            print("in minimize dir is ", dir)            
            child = state.clone()
            if child.move(dir):
                (_, utility) = self.maximize(child, alpha, beta)

            if utility < minUtility:
                (minChild, minUtility) = (dir, utility)

            if minUtility <= alpha:
                break

            if minUtility < beta:
                beta = minUtility

        return (minChild, minUtility)
