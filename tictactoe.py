"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # flatten the board to be able to count values
    flat_board = [marker for row in board for marker in row]

    # if board in an initial state or same number of X's and O's return X
    if board == initial_state() or flat_board.count(O) == flat_board.count(X):
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, position in enumerate(row):
            if position == EMPTY:
                actions.add((i, j))
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # unpack the action tuple
    i, j = action
    # if action is not valid raise an exception
    if board[i][j] != EMPTY:
        raise Exception('This move is not allowed')
    else:
        new_board = copy.deepcopy(board)
        # assign current player marker to the position on the copied board
        new_board[i][j] = player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # row win
    if (board[0][0] == board[0][1] == board[0][2] != EMPTY) or (board[1][0] == board[1][1] == board[1][2] != EMPTY) or (board[2][0] == board[2][1] == board[2][2] != EMPTY):
        return X if player(board) == O else O
    # col win
    elif (board[0][0] == board[1][0] == board[2][0] != EMPTY) or (board[0][1] == board[1][1] == board[2][1] != EMPTY) or (board[0][2] == board[1][2] == board[2][2] != EMPTY):
        return X if player(board) == O else O
    # diagonal win
    elif (board[0][0] == board[1][1] == board[2][2] != EMPTY) or (board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return X if player(board) == O else O
    # tie or game in progress
    else:
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there is a winner return True
    if winner(board) is not None:
        return True
    else:
        if any(position == EMPTY for row in board for position in row):
            return False
        else:
            return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # MAX player
    elif player(board) == X:
        value = -math.inf
        for action in actions(board):
            curr_value = min_value(result(board, action))
            # Alpha-Beta Pruning
            if curr_value == 1:
                return action
            elif curr_value > value:
                value = curr_value
                optimal_action = action
        return optimal_action

    # MIN player
    else:
        value = math.inf
        for action in actions(board):
            curr_value = max_value(result(board, action))
            # Alpha-Beta Pruning
            if curr_value == -1:
                return action
            elif curr_value < value:
                value = curr_value
                optimal_action = action
        return optimal_action

    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        # Alpha-Beta Pruning
        if v == 1:
            return v
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        # Alpha-Beta Pruning
        if v == -1:
            return v
    return v
