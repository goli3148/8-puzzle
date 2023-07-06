import copy, os
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(copy.deepcopy(data))
    def pop(self):
        if self.isEmpty(): return False
        return self.stack.pop()
    def visitedNode(self, data):
        for i in self.stack:
            if i == data:
                return True
        return False
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
class Board:
    def __init__(self):
        self.size = 3
        self.board = [[1,2,3], [6,5,4], [7,8,0]]
        self.board = [[5,6,8], [0,1,2], [3,4,7]]
        self.goal  = [[0,1,2], [5,4,3], [6,7,8]]
        
    def set_board(self, board):
        self.board = copy.deepcopy(board)
        
    def goal_test(self):
        if self.board == self.goal:
            return True
        return False
    
    def move(self, dir):
        temp = copy.deepcopy(self.board)
        i,j  = self.findZero()
        if i == -1 and j == -1:
            return False
        if dir == 'R' and j+1 < self.size: temp[i][j+1] ,temp[i][j] = temp[i][j], temp[i][j+1]
        elif dir == 'L' and j-1 > -1: temp [i][j-1] ,temp[i][j] = temp[i][j], temp[i][j-1]
        elif dir == 'D' and i+1 < self.size: temp [i+1][j], temp[i][j] = temp[i][j], temp[i+1][j]
        elif dir == 'U' and i-1 > -1: temp [i-1][j], temp[i][j] = temp[i][j], temp[i-1][j]
        else:
            return False
        return temp
    
    def findZero(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j
        return -1, -1
    
    def equal(self, board):
        if self.board == board:
            return True
        return False
    
    def printBoard(self, extra=''):
        print("------------------------")
        print(f"BOARD:{extra}")
        for i in range(len(self.board)):
            print(self.board[i])

class DFS:
    def __init__(self):
        self.frontier = Stack()
        self.closed = Stack()
        self.board = Board()
        self.frontier.push(self.board.board)
        self.dir = ['L', 'R', 'U', 'D']
        
        self.LEVEL = 0
        
        while not self.frontier.isEmpty():
            self.expand()
        print("FAILED")
        pass
    
    def expand(self):
        board_ = Board()
        self.LEVEL+=1
        board = self.frontier.pop()
        self.closed.push(board)
        board_.set_board(board)
        board_.printBoard()
        if board_.goal_test():
            print("success")
            exit()
        for i in range(4):
            result = board_.move(self.dir[i])
            print(f"LEVEL:{self.LEVEL}->{i}")
            if (self.LEVEL == 29 and i ==3):
                print(result)
                # print(self.printBoard(result))
            if not result == False:
                if not self.closed.visitedNode(result) and not self.frontier.visitedNode(result):
                    self.frontier.push(result)
                    self.expand()
                    self.LEVEL -= 1
    
    def printBoard(self, board,extra=''):
        print("------------------------")
        print(f"BOARD:{extra}")
        for i in range(len(board)):
            print(board[i])
    
                        

print("START:")

DFS()