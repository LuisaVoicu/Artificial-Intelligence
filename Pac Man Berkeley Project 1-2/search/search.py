# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem): # in loc de self,.. 
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # de ce nu recursiv? pentru ca e nevoie ca algoritmul sa returneze o lista de actiuni
    
    start_state = problem.getStartState()
    explored_nodes = []
    stack = util.Stack() #frontiera
    stack.push((start_state,[]))

    #  getsuccessors:  problem.getSucessors(current_state) => (successors, actions, stepCost) -> mai usor la pop
    # print("DFS:")
    # print("Start State: ", start_state)
    # print("Goal State: ", problem.isGoalState)


    while stack.isEmpty() == False :
        (current_state, actions) = stack.pop()
        explored_nodes.append(current_state)

        if problem.isGoalState(current_state) :
            return actions
            
        next_move  = problem.getSuccessors(current_state)
        for (successor, action, _) in next_move:
            if (successor in explored_nodes)==False :
                actions_copy = actions.copy()
                actions_copy.append(action)
                stack.push((successor,actions_copy))
    
    return [] # no goal found


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()
    explored_nodes = [start_state] # echivalent cu visited[] 
    queue = util.Queue() #frontiera
    queue.push((start_state,[]))

    #  getsuccessors:  problem.getSucessors(current_state) => (successors, actions, stepCost) -> mai usor la pop
    # print("BFS:")
    # print("Start State: ", start_state)
    # print("Goal State: ", problem.isGoalState)

    # in frointiera tin tupla cu state-ul curent si lista cu actiunile facute pentru a ajunge in acel state

    while queue.isEmpty() == False:
        (current_state, actions) = queue.pop()

        if problem.isGoalState(current_state) == True:
            return actions

        next_move = problem.getSuccessors(current_state)
        
        
        for (successor, action, _) in next_move:
            if (successor in explored_nodes) == False :
                explored_nodes.append(successor)
                actions_copy = actions.copy() # altfel se va modifica lista initiala!! --> se pun modificarile si celorlalti successori
                actions_copy.append(action)
                queue.push((successor, actions_copy))

                # Problem: daca imbunatatesc BFS expanded_states va omite o stare 
                # ***     student solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
                # ***     student expanded_states:        ['A', 'B1', 'C', 'B2', 'D', 'E1', 'F']
                # *** 
                # ***     correct solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
                # ***     correct expanded_states:        ['A', 'B1', 'C', 'B2', 'D', 'E1', 'F', 'E2']
                
                # if problem.isGoalState(successor): # imbunatatire bfs 
                #     return actions_copy

    return [] # no goal found
               


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()

    explored_nodes = {} # set de tip explored_nodes[state] = cost
    explored_nodes[start_state] = 0 

    priority_queue = util.PriorityQueue() # (item,priority) , unde priority e euristica(???)!!
    priority_queue.push((start_state,[],0),0) # (current_state, actions, currenct_cost)

    while priority_queue.isEmpty() == False :
        (current_state, actions, current_cost) = priority_queue.pop()
        
        # am gasit goal state
        if problem.isGoalState(current_state) == True:
            return actions

        next_move = problem.getSuccessors(current_state)

        for (successor, action, cost) in next_move:
            calculate_cost = cost + current_cost

            if (successor in explored_nodes) == False or explored_nodes[successor] > calculate_cost:                      #problem: nu pot retine costul curent in .getSuccessors --> update metoda pentru explore_nodes fata de bfs/dfs ---> folosesc set
                explored_nodes[successor] = calculate_cost
                actions_copy = actions.copy() # altfel se vor pun toate la un loc
                actions_copy.append(action)
                priority_queue.push((successor, actions_copy, explored_nodes[successor]), explored_nodes[successor])
                            
  

def nullHeuristic(state,  problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    start_state = problem.getStartState()

    explored_nodes = []
    explored_nodes.append((start_state,0))
 
    priority_queue = util.PriorityQueue()
    priority = heuristic(start_state, problem) #calculam costul de la nodul curent la GoalState
    priority_queue.push((start_state,[],0), priority)

    while priority_queue.isEmpty() == False :
        (current_state, actions, current_cost) = priority_queue.pop()

        if problem.isGoalState(current_state) == True:
            return actions
        
        next_move = problem.getSuccessors(current_state)
        for (successor,action, cost) in next_move:
            calculate_cost = cost + current_cost

            #verificam daca nu cumva nodurile exploraje deja pot obtine un path mai scurt
                            # folosindu-ne de state-ul curent ca intermediat
            update_exploration = True
            for (explored, cost) in explored_nodes:
                if successor == explored and calculate_cost >= cost:
                    update_exploration = False
            
            if update_exploration :
                actions_copy = actions.copy()
                actions_copy.append(action)
                priority = calculate_cost + heuristic(successor, problem)
                priority_queue.push((successor,actions_copy,calculate_cost), priority)
                explored_nodes.append((successor,calculate_cost))



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


