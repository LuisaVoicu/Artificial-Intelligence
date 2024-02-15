# multiAgents.py

# --------------

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





from util import manhattanDistance

from game import Directions

import random, util



from game import Agent

from pacman import GameState



class ReflexAgent(Agent):

    """

    A reflex agent chooses an action at each choice point by examining

    its alternatives via a state evaluation function.



    The code below is provided as a guide.  You are welcome to change

    it in any way you see fit, so long as you don't touch our method

    headers.

    """





    def getAction(self, gameState: GameState):

        """

        You do not need to change this method, but you're welcome to.



        getAction chooses among the best options according to the evaluation function.



        Just like in the previous project, getAction takes a GameState and returns

        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}

        """

        # Collect legal moves and successor states

        legalMoves = gameState.getLegalActions()



        # Choose one of the best actions

        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]

        bestScore = max(scores)

        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]

        chosenIndex = random.choice(bestIndices) # Pick randomly among the best



        "Add more of your code here if you want to"



        return legalMoves[chosenIndex]



    def evaluationFunction(self, currentGameState: GameState, action):

        """

        Design a better evaluation function here.



        The evaluation function takes in the current and proposed successor

        GameStates (pacman.py) and returns a number, where higher numbers are better.



        The code below extracts some useful information from the state, like the

        remaining food (newFood) and Pacman position after moving (newPos).

        newScaredTimes holds the number of moves that each ghost will remain

        scared because of Pacman having eaten a power pellet.



        Print out these variables to see what you're getting, then combine them

        to create a masterful evaluation function.

        """

        # Useful information you can extract from a GameState (pacman.py)

        successorGameState = currentGameState.generatePacmanSuccessor(action)

        newPos = successorGameState.getPacmanPosition()

        newFood = successorGameState.getFood().asList() # facem lista din matrice pt a parcurge mai usor

        newGhostStates = successorGameState.getGhostStates()

        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        

        "*** YOUR CODE HERE ***"



        # print("--> new Food:\n", newFood)

        # print("\n--> nre Ghost State:", newGhostStates)

        # print("\n--> new Scared Times:", newScaredTimes)



        

        ghostPos = successorGameState.getGhostPositions()

        

        #iau mai intai mancarea cea mai apropiata 



        min_dist_food = 1000000

        new_pacman_pos = newPos

        for food_pos in newFood:

            dist_food = util.manhattanDistance(newPos, food_pos)

            # min_dist_food = min(min_dist_food, dist_food)

            if dist_food < min_dist_food:

                min_dist_food = dist_food

                new_pacman_pos = food_pos

            

        #unde sunt fantomele? daca langa mancarea cea mai apropiata se afla o fantoma, renunt sa mai merg spre acea mancare

        for ghost_pos in ghostPos:

              if new_pacman_pos == ghost_pos:

                return -999999



        return successorGameState.getScore() + 1.0/min_dist_food





def scoreEvaluationFunction(currentGameState: GameState):

    """

    This default evaluation function just returns the score of the state.

    The score is the same one displayed in the Pacman GUI.



    This evaluation function is meant for use with adversarial search agents

    (not reflex agents).

    """

    return currentGameState.getScore()



class MultiAgentSearchAgent(Agent):

    """

    This class provides some common elements to all of your

    multi-agent searchers.  Any methods defined here will be available

    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.



    You *do not* need to make any changes here, but you can if you want to

    add functionality to all your adversarial search agents.  Please do not

    remove anything, however.



    Note: this is an abstract class: one that should not be instantiated.  It's

    only partially specified, and designed to be extended.  Agent (game.py)

    is another abstract class.

    """



    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):

        self.index = 0 # Pacman is always agent index 0

        self.evaluationFunction = util.lookup(evalFn, globals())

        self.depth = int(depth)



class MinimaxAgent(MultiAgentSearchAgent):

    """

    Your minimax agent (question 2)

    """



    def getAction(self, gameState: GameState):

        """

        Returns the minimax action from the current gameState using self.depth

        and self.evaluationFunction.



        Here are some method calls that might be useful when implementing minimax.



        gameState.getLegalActions(agentIndex):

        Returns a list of legal actions for an agent

        agentIndex=0 means Pacman, ghosts are >= 1



        gameState.generateSuccessor(agentIndex, action):

        Returns the successor game state after an agent takes an action



        gameState.getNumAgents():

        Returns the total number of agents in the game



        gameState.isWin():

        Returns whether or not the game state is a winning state



        gameState.isLose():

        Returns whether or not the game state is a losing state

        """

        "*** YOUR CODE HERE ***"



        self.nb_agents = gameState.getNumAgents()



        return self.minimax(gameState, self.depth, 0)[0]

    

    def minimax(self, gameState, minimax_depth, agent_index):



        # functie ce determina al cui rand e : pacman sau ghost?

        # ma voi opri doar cand castig/pierd/am evaluat tot arborele bottom-up



        # se va returna  tupla (action, value) , unde action reprezinta actiunea 

        # decisa ce determina cea mai buna optiune pentru pacman



        if gameState.isWin() or gameState.isLose() or minimax_depth == 0:

            return("" , self.evaluationFunction(gameState))



        if agent_index == 0:

            return self.max_pacman(gameState, minimax_depth, agent_index)

        else:

            return self.min_ghost(gameState, minimax_depth, agent_index)





    def max_pacman(self, state, depth, index):

        





        next_index = (index + 1) % self.nb_agents

        max_value = -100000000

        action_max = ""

        

        # pentru fiecare state verific daca selfEvaluation e maxim

        for action in state.getLegalActions(index):

            successor = state.generateSuccessor(index,action)

            value = self.minimax(successor, depth , next_index)[1] # ma intereseaza doar valoarea de la ghost, nu si actiunea



            if value > max_value:

                max_value = value

                action_max = action

        

        return (action_max, max_value)

    

    

    def min_ghost(self, state, depth, index):

        

        actions = state.getLegalActions(index)

        next_index = (index + 1) % self.nb_agents

        min_value = 100000000

        action_min = ""



        # se procedeaza similar ca la max_pacman

        # doar ca acum daca urmeaza randul pacman-ului depth-ul va scadea

        # vom avea atatea depth-uri cati agenti de ghost

        

        for action in actions:

            successor = state.generateSuccessor(index,action)

            

            if next_index == 0:

                value = self.minimax(successor, depth - 1, next_index)[1]



            else:

                value = self.minimax(successor, depth , next_index)[1]

            if value < min_value:

                min_value = value

                action_min = action

        return (action_min, min_value)













class AlphaBetaAgent(MultiAgentSearchAgent):

    """

    Your minimax agent with alpha-beta pruning (question 3)

    """



    def getAction(self, gameState: GameState):

        """

        Returns the minimax action using self.depth and self.evaluationFunction

        """

        "*** YOUR CODE HERE ***"

        self.nb_agents = gameState.getNumAgents()

        return self.minimax(gameState, self.depth, 0,-100000000,100000000)[0]

    

    def minimax(self, gameState, minimax_depth, agent_index, alpha, beta,):



        if gameState.isWin() or gameState.isLose() or minimax_depth == 0:

            return "" , self.evaluationFunction(gameState)



        if agent_index == 0:

            return self.max_pacman(gameState, minimax_depth, agent_index,alpha,beta)

        else:

            return self.min_ghost(gameState, minimax_depth, agent_index,alpha,beta)





    def max_pacman(self, state, depth, index, alpha, beta):



        next_index = (index + 1) % self.nb_agents

        max_value = -100000000

        action_max = ""

        for action in state.getLegalActions(index):

            successor = state.generateSuccessor(index,action)

            value = self.minimax(successor, depth , next_index,alpha,beta)[1] # ma intereseaza doar valoarea de la ghost, nu si actiunea



            if value > beta:

                return (action, value)

            

            if value > max_value:

                max_value = value

                action_max = action

        

            if alpha < max_value:

                alpha = max_value



        return (action_max, max_value)

    

    

    def min_ghost(self, state, depth, index, alpha, beta):

        

        actions = state.getLegalActions(index)

        next_index = (index + 1) % self.nb_agents

        min_value = 100000000

        action_min = ""

        for action in actions:

            successor = state.generateSuccessor(index,action)

            

            if next_index == 0:

                value = self.minimax(successor, depth - 1, next_index, alpha, beta)[1]



            else:

                value = self.minimax(successor, depth , next_index, alpha, beta)[1]



            if value < alpha:

                return (action, value)



            if value < min_value:

                min_value = value

                action_min = action

                    

            if beta > min_value:

                beta = min_value



        return (action_min, min_value)







class ExpectimaxAgent(MultiAgentSearchAgent):

    """

      Your expectimax agent (question 4)

    """



    def getAction(self, gameState: GameState):

        """

        Returns the expectimax action using self.depth and self.evaluationFunction



        All ghosts should be modeled as choosing uniformly at random from their

        legal moves.

        """

        "*** YOUR CODE HERE ***"

        util.raiseNotDefined()



def betterEvaluationFunction(currentGameState: GameState):

    """

    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable

    evaluation function (question 5).



    DESCRIPTION: <write something here so we know what you did>

    """

    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()



# Abbreviation

better = betterEvaluationFunction

