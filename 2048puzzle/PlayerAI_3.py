from random import randint
from BaseAI import BaseAI
import time
import Grid_3
import math

def terminal(state):
    return not state.canMove()


def getChild(state, dir):
    t = state.clone()
    moved = t.move(dir)
    return (t, moved)


def children(state):
    c = []
    for dir in state.getAvailableMoves():
        (child, moved) = getChild(state, dir)
        if moved:
            c.append((child,dir))
    return c

 
class PlayerAI(BaseAI):
    def __init__(self):
        self.previous_max_score = 0
        self.previous_min_score = float('inf')
        self.available_cells = 14
        
    def getMove(self, state):
        start = time.process_time()
        limit = 4
        (dir, utility) = self.maximize(state, float('-inf'), float('inf'), limit, start)
        return dir

    def emptyness(self, state):
        return (len(state.getAvailableCells())/16.0)* 100

    def smoothness(self, state):
        u2 = 0
        for i in range(state.size):
            for j in range(state.size - 1):
                if state.map[i][j] == state.map[i][j+1]:
                    u2 += 1

        for j in range(state.size):
            for i in range(state.size - 1):
                if state.map[i][j] == state.map[i+1][j]:
                    u2 += 1

        return (u2/16.0)*100.0


    def edge_bonus(self, state):
        e = 0
        m = max(max(state.map[1][1], state.map[1][2]), max(state.map[2][1], state.map[2][2]))
        for x,y in [(0,0), (0,1), (0,2), (0,3), (1,0), (1,3), (2,0), (2,3), (3,0), (3,1), (3,2), (3,3)]:
            for v in range(1,13,1):
                if state.map[x][y] > (2**v)*m:
                    e += v
                    break

        return e
                    

    def monotonicity(self, state):
        m = 0
        a1 = True
        a2 = True
        for i in range(state.size):
            a1 = a1 and (state.map[i][0] <= state.map[i][1] <= state.map[i][2] <= state.map[i][3])
            a2 = a2 and (state.map[i][0] >= state.map[i][1] >= state.map[i][2] >= state.map[i][3])

        if a1 or a2:
            m += 10
            
        a3 = True
        a4 = True            
        for j in range(state.size):
            a3 = a4 and (state.map[0][j] <= state.map[1][j] <= state.map[2][j] <= state.map[j][3])
            a4 = a4 and (state.map[0][j] >= state.map[1][j] >= state.map[2][j] >= state.map[j][3])

        if a3 or a4:
            m += 10
            
        if (a1 and a4) or (a1 and a3) or (a2 and a4) or (a2 and a3):
            m += 10

        return (m/40.0)*100
                

    def max_weight(self, state):
        return (state.getMaxTile()/32768)*100.0

    def eval(self, state):
        h1 = self.emptyness(state)
        h2 = self.smoothness(state)
        h3 = self.edge_bonus(state)
        h4 = self.monotonicity(state)
        h5 = math.log(self.max_weight(state),2)
        
        return (0, 3*h1 + h2 + h4 + h5) # 1024, 512, 256, 128

    def maximize(self, state, alpha, beta, depth, start):

        if terminal(state) or depth == 0 or (time.process_time() - start > 0.195):
            return self.eval(state)
                
        (maxDir, maxUtility) = (None, float('-inf'))

        for (child,dir) in children(state):
            (_,utility) = self.minimize(child, alpha, beta, depth-1, start)
            
            if utility > maxUtility:
                (maxDir, maxUtility) = (dir, utility)

            if maxUtility >= beta:
                break
            
            if maxUtility > alpha:
                alpha = maxUtility

        return (maxDir, maxUtility)

    
    def minimize(self, state, alpha, beta, depth, start):
        if terminal(state) or depth == 0 or (time.process_time() - start > 0.195):
            return self.eval(state)

        (minDir, minUtility) = (None, float('inf'))
        
        L = state.getAvailableCells()
        children = []
        
        for pos in L:
            grid2 = state.clone()
            grid4 = state.clone()
            grid2.insertTile(pos,2)
            grid4.insertTile(pos,2)
            children.append(grid2)
            children.append(grid4)
            
        for child in children:
            (_, utility) = self.maximize(child, alpha, beta, depth-1, start)
            
            if utility < minUtility:
                minUtility = utility

            if minUtility <= alpha:
                break

            if minUtility < beta:
                beta = minUtility

        return (0, minUtility)
