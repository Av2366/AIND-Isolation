"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

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

    
    return float(len(game.get_legal_moves(player)))



    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    #raise NotImplementedError
    # if there are less than 3 legal moves left the branching factor isn't that high so we can
    # try to see how each of them positions us. 
    #inpsired by how Deep Blue and an endbook for less than five pieces on the table. 

    #legal_moves = (game.get_legal_moves())

     #   if len(legal_moves)>2:
      #      return (-1,-1)
       # else:
        #    for move in legal_moves 
         #       new_game = game.forecast_move((legalmoves[move]))
          #      assert(new_game.to_string() != game.to_string())
           #     print("\nOld state:\n{}".format(game.to_string()))
            #    print("\nNew state:\n{}".format(new_game.to_string()))
             #   winner, history, outcome = game.play()
              #  print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
               # print(game.to_string())
                #print("Move history:\n{!s}".format(history))


   

        #just take the move that gives us the most legal moves. 

    place_holder= game.get_legal_moves(player)
    more_score = float("-inf")
    if not place_holder:
        return float("-inf")


    for move in place_holder:
        rend_game = game.forecast_move(move)
        marlon_rando = float(len(rend_game.get_legal_moves(player)))
        if marlon_rando > more_score:
            more_score=marlon_rando
            return more_score
        else:
            return float("-inf")






def custom_score_2(game, player):
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
    # TODO: finish this function!

    #idea is try to pick moves as close to center as possible 
    #particularly useful for the opening game to make sure you don get cornered quickly. 

   #if game.is_loser(player):
    #    return float("-inf")

    #if game.is_winner(player):
     #   return float("inf")

    #w, h = game.width / 2., game.height / 2.
    #y, x = game.get_player_location(player)
    #rsquared=float((h - y)**2 + (w - x)**2)
    #own_moves_list = get_legal_moves(player)

     #   for moves in own_moves_list:
   
      #      new_game = game.forecast_move((1, 1))
       #     assert(new_game.to_string() != game.to_string())
        

    #idea is try to pick moves as close to center as possible 
    #particularly useful for the opening game to make sure you don get cornered quickly. 

    
    center_move = (3,3)
    center_score = float ("inf")
    our_moves = game.get_legal_moves(player)

    outer_ring = [(2,2),(2,3),(2,4),(3,2),(3,4),(4,2),(4,3),(4,4)]
    outer_ring_set= set(outer_ring)
    our_moves_set=set(our_moves)
    intersect_set = (our_moves_set & outer_ring_set)

    if (3,3) in our_moves:
        return center_score

    move_score= float ("-inf")
    if len(intersect_set) <=0: 
            return  float("-inf") 
    else:
        new_score =float("-inf")
        for move in intersect_set: 
            blend_game=game.forecast_move(move)
            move_score= len(blend_game.get_legal_moves(player))
            if move_score > new_score:
                new_score =move_score
                return new_score
            else:
                return float("-inf")










    raise NotImplementedError




def custom_score_3(game, player):
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
    # TODO: finish this function!
    

    # idea is to see if we can block our opponent. 
    # we're going to see if we have a move in common with our opponent. 
    # If taking one of their moves leaves them fewer legal moves than us, we want to take it 
    # This is particularly useful in the endgame
    # can even threshold it potentially (Difference greater than 2  difference greeter than 3)

   

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    


     #look for common elements in the two lists 
    own_moves_set = set(game.get_legal_moves(player))
    opp_moves_set = set(game.get_legal_moves(game.get_opponent(player)))
    intersection_set = (opp_moves_set & own_moves_set)

    if (len(intersection_set))<= 0:
       return float("-inf");
    else:
        intersection_list = list(intersection_set)
        plt_device= float("inf")
      #  number_of_moves=float(-inf)
        for move in intersection_list: 
            end_game=game.forecast_move(move)
            number_of_opp_moves = len(end_game.get_legal_moves(end_game.get_opponent(player)))
            if number_of_opp_moves <= plt_device:
                plt_device =number_of_opp_moves
                h_move =move
    return  plt_device

      # for diff_moves in intersection_list:




    #raise NotImplementedError




    #return float(own_moves - opp_moves)

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game,time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

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

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move







    
    def minimax(self, game, depth):
        #depth=2
            
        def max_value(game, depth):

                # if we're not going to return in time - throw an exceptio
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

                # get a list of our legal moves
            our_moves = game.get_legal_moves()
            if not our_moves:
                #if no legal moves or the depth is zero return the utility state
                return game.utility(self)
            if depth <= 0:
                return self.score(game,self)
             #if the above conditions set the floor for what we want our max to be better than           
            
            v = float("-inf")
            # for every move that we have, score it and take the max of v take the max of the min value nodes beneath it 

            for move in our_moves:
                v = max(v, min_value(game.forecast_move(move),depth-1))
               #current_depth=current_depth-1
                #return the max of these two items. 
            return v

        def min_value(game, depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
                #raise timeout 
            our_moves = game.get_legal_moves()
            # get our moves 
            
            if  not our_moves  :
                #reutrn utility state if terminal 
                return game.utility(self)
                #set the max value

            if depth<=0:
                return self.score(game,self)
            v = float("inf")
            for move in our_moves:
                v = min(v, max_value(game.forecast_move(move),depth-1))
               # current_depth=current_depth-1
               # score= self.score(game,self)
               #for each move take take the min value of the max node moves beneath is 
            return v


       # if self.time_left() < self.TIMER_THRESHOLD:
        #    raise SearchTimeout()
    #returning the arg max of all 
    #standard utility check 
        our_moves = game.get_legal_moves()
        if not our_moves: 
            return game.utility(self)
        if depth<=0:
            return self.score(game,self)
        v=float("-inf")
        mm_move= (-1,-1)
        for move in our_moves:
            #create a new_game that we can score for each move 
            new_game =game.forecast_move(move)
            #return the minimum 
            score = min_value(new_game, depth-1)
            #current_depth = current_depth-1
            #return the score of each of these moves
            if score>v:
                v = score
                mm_move = move
                #take the the move with the best score. 
        return mm_move

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """






    def get_move(self, game, time_left):
    


        # had to trash my previous approach ( way below) 
        # went to a much simpler version 
        # all we do is make sure we have a move in case of timeout
        #the try block will catch if we run out of time, 
        # we keep going till we trip the timeout, once we do we pass that and return the move we have. 
       # if self.time_left() < self.TIMER_THRESHOLD:
        #    raise SearchTimeout()
        self.time_left = time_left

       
        a_move = game.get_legal_moves()
        ab_move=(-1,-1)
        if not a_move:
            return(-1,-1)
        else:
            ab_move =a_move[0]
        
        try:
            
            depth = 1
            while True:
                ab_move = self.alphabeta(game, depth)
                depth =depth + 1
            return ab_move
        
        except SearchTimeout:
            pass
        
       








        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        
                player = game.active_player
"""     

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
       # n=0
       # depth =0


        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

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

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
    



        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if not game.get_legal_moves():
            return (-1,-1)


        ''' 
           # v=0
            # take a max value but we're using alpha beta to make the decisions 
        def max_value(self,game,depth,alpha,beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            
                    
            v = float("-inf")
            our_moves = game.get_legal_moves()
            for move in our_moves:
                print (our_moves)
                v = max(v,min_value(self,game.forecast_move(move),alpha,beta))
                if v >= beta:
                    return v
                alpha = max(alpha,v)
            return v
        '''





        def max_value(game, depth,alpha,beta):

                # if we're not going to return in time - throw an exceptio
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

                # get a list of our legal moves
            our_moves = game.get_legal_moves()
            if not our_moves:
                #if no legal moves or the depth is zero return the utility state
                return game.utility(self)
            if depth <= 0:
                return self.score(game,self)
             #if the above conditions set the floor for what we want our max to be better than           
            
            v = float("-inf")
            # for every move that we have, score it and take the max of v take the max of the min value nodes beneath it 

            for move in our_moves:
                v = max(v, min_value(game.forecast_move(move),depth-1,alpha,beta))
                if v >= beta:
                    return v
                alpha = max(alpha,v)
            return v
               #current_depth=current_depth-1
             

        '''         
        def min_value(self,game,depth,alpha,beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if depth ==0:
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
       
        '''



        def min_value(game, depth,alpha,beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
                #raise timeout 
            our_moves = game.get_legal_moves()
            # get our moves 
            
            if  not our_moves  :
                #reutrn utility state if terminal 
                return game.utility(self)
                #set the max value

            if depth<=0:
                return self.score(game,self)
            v = float("inf")
            for move in our_moves:
                v = min(v, max_value(game.forecast_move(move),depth-1,alpha,beta))
               # current_depth=current_depth-1
               # score= self.score(game,self)
                if v <= alpha:
                    return v
                beta = min(beta,v)

               #for each move take take the min value of the max node moves beneath is 
            return v




        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()    
        our_moves = game.get_legal_moves(self)
        #print ( 'akdjlksjs',our_moves)
        if not our_moves:
            return 0
        
        ab_score = float("-inf")
        ab_move = (-1,-1)
    
        for move in our_moves:
            score = min_value(game.forecast_move(move),depth-1,alpha,beta)
            
            if score >= beta:
                return score
            alpha = max(alpha,score)
            #print ('frustration')
            if score > ab_score:
                ab_score=score
               # print(' AB SCORE AB SCORE AB SCORE',ab_move)
                ab_move=move
                #print(' AB SCORE AB SCORE AB SCORE',ab_move)
                
        return  ab_move
    
    #raise NotImplementedError
