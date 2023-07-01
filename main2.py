import copy
class data:
    def __init__(self) -> None:
        self.size = 9
        self.arraySize = 3
        self.board = None
        self.memory = []
        self.branches = []
        self.level = -1
        self.moveDirs = ['R', 'U', 'L', 'D']
        self.zeroIndex = [-1, -1]
    
    # board functions
    def get_board(self):
        return copy.deepcopy(self.board)
    def set_board(self, board):
        self.board = copy.deepcopy(board)
    
    # memory functions
    def get_memory(self):
        return copy.deepcopy(self.memory[-1])
    def save_memory(self, board):
        self.memory.append(copy.deepcopy(board))
    def del_memory(self):
        try:
            self.memory.remove(self.level)
        except:
            pass
    
    # branches function
    def get_branches(self):
        return self.branches[self.level]
    def new_branches(self):
        self.branches.append(-1)
    def increase_branches(self):
        self.branches[self.level] += 1
    def decrease_branches(self):
        self.branches[self.level] -= 1
    def del_branches(self):
        self.branches.pop()
    
    # level functions
    def get_level(self):
        return self.level
    def increase_level(self):
        self.level += 1
    def decrease_level(self):
        self.level -= 1
    
    # moveDirs functions
    def get_moveDirs(self, index):
        return self.moveDirs[index]
    
    # zeroIndex functions
    def get_zeroIndex(self):
        return copy.deepcopy(self.zeroIndex)
    def set_zeroIndex(self, zeroIndex):
        self.zeroIndex = zeroIndex
    
    # PERMISSIONS (True: allow, False: forbidden)
    def permisson_move(self, dir):    
        if   dir == 'R': return True if self.zeroIndex[1]+1 < self.arraySize else False
        elif dir == 'L': return True if self.zeroIndex[1]-1 > -1             else False
        elif dir == 'U': return True if self.zeroIndex[0]+1 < self.arraySize else False
        elif dir == 'D': return True if self.zeroIndex[0]-1 > -1             else False
        return False
    
    def permission_duplicate(self, board):
        for i in self.memory:
            if i == board:
                return False
        return True
    
    def permission_branches(self):
        if self.branches[self.level]+1 == 4:
            return False
        return True
    
class Operations:
    def __init__(self) -> None:
        self.data = data()
        self.goal = [[0,1,2],[3,4,5],[6,7,8]]
        
    def initialization(self):
        board = [[1,2,0],[3,4,5],[6,7,8]]
        self.create(board, [0, 2])
    
    def create(self, board, zeroIndex):
        self.data.increase_level()
        self.data.save_memory(board)
        self.data.new_branches()
        self.data.set_board(board)
        self.data.set_zeroIndex(zeroIndex)
        if self.goal_test():
            print("SOLVED")
            exit()
    
    def move(self, dir):
        temp = self.data.get_board()
        i,j = self.data.get_zeroIndex()
        if dir == 'R' : 
            temp[i][j+1] ,temp[i][j] = temp[i][j], temp[i][j+1]
            j += 1
        elif dir == 'L' : 
            temp [i][j-1] ,temp[i][j] = temp[i][j], temp[i][j-1]
            j -= 1
        elif dir == 'U':
            temp [i+1][j], temp[i][j] = temp[i][j], temp[i+1][j]
            i += 1
        elif dir == 'D':
            temp [i-1][j], temp[i][j] = temp[i][j], temp[i-1][j]
            i -= 1
        else:
            return False
        return temp, i, j
    
    # three main op: 
    # 1.allowAll  2.duplicate or move:forbidden - branches:allow    3.branches:allow    
    def alwAl(self, res): #allowAll
        self.create(res[0], [res[1], res[2]])
    
    def dmFbA(self):# duplicate  move:Forbidden  branches:Allow
        self.data.increase_branches()
        
    def bF(self):# branches: Forbidden
        self.data.del_memory() # delete current memory
        self.data.del_branches() # delete current branches level
        self.data.decrease_level() # get back
        # RESTORE data
        board = self.data.get_memory()
        self.data.set_board(board)
        self.data.increase_branches() # increase branches of current level
        #FIND ZERO IN BOARD
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    self.data.set_zeroIndex([i,j])
                    return None
        #FIND ZERO IN BOARD
    
    # TEST Functions
    def goal_test(self):
        return True if self.data.get_board() == self.goal else False
    
    #MAiN ALGORITHM
    def MnAm(self):
        self.data.increase_branches()
        Dir = self.data.get_branches()
        Dir = self.data.get_moveDirs(Dir)
            
        if self.data.permisson_move(Dir) and self.data.permission_branches():
            res = self.move(Dir)
            if self.data.permission_duplicate(res[0]):
                self.alwAl(res)
        elif self.data.permission_branches():
            self.dmFbA()
        elif not self.data.permission_branches():
            self.bF()
            


op = Operations()
op.initialization()
while True:
    op.MnAm()