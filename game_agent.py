"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # For my function I've decided to implement a heuristic that aims to limit the number of moves your opponent can make while maximizing the optionality it creates for our player
    #For example if you have a situation where you give your opponent one legal move but give yourself four legal moves - this is advantageous. 
    # There are points where this won't matter at all. However in the endgame this will be particuarly advatangeous, and it's even possible to force end game faster by running this in the mid-game. 
    # The cases that we have to deal with involve divergent cases - one's in which you can wither give yourself high optionality or limit your opponents moves 
    # This can come up in a situation where you can either end the game by taking away an opponents last legal move OR giving yourself 4 legal moves. 

    # to deal with this we do a couple things. 

    #1 Anything that leaves our opponent with zero moves is the automatic best move

    #2 In any other case we want to score based on the optionality score that we have - minus our opponents 

    #3 in the case of situations where the score = zero or ties we will take the option that maximizes our optionality. 

     #   my_options = game.get_legal_moves()
     #   for move in my_options:
      #      ab_move 



    #opp_options =0
   #optionscore =  =myoptions -opp_options


    #Implementation 
    #Go through the legal moves for the opponent as they are in place




    # Go though the legal moves for ourselves at each new position 
    #Check how many legal moves they leave us with
    #Check how many legal moves each of them leaves our opponent with
    # store them 
    #evaluate and pick the move based on the rules we stated above. 
 # in order to check our moves we have to 








    # TODO: finish this function!
    raise NotImplementedError


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)  This parameter should be ignored when iterative = True.

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).  When True, search_depth should
        be ignored and no limit to search depth.

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************
               Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            DEPRECATED -- This argument will be removed in the next release

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left
        legal_moves = game.get_legal_moves()
        our_moves= legal_moves

        if not legal_moves:
            return(-1,-1)

        #I used our_moves to denote all the possible moves for all the functions below I am renaming to keep it consistent 


        # TODO: finish this function!
        depth =0
        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves

        # based on https://github.com/aimacode/aima-pseudocode/blob/master/md/Iterative-Deepening-Search.md
        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            
            #because this try block should return before time runs out 
            # I only have to do two things 1.) Write an infinite loop as it will run until time runs out
            # make sure that I only take the results from a completed depth level 

            while (0>1):
                depth = 0
                while depth < float(inf):
                    ab_move =self.minimax()
                    depth+1


                    return ab_move

            

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return ab_move

    def minimax(self, game, depth, maximizing_player=True):
        
      #  depth ==1

      #depth =n

       # puggle=[]      
        # The way that I look at this problem is that we have to basic building blocks that we have to do in order to get this to work
        # Minimax is how we are telling our computer player what the best move is
        # Alpha beta makes the above more efficient. 

        #I used the pseudocode at https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md to build this
       # as given to us in the readme file 



    #Start by having the time constraint that was implemented for us at the start. 

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        def max_value(self,game):
    
         # the args self, game represent the current state again following the pseudocode
            if game.move_count >= depth+2: 
                return self.score(game,self) # if your in the terminal case return
                v=0 
            v=float("-inf")
    #setting v = to negative infinity
            our_moves = game.get_legal_moves()
    # get all the legal moves
            for move in our_moves:
               #our_move = puggle
                v=max(v,float(min_value(self,game.forecast_move(move))))    
            return v
    # For every move take the max_value of the branches we have. 
    #print (puggle) 



        def min_value(self,game):
        
    # the args self, game represent the current state again following the pseudocode
            if game.move_count >= depth+2: 
                return self.score(game,self) # if your in the terminal case return
                v=0
            v=float("inf")
    #setting v = to  infinity
            our_moves = game.get_legal_moves()
    # get all the legal moves
            #print ('alaklsflfsdfhd',our_moves)
            for move in our_moves:
                v=min(v,float(max_value(self,game.forecast_move(move))))    
            return v

        # For every move take the min_value of the branches we have. 


    #dealing with the case where we don't have legal moves. 
        our_moves = game.get_legal_moves(self)
        if not our_moves:
            return 0
            #return null - doesn't work 



#declare these variables I set ab_score equal to negative infinity to make sure that unless it's the worst case scenario we don't return the base case 
#using a zerou would be bad

        ab_score = float("-inf")
        ab_move =0
# now we have to deal with the first part of our pseudo code returning

#The notation argmax a ∈ S f(a) computes the element a of set S that has maximum value of f(a).

        for move in our_moves:
            score = min_value(self,game.forecast_move(move))
            if score >ab_score:
                ab_score =score
              # print('alkjdk',ab_score)

                ab_move=move
                 # print('IOWEUOIWUEOIE',ab_move)
        return ab_score,ab_move







        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        

        # TODO: finish this function!
       # raise NotImplementedError




    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
       
        n=2
        #idea is to implement alpha beta pruning - to make our minmax clearer. 







        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()
            v=0
            # take a max value but we're using alpha beta to make the decisions 
        def max_value(self,game,alpha,beta):
            
            if game.move_count >= depth+n:
                return self.score(game,self)
                    
            v = float("-inf")
            our_moves = game.get_legal_moves()
            for move in our_moves:
                print (our_moves)
                v = max(v,min_value(self,game.forecast_move(move),alpha,beta))
                if v >= beta:
                    return v
                alpha = max(alpha,v)
            return v
                        # take a min value but we're using alpha beta to make the decisions 

        def min_value(self,game,alpha,beta):
        
            if game.move_count >= depth+n:
                return self.score(game,self)
            v = float("inf")
            our_moves = game.get_legal_moves()
            for move in our_moves:
                print (our_moves)
                v = min(v,max_value(self,game.forecast_move(move),alpha,beta))
                if v <= alpha:
                    return v
                beta = min(beta,v)
            return v
            
        our_moves = game.get_legal_moves(self)
        #print ( 'akdjlksjs',our_moves)
        if not our_moves:
            return 0
    
        ab_score = float("-inf")
        ab_move = 0
    
        for move in our_moves:
            score = min_value(self,game.forecast_move(move),alpha,beta)
            
            if score >= beta:
                return score
            alpha = max(alpha,score)
            #print ('frustration')
            if score > ab_score:
                ab_score=score
                print(' AB SCORE AB SCORE AB SCORE',ab_move)
                ab_move=move
                print(' AB SCORE AB SCORE AB SCORE',ab_move)
        return ab_score, ab_move




        # TODO: finish this function!
        #raise NotImplementedError
