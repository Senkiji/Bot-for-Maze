import os
import keyboard
import time

# Class
class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x) #ตำแหน่ง x y
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    # def auto_test(self):
    #     check_up = pos(self.ply.y-1,self.ply.x)
    #     if self.isInBound(check_up.y,check_up.x):
    #         if self.maze[check_up.y][check_up.x] == " ":
    #             self.maze[self.ply.y][self.ply.x] = "1"
    #             self.maze[check_up.y][check_up.x] = "P"
    #             self.ply = check_up
    #             time.sleep(0.25)
    #         if self.maze[check_up.y][check_up.x] == "E":
    #             self.printEND()
    #             return False
    #     return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

# Funtion
    
def check_up(self):
    next_move = pos(self.ply.y-1,self.ply.x)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างบนเดินได้ไอโง่")
            return True
        else:
            return False

def check_down(self):
    next_move = pos(self.ply.y+1,self.ply.x)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างล่างเดินได้ไอโง่")
            return True
        else:
            return False

def check_left(self):
    next_move = pos(self.ply.y,self.ply.x-1)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างซ้ายเดินได้ไอโง่")
            return True
        else:
            return False

def check_right(self):
    next_move = pos(self.ply.y,self.ply.x-1)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างขวาเดินได้ไอโง่")
            return True
        else:
            return False
        
def auto_move(self):
    up = False
    down = False
    left = False
    right = False
    way_to_go =[up,down,left,right]
    print(way_to_go)
    
    up = check_up(self)
    if way_to_go == [True,False,False,False] or way_to_go == [True,True,False,False]:
        print("walk up")

        
# Main

if __name__ == '__main__':

    m = maze()
    m.print()
    auto_move(m)

    # while True:
    #     if m.move_up():
    #         m.print()
        


    