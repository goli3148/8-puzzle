import random, math, copy

puzzle_size_index = 8
puzzle_size = puzzle_size_index+1
row_col_size = int(math.sqrt(puzzle_size))

# tree depth first search with saving current path from start node
level = -1
levels = []
branches = ['R', 'L', 'U', 'D']
memory = []
goal = None

zero_indexes = [-1, -1]

def board_initialization():
    global zero_indexes
    global goal
    global level
    
    rand = random.sample(range(puzzle_size), puzzle_size)
    board = [[-1 for i in range(row_col_size)] for i in range(row_col_size)]
    for i in range(row_col_size):
        for j in range(row_col_size):
            board[i][j] = rand[i*row_col_size+j]
            if board[i][j] == 0:
                zero_indexes = [i, j]
    
    board = [[1,2,5],[3,4,0],[6,7,8]]
    zero_indexes = [0, 2]
    level = 0
    levels.append(-1)
    memory.append(board)
    
    goal = [[i for i in range(j*3, j*3+3)] for j in range(3)]
    return board


def move(board, dir):
    global zero_indexes
    global row_col_size
    
    result = copy.deepcopy(board)
    i = copy.deepcopy(zero_indexes[0])
    j = copy.deepcopy(zero_indexes[1])
    if dir=='D':
        if i+1 == row_col_size:
            return False
        result[i+1][j], result[i][j] = result[i][j], result[i+1][j]
        return result, i+1, j
    if dir=='U':
        if i-1 == -1:
            return False
        result[i-1][j], result[i][j] = result[i][j], result[i-1][j]
        return result, i-1, j
    if dir=='R':
        if j+1 == row_col_size:
            return False
        result[i][j+1], result[i][j] = result[i][j], result[i][j+1]
        return result, i, j+1
    if dir=='L':
        if j-1 == -1:
            return False
        result[i][j-1], result[i][j] = result[i][j], result[i][j-1]
        return result, i, j-1
    
    print(f"ERROR:{dir}")
    exit()

def goal_test(board):
    global goal
    if board == goal:
        return True
    return False

def memory_test(board):
    global memory
    global level
    for i in range(len(memory)):
        if memory[i] == board:
            return True
    return False

def depth_first_search(arg):
    global level
    global levels
    global branches
    global memory
    global zero_indexes
    
    board = arg[0]
    next_level = arg[1]
    # -- next level
    if next_level:
        level+=1
        memory.append(copy.deepcopy(board))
        levels.append(-1)
        if goal_test(board):
            board_print(board, extra="SUCCESS")
            exit()
        return board, False
    # -- check if this level need backtracking
    elif (levels[level]+1>3):
        levels.pop()
        level -= 1
        memory.pop()
        board = copy.deepcopy(memory[-1])
        return board, False
    # -- check next move
    else:
        levels[level] += 1
        dir = branches[levels[level]]
        res = move(board, dir)
        if not res == False and memory_test(res[0]) == False:            
            board = res[0]
            
            zero_indexes[0] = res[1]
            zero_indexes[1] = res[2]
            return board, True
        else:
            return board, False
        

def board_print(board, index = -1, extra = ""):
    print(f"{index if not index == -1 else ''}: {extra}:board printing:")
    for i in range(row_col_size):
        print(board[i])
        
    print('-----------------------------------')


level_0_counter = 0
board = board_initialization()
board, res = depth_first_search((board, True))
while True:
    if level == 0:
        level_0_counter +=1
    board, res = depth_first_search((board, res))
