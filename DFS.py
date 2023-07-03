import copy
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
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
        self.board = [[1,2,0], [3,4,5], [6,7,8]]
        self.goal  = [[0,1,2], [3,4,5], [6,7,8]]
        
    def set_board(self, board):
        self.board = board
        
    def goal_test(self):
        if self.board == self.goal:
            return True
        return False
    
    def move(self, dir):
        temp = copy.deepcopy(self.board)
        i,j  = self.findZero()
        if i == False and j == False:
            return False
        if dir == 'R' and j+1 < 3: temp[i][j+1] ,temp[i][j] = temp[i][j], temp[i][j+1]
        elif dir == 'L' and j-1 > -1: temp [i][j-1] ,temp[i][j] = temp[i][j], temp[i][j-1]
        elif dir == 'U' and i+1 < 3: temp [i+1][j], temp[i][j] = temp[i][j], temp[i+1][j]
        elif dir == 'D' and i-1 > -1: temp [i-1][j], temp[i][j] = temp[i][j], temp[i-1][j]
        else:
            return False
        return temp
    
    def findZero(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j
        return False, False
    def equal(self, board):
        if self.board == board:
            return True
        return False
    
    def printBoard(self):
        print("BOARD:")
        for i in range(len(self.board)):
            print(self.board[i])
        print("------------------------")

class DFS:
    def SecondMethod(self):
        Dir = ['R', 'U', 'L', 'D']
        stack = Stack()
        board_ = Board()
        stack.push(board_.board)
        temp = True
        while not temp == False:
            board_.printBoard()
            temp = stack.pop()
            board_.set_board(temp)
            if (board_.goal_test()):
                print("Success")
                exit()
            for i in range(4):
                res = board_.move(Dir[i])
                if not res == False:
                    if not board_.equal(res) and not stack.visitedNode(res):
                        stack.push(board_.board)
                        stack.push(res)
                        board_.set_board(res)
        print("failed")
    def __init__(self):
        self.stack = Stack()
        self.board = Board()
        self.stack.push(self.board.board)
        self.dir = ['L', 'U', 'R', 'D']
        self.level()
        print("FAILED")
        pass
    
    def level(self):
        while not self.stack.isEmpty():
            temp = self.stack.pop()
            self.board.set_board(temp)
            self.board.printBoard()
            if (self.board.goal_test()):
                print("SUCCESS")
                exit()
            for i in range(4):
                res = self.board.move(self.dir[i])
                if not res == False:
                    if not self.board.equal(res) and not self.stack.visitedNode(res):
                        self.stack.push(temp)
                        self.stack.push(res)
                        self.board.set_board(res)
                        self.level()
    
                        
    


print("START:")
DFS()