import queue
import time
import resource
import sys
import math

#### SKELETON CODE ####

## The Class that Represents the Puzzle

class PuzzleState(object):
    """docstring for PuzzleState"""
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        if n*n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")

        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []
        self.manhattan_distance = 0
        self.action_value = 0

        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

        for i, item in enumerate(self.config):
            if item != 0:
                self.manhattan_distance += abs(i // self.n - item // self.n) + abs(i%self.n - item%self.n)

        if self.action == "Up":
            self.action_value = 0
        elif self.action == "Down":
            self.action_value = 1
        elif self.action == "Left":
            self.action_value = 2
        elif self.action == "Right":
            self.action_value = 3           

    def __lt__(self, other):
        selfcost = self.cost + self.manhattan_distance
        othercost = other.cost + other.manhattan_distance
        
        if selfcost < othercost:
            return True
        elif selfcost == othercost:
            return self.action_value < other.action_value
        else:
            return False

    def __gt__(self, other):
        selfcost = self.cost + self.manhattan_distance
        othercost = other.cost + other.manhattan_distance
        
        if selfcost > othercost:
            return True
        elif selfcost == othercost:
            return self.action_value > other.action_value
        else:
            return False
        
    def __eq__(self, other):
        selfcost = self.cost + self.manhattan_distance
        othercost = other.cost + other.manhattan_distance
        
        return selfcost == othercost and self.action_value == other.action_value
    
    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])

            print(line)
            
    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""
        # add child nodes in order of UDLR
        if len(self.children) == 0:

            up_child = self.move_up()
            if up_child is not None:
                self.children.append(up_child)

            down_child = self.move_down()
            if down_child is not None:
                self.children.append(down_child)

            left_child = self.move_left()
            if left_child is not None:
                self.children.append(left_child)

            right_child = self.move_right()
            if right_child is not None:
                self.children.append(right_child)

        return self.children


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def pathToGoal(state, path_to_goal):
    if state:
        pathToGoal(state.parent, path_to_goal)
        path_to_goal += [state.action]
    
    

def writeOutput(state, max_depth, expanded_node_count):
    ### Student Code Goes here
    f = open('output.txt', 'w')
    path_to_goal = []
    p = state
    while p.parent:
        path_to_goal.insert(0, p.action)
        p = p.parent
        
    f.write("path_to_goal: {}\n".format(path_to_goal))
    f.write("cost_of_path: {}\n".format(state.cost))
    f.write("nodes_expanded: {}\n".format(expanded_node_count))
    f.write("search_depth: {}\n".format(state.cost))
    f.write("max_search_depth: {}\n".format(max_depth))
    
    f.write("running_time: {:f}\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_utime
                                           + resource.getrusage(resource.RUSAGE_SELF).ru_stime))
    f.write("max_ram_usage: {:f}\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024)))
    

def bfs_search(initial_state):
    """BFS search"""

    d = {}
    d[initial_state.config] = True

    frontier = queue.Queue()
    frontier.put(initial_state)

    explored = set()
    goal_state = (0,1,2,3,4,5,6,7,8)
    expanded_node_count = 0
    max_depth = 0
    
    while not frontier.empty():
        state = frontier.get()
        max_depth = max(max_depth, state.cost)
        del d[state.config]
        
        explored.add(state.config)
        if goal_state == state.config:
            writeOutput(state, max_depth, expanded_node_count)
            return True

        state.expand()
        expanded_node_count += 1
        for neighbor in state.children:
            if neighbor.config not in d and neighbor.config not in explored:
                max_depth = max(max_depth, neighbor.cost)                
                frontier.put(neighbor)
                d[neighbor.config] = True


    return False

def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    d = {}
    d[initial_state.config] = True

    frontier = []
    frontier.append(initial_state)

    explored = set()
    goal_state = (0,1,2,3,4,5,6,7,8)
    expanded_node_count = 0
    max_depth = 0
    
    while frontier:
        state = frontier.pop()
        max_depth = max(max_depth, state.cost)
        del d[state.config]
        
        explored.add(state.config)
        if goal_state == state.config:
            writeOutput(state, max_depth, expanded_node_count)
            return True

        state.expand()
        expanded_node_count += 1
        for i in range(len(state.children)-1,-1,-1):
            neighbor = state.children[i]
            if neighbor.config not in d and neighbor.config not in explored:
                max_depth = max(max_depth, neighbor.cost)                
                frontier.append(neighbor)
                d[neighbor.config] = True


    return False

    
def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    d = {}
    d[initial_state.config] = True

    frontier = queue.PriorityQueue()
    #frontier.put(((initial_state.cost + initial_state.manhattan_distance),initial_state))
    frontier.put(initial_state)

    explored = set()
    goal_state = (0,1,2,3,4,5,6,7,8)
    expanded_node_count = 0
    max_depth = 0
    
    while frontier:
        state = frontier.get()
        max_depth = max(max_depth, state.cost)
        del d[state.config]
        
        explored.add(state.config)
        if goal_state == state.config:
            writeOutput(state, max_depth, expanded_node_count)
            return True

        state.expand()
        expanded_node_count += 1
        for neighbor in state.children:
            if neighbor.config not in d and neighbor.config not in explored:
                max_depth = max(max_depth, neighbor.cost) 
                #frontier.put(((neighbor.cost + neighbor.manhattan_distance),neighbor))
                frontier.put(neighbor)
                d[neighbor.config] = True


    return False
    

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""

    ### STUDENT CODE GOES HERE ###

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###

# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    sm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)
    hard_state.display()
    if sm == "bfs":
        bfs_search(hard_state)
    elif sm == "dfs":
        dfs_search(hard_state)
    elif sm == "ast":
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")

if __name__ == '__main__':
    main()

