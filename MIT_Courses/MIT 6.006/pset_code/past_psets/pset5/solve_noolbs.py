##################################################
##  Problem 5.5 Noolbs
##################################################

#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################


def board_str(B):
    """
    Args:
        B (tuple): board configuration
    Output:
        str: ASCII string representing the input board configuration
    """
    C = len(B[0])
    rows = ["+" + ("-" * C) + "+"]
    for row in B:
        rows.append("|" + "".join([str(c) for c in row]) + "|")
    rows.append(rows[0])
    S = "\n".join(rows)
    return S


def find_monkey_position(B):
    """
    Args:
        B (tuple): board configuration
    Output:
        int: column position of the monkey in B
    """
    for i, x in enumerate(B[-1]):
        if x == "x":
            return i

    assert False


def num_balloons(B):
    """
    Args:
        B (tuple): board configuration
    Output:
        int: number of balloons on the board
    """
    ret = 0
    for r in B[:-1]:
        for c in r:
            if c != 0:
                ret += 1
    return ret


def make_move(B, cur_monkey_pos, cur_num_balloons, cur_num_lives, move):
    """
    This function simulates a single move in the game. Specifically, it (potentially) changes the
    position of the monkey on the board, depending on the given move, and then shifts all the
    balloons down, respawning at the top as needed.

    It updates and returns the board, monkey position, number of balloons, and number of remaining lives.

    Args:
        B (tuple): current board configuration
        cur_monkey_pos (int): current column position of the monkey
        cur_num_balloons (int): current number of balloons on the board
        cur_num_lives (int): current number of lives remaining
        move (str): the proposed move (one of 'left', 'right', 'shoot')
    Output:
        (tuple, int, int, int): A tuple consisting of the board configuration after the move,
                                the new monkey position, the new number of balloons on the map,
                                and the new number of lives left
                                (or None if invalid move or if the monkey gets hit)
    """

    def check_lose(B, cur_monkey_pos):
        """
        Args:
            B (tuple): board configuration
            cur_monkey_pos (int): current column position of the monkey
        Output:
            bool: True if a balloon will hit the monkey when the balloons shift down; False otherwise
        """
        assert B[-1][cur_monkey_pos] == "x"
        if B[-2][cur_monkey_pos] != 0:
            return True
        return False

    def shift_down(B, cur_monkey_pos, cur_num_lives):
        """
        Just performs the shift of all the balloons downwards.
        Args:
            B (tuple): board configuration
            cur_monkey_pos (int): current column position of the monkey
            cur_num_lives (int): current number of lives in this configuration
        Output:
            (tuple, int): tuple consisting of the board configuration after balloons have all moved
                          down by 1 and the new number of lives (or None if the monkey gets hit)
        """

        if check_lose(B, cur_monkey_pos):
            return None

        new_board = []
        new_num_lives = cur_num_lives

        # construct the top row: if the balloon hits the ground, it respawns with +1 and we lose a life
        new_num_lives -= sum(1 for b in B[-2] if b > 0)
        top_row = tuple((b + 1 if 0 < b < 3 else b) for b in B[-2])
        new_board.append(top_row)

        # move all the middle rows down
        new_board.extend([r for r in B[:-2]])

        # add the ground row: nothing changes
        new_board.append(B[-1])

        return (tuple(new_board), new_num_lives)

    def partial_move(B, cur_monkey_pos, cur_num_balloons, move):
        """
        Just performs the move, without the shift downwards
        Args:
            B (tuple): board configuration
            cur_monkey_pos (int): current column position of the monkey
            cur_num_balloons (int): current number of balloons on the board
            move (str): the proposed move (one of 'left', 'right', 'shoot')
        Output:
            (tuple, int, int): A tuple consisting of the board configuration after the move,
                               the new monkey position, and the new number of balloons on the map
                               (or None if invalid move)
        """

        assert B[-1][cur_monkey_pos] == "x"
        R = len(B)
        C = len(B[0])

        new_board = [r for r in B[:-1]]
        new_bottom_row = [0 for _ in range(C)]
        new_monkey_pos = cur_monkey_pos
        new_num_balloons = cur_num_balloons

        if move == "left":
            if new_monkey_pos == 0:
                return None
            new_monkey_pos -= 1
        elif move == "right":
            if new_monkey_pos == C - 1:
                return None
            new_monkey_pos += 1
        elif move == "shoot":
            # simulate the dart
            for row in range(R - 2, -1, -1):
                if B[row][new_monkey_pos] != 0:
                    new_row = list(B[row])
                    new_row[new_monkey_pos] -= 1
                    if new_row[new_monkey_pos] == 0:
                        new_num_balloons -= 1
                    new_board[row] = tuple(new_row)
                    break
        else:
            assert False, "invalid move: " + move

        new_bottom_row[new_monkey_pos] = "x"
        new_board.append(tuple(new_bottom_row))
        return (tuple(new_board), new_monkey_pos, new_num_balloons)

    # make the move
    move_res = partial_move(B, cur_monkey_pos, cur_num_balloons, move)
    if move_res is None:  # invalid move
        return None
    move_board, new_monkey_pos, new_num_balloons = move_res  # unpack

    # shift all the balloons down
    shift_res = shift_down(move_board, new_monkey_pos, cur_num_lives)
    if shift_res is None:  # check if a balloon hit the monkey
        return None
    new_board, new_num_lives = shift_res  # unpack
    return (new_board, new_monkey_pos, new_num_balloons, new_num_lives)

#####################################
##### YOUR CODE IN THIS SECTION
#####################################
from collections import deque

def solve_noolbs(B):
    """
    Args:
        B (tuple): the initial board configuration.

    Output:
        int: the minimum number of moves to pop all the balloons (or None if it's not possible).
    """

    ##################
    # YOUR CODE HERE #
    ##################
    print("\nORIGINAL")
    print(board_str(B))

    # BFS processing queue, append initial configuration. #? also keep track of num moves to this config?
    queue = deque()
    queue.append(((B, find_monkey_position(B), num_balloons(B), 3), 0))

    SEEN = set()

    num_moves = 0

    while len(queue) != 0:
        res = queue.popleft()
        config = res[0]
        num_moves = res[1]

        # return if this was dead end
        if config == None: continue

        # else get the configuration
        board, mpos, balloons, lives  = config
        # print(f"\n{board_str(board)}\nPos:{mpos}, NumBalloons:{balloons}, Lives:{lives}")

        # if out of lives, continue
        if lives <= 0: continue

        # check if configuration is a winning configuration:
        if balloons == 0 and lives > 0: 
            print(f"MINIMUM num moves: {num_moves}")
            return num_moves

        # else create neighbors - will never be a previous configuration since all balloons go down eventually
        move1 = make_move(board, mpos, balloons, lives, move='left')
        if move1 == None: pass
        if move1 not in SEEN:
            SEEN.add(move1)
            queue.append((move1, num_moves+1))

        move2 = make_move(board, mpos, balloons, lives, move='right')
        if move2 == None: pass
        if move2 not in SEEN:
            SEEN.add(move2)
            queue.append((move2, num_moves+1))

        move3 = make_move(board, mpos, balloons, lives, move='shoot')
        if move3 == None: pass
        if move3 not in SEEN:
            SEEN.add(move3)
            queue.append((move3, num_moves+1))

        # store these moves in memory? linear scan to check if 

        # WILL GIVE ERROR IF NONE!!! i.e. if you LOSE!!
        # B1, mpos1, ball1, lives1 = make_move(B, find_monkey_position(B), num_balloons(B), 3, move='left')
        # B2, mpos2, ball2, lives2 = make_move(B, find_monkey_position(B), num_balloons(B), 3, move='right')
        # B3, mpos3, ball3, lives3 = make_move(B, find_monkey_position(B), num_balloons(B), 3, move='shoot')

        # print(f"\n{board_str(B1)}\nPos:{mpos1}, NumBalloons:{ball1}, Lives:{lives1}")
        # print(f"\n{board_str(B2)}\nPos:{mpos2}, NumBalloons:{ball2}, Lives:{lives2}")
        # print(f"\n{board_str(B3)}\nPos:{mpos3}, NumBalloons:{ball3}, Lives:{lives3}")

    return None