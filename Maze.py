import os
import keyboard
import time
import Stack as stk

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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                self.maze[self.ply.y][self.ply.x] = "1"
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
                self.maze[self.ply.y][self.ply.x] = "1"
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def check_way(self):
        positon = pos(self.ply.y, self.ply.x)
        if self.isInBound(positon.y-1,positon.x):
            if self.maze[positon.y-1][positon.x] == " ":
                up = True
            elif self.maze[positon.y-1][positon.x] == "E":
                up = True
            elif self.maze[positon.y-1][positon.x] == "X":
                up = False
            else:
                up = False
        else:
            up = False
        if self.isInBound(positon.y+1,positon.x):
            if self.maze[positon.y+1][positon.x] == " ":
                down = True
            elif self.maze[positon.y+1][positon.x] == "E":
                down = True
            elif self.maze[positon.y+1][positon.x] == "X":
                down = False
            else:
                down = False
        else:
            down = False
        if self.isInBound(positon.y,positon.x-1):
            if self.maze[positon.y][positon.x-1] == " ":
                left = True
            elif self.maze[positon.y][positon.x-1] == "E":
                left = True
            elif self.maze[positon.y][positon.x-1] == "X":
                left = False
            else:
                left = False
        else:
            left = False
        if self.isInBound(positon.y,positon.x+1):
            if self.maze[positon.y][positon.x+1] == " ":
                right = True
            elif self.maze[positon.y][positon.x+1] == "E":
                right = True
            elif self.maze[positon.y][positon.x+1] == "X":
                right = False
            else:
                right = False
        else:
            right = False
        a = waycan(up,down,left,right)
        return a

    def clearway(self):
        posnow = pos(self.ply.y, self.ply.x)
        part = self.check_way()
        if not(part.up or part.down or part.left or part.right):
            if self.isInBound(posnow.y-1,posnow.x):
                if self.maze[posnow.y-1][posnow.x] == "1" :
                    self.maze[posnow.y-1][posnow.x] = " "
            if self.isInBound(posnow.y+1,posnow.x):
                if self.maze[posnow.y+1][posnow.x] == "1" :
                    self.maze[posnow.y+1][posnow.x] = " "
            if self.isInBound(posnow.y,posnow.x-1):
                if self.maze[posnow.y][posnow.x-1] == "1" :
                    self.maze[posnow.y][posnow.x-1] = " "
            if self.isInBound(posnow.y,posnow.x+1):
                if self.maze[posnow.y][posnow.x+1] == "1" :
                    self.maze[posnow.y][posnow.x+1] = " "

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

class waycan:

    def __init__(self, u, d, r, l) -> None:
        self.up = u
        self.down = d
        self.right = r
        self.left = l

# Funtion
    
def check_up(self): # ไม่ได้ใช้
    next_move = pos(self.ply.y-1,self.ply.x)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างบนเดินได้ไอโง่")
            
        else:
            return False
    return True
def check_down(self): # ไม่ได้ใช้
    next_move = pos(self.ply.y+1,self.ply.x)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างล่างเดินได้ไอโง่")
            return True
        else:
            return False

def check_left(self): # ไม่ได้ใช้
    next_move = pos(self.ply.y, self.ply.x-1)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างซ้ายเดินได้ไอโง่")
            return True
        else:
            return False

def check_right(self): # ไม่ได้ใช้
    next_move = pos(self.ply.y, self.ply.x+1)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างขวาเดินได้ไอโง่")
            return True
        else:
            return False
        
def auto_move(self): # ไม่ได้ใช้
    up = False
    down = False
    left = False
    right = False
    
    up = check_up(self)
    down = check_down(self)
    left = check_left(self)
    right = check_right(self)

    way_to_go =[up,down,left,right]

    print(way_to_go)
    while True:
        if up == True:
            self.move_up()
            self.print()
        else:
            break
        if left == True:
            self.move_left()
            self.print()
        else:
            break
        if right == True:
            self.move_right
            self.print()
        else:
            self.move_down()
            break

        
        

        
# Main

if __name__ == '__main__':

    m = maze()
    m.print()
    a = m.check_way()
    print(a.up,a.down,a.left,a.right)

    old_x = m.ply.x 
    old_y = m.ply.y

    # if (old_x == m.ply.x and old_y == m.ply.y) :
    
    x = stk.Stack()

    while True:

        if x._top == None:
                if m.move_up():
                    m.print()
                    x.push(1)
                else:
                    break
        if x._top.item == 1 or x._top.item == 5:
                if m.move_up():
                    m.print()
                    print(x._top.item)
                    x.push(1)
                else:
                    break
        if x._top.item == 2:
                if m.move_left():
                    m.print()
                    x.push(2)
                    print(x._top.item)
                else:
                    break
        if x._top.item == 3:
                if m.move_right():
                    m.print()
                    print(x._top.item)
                    x.push(3)
                else:
                    break
        if x._top.item == 4:
                if m.move_down():
                    m.print()
                    x.push(4)
                    print(x._top.item)
                else:
                    break

        if (old_x == m.ply.x and old_y == m.ply.y) :
            if x._top.item == 4:
                x.pop()
                x.push(5)
            elif x._top.item == 3:
                x.pop()
                x.push(4)
            elif x._top.item == 2:
                x.pop()
                x.push(3)
            elif x._top.item == 1:
                x.pop()
                x.push(2)
            m.clearway()

        old_x = m.ply.x 
        old_y = m.ply.y



    