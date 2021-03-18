"""
Write your code to play tic-tac-toe in this file.

Have a look over the example agent `make_first_avaliable_move` before implimenting 
your own agent.
"""

# Import the function engine from engine.py
# If you get an error saying you can't find engine, check that engine.py (from the same wattle
# folder as this file) is in the same folder on your computer
from engine import engine


# Example agent
def make_first_avaliable_move(board):
    """
    An agent that only plays in the first available position

    Input: A tic tac toe board in its string representation nine characters (either "X"s, "O"s or "."s)
    Output: A string representation of the input board with our move made on it

    A valid strategy (if not a very good one) is to place your piece in the first
    open place on the tic tac toe board. An agent that does this isn't going to win
    every game but it is able to play a move onto every possible board so its a good start
    to see how the system operates with a valid agent

    """
    # Work out which pieces we are playing
    """
        Summary of thinking:
        - Starting with the premise that "X" always play first we can infer two things
            -> if the number of X's and O's are equal X should play next
            -> if the number of empty squares ('.') is odd (empty board = 9, one move each = 7, ....)
                then X should be playing
        - Using the first inference we will make the comparison and return one of two things based on the result
            -> Structure of the code: an if statement with different return calls within each condition
    """
    # Work out which pieces we are playing
    # Compare the number of "X"s and "O"s
    if board.count("X") == board.count("O"):
    # If equal number of X's and O's then we are playing "X"s (if statement)
        our_pieces = "X"
    # If not then we must be playing "O"s (else)
    else:
        our_pieces = "O"

    # Seize the top centre (position number 1)
    # check that its an available move (if statement)
    # generate the board with our move on it
    # return the board (on the spot return call)
    """this turned out to be a terrible strategy and wasn't implemented. The only way to win, was not to play (position 1)!"""


    # Replace the first "." with our pieces
    """
    Conveniently there is a bound method for string objects called "replace"
    looking at the documentation it can take three arguments: a string of the character(s) to
    be replaced, what to replace those character(s) with and (optionally) how many times to do so.

    Calling this bound method on `board` which returns us a new string with our requested changes that
    we will call `first_open_move`
    
    """
    move = board.replace('.',our_pieces,1)
    # Give out move back to the engine
    return move

def stringify (str):

    """ function modified from https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/ .... converts array to string """

    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in str:  
        str1 += ele
    # return string which we will then pass to engine
    return str1

def your_agent(board):

    """
    The engine will pass this function the current game-board;
    after adding your prefered move to the board, return it back to the engine.

    SHALL WE PLAY A GAME!
    """
  
    # convert board to list (need better name for array)

   
    # If equal number of X's and O's then we are playing "X"s (if statement)
    if board.count("X") == board.count("O"):

        our_pieces = "X"

        # if we move first 

    else:
        our_pieces = "O"


    """ take middle piece then corner 2 and 6"""

    # 0 1 2
    # 3 4 5
    # 6 7 8
    wins = []
    for a, b, c in (

    (0, 1, 2),  # top row                       Here's the board:
    (3, 4, 5),  # middle row                         0 1 2
    (6, 7, 8),  # bottom row                         3 4 5
    (0, 3, 6),  # left column                        6 7 8
    (1, 4, 7),  # middle column
    (2, 5, 8),  # right column
    (0, 4, 8),  # top-left to bottom-right diagonal
    (2, 4, 6),  # top-right to bottom-left diagonal

    ):

    # send array to be converted back to string then replace board with updated values
        list = []
        for i in (board):
            list.append(i)


        moves_a = a
        moves_b = b
        moves_c = c

        print (f"this is a: {a}, this is b: {b}, this is c: {c}") 

        if list[a] == '.':
            print (a)
            list[a] = our_pieces
            print (list)
            move = board.replace(board,stringify(list))
            
            return move
        elif list[a] != '.' and list[b] == '.':
            list[b] = our_pieces
             
            
        # print (list)
        # print (f"this is the move: {move}")
        # print (f"this is the board: {board}")

    """
    All the functions above (our agent(s) and any helper functions) are just sitting there waiting
    to be called and put to use. The actual calling of the function is done by the engine code
    which takes in an agent function and plays out all the possible games with that agent

    We imported the engine function from engine.py at the top of the file, to run an agent
    we call engine and pass in the agent

    When you're ready with `your_agent` you can replace the agent function that is being called
    """

#When you're ready swap over which line is being commented out
# engine(make_first_avaliable_move)
engine(your_agent)