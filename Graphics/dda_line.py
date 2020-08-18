from graphics import *
import time

def DDALine(x1,y1,x2,y2):
    win = GraphWin('DDA Line', 600, 480)
    dx = float(x2-x1)
    dy = float(y2-y1)
    
    if dx>=dy:
        length = int(dx)
    else:
        length = int(dy)

    dx = dx/length
    dy = dy/length

    x = float(round(x1))
    y = float(round(y1))
    
    for i in range(1,length+1):
        PutPixle(win, int(x), int(y))
        x = x + dx
        y = y + dy
        i = i + 1
    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    pt = Point(x, y)
    pt.draw(win)


def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))
    DDALine(x1, y1, x2, y2)

if __name__ == "__main__":
    main()