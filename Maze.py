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
            
        else:
            return False
    return True
def check_down(self):
    next_move = pos(self.ply.y+1,self.ply.x)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างล่างเดินได้ไอโง่")
            return True
        else:
            return False

def check_left(self):
    next_move = pos(self.ply.y, self.ply.x-1)
    if self.isInBound(next_move.y,next_move.x):
        if self.maze[next_move.y][next_move.x] == " ":
            print("ข้างซ้ายเดินได้ไอโง่")
            return True
        else:
            return False

def check_right(self):
    next_move = pos(self.ply.y, self.ply.x+1)
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
    # auto_move(m)

    # while True:
    #     if m.move_up():
    #         m.print()

    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        if keyboard.is_pressed("w"):
            auto_move(m)
            # if m.move_up():
            #     m.print()
                
            # else:
            #     break
        if keyboard.is_pressed("s"):
            if m.move_down():
                m.print()
                auto_move(m)
            else:
                break
        if keyboard.is_pressed("a"):
            if m.move_left():
                m.print()
                auto_move(m)
            else:
                break
        if keyboard.is_pressed("d"):
            if m.move_right():
                m.print()
                auto_move(m)
            else:
                break
        # if keyboard.is_pressed("k"):
        #     if m.print():
        #         auto_move(m)
        # else:
        #     break



    