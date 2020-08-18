from graphics import *
import numpy as np
import math

def Translation(win,choice1,p,T):
    dp = np.zeros((3,3))

    if choice1 == 1:
        p1 = Point(p[0][0],p[0][1])
        p2 = Point(p[1][0],p[1][1])
        p3 = Point(p[2][0],p[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win)
    
    elif choice1 == 2:
        rect = Rectangle(Point(p[0][0], p[0][1]), Point(p[1][0],p[1][1]))
        rect.draw(win)

    # Translation    
    #p.shape will return the (row,column)
    print(p.shape[0])
    for i in range(p.shape[0]):
        dp[i][0] = p[i][0] + T[0][0]
        dp[i][1] = p[i][1] + T[1][0]

    if choice1 == 1:
        p1 = Point(dp[0][0],dp[0][1])
        p2 = Point(dp[1][0],dp[1][1])
        p3 = Point(dp[2][0],dp[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win) 

    elif choice1 == 2:
        rect = Rectangle(Point(dp[0][0], dp[0][1]), Point(dp[1][0],dp[1][1]))
        rect.draw(win)
    
    win.getMouse()
    win.close()
    
def Rotation(win,choice1,p,theta,rot_choice):
    dp = np.zeros((3,3))

    if choice1 == 1:
        p1 = Point(p[0][0],p[0][1])
        p2 = Point(p[1][0],p[1][1])
        p3 = Point(p[2][0],p[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win)
    
    elif choice1 == 2:
        rect = Rectangle(Point(p[0][0], p[0][1]), Point(p[1][0],p[1][1]))
        rect.draw(win)
    
    print(p.shape[0])
    for i in range(p.shape[0]):
        if rot_choice == 1:
            dp[i][0] = int(p[i][0]*math.cos(theta) - p[i][1]*math.sin(theta))
            dp[i][1] = int(p[i][0]*math.sin(theta) + p[i][1]*math.cos(theta))
        
        elif rot_choice == 2:
            dp[i][0] = int(p[i][0]*math.cos(theta) + p[i][1]*math.sin(theta))
            dp[i][1] = int((-p[i][0]*math.sin(theta)) + p[i][1]*math.cos(theta))

    print(dp)

    if choice1 == 1:
        p1 = Point(dp[0][0],dp[0][1])
        p2 = Point(dp[1][0],dp[1][1])
        p3 = Point(dp[2][0],dp[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win) 

    elif choice1 == 2:
        rect = Rectangle(Point(dp[0][0], dp[0][1]), Point(dp[1][0],dp[1][1]))
        rect.draw(win)
    
    win.getMouse()
    win.close()

def Scaling(win,choice1,p,S):
    dp = np.zeros((3,3))

    if choice1 == 1:
        p1 = Point(p[0][0],p[0][1])
        p2 = Point(p[1][0],p[1][1])
        p3 = Point(p[2][0],p[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win)
    
    elif choice1 == 2:
        rect = Rectangle(Point(p[0][0], p[0][1]), Point(p[1][0],p[1][1]))
        rect.draw(win)

    print(p.shape[0])
    dp = np.dot(p,S)
    print(dp)

    if choice1 == 1:
        p1 = Point(dp[0][0],dp[0][1])
        p2 = Point(dp[1][0],dp[1][1])
        p3 = Point(dp[2][0],dp[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win) 

    elif choice1 == 2:
        rect = Rectangle(Point(dp[0][0], dp[0][1]), Point(dp[1][0],dp[1][1]))
        rect.draw(win)
    
    win.getMouse()
    win.close()

def Reflection(win,choice1,p,ref_choice):
    dp = np.zeros((3,3))

    if choice1 == 1:
        p1 = Point(p[0][0],p[0][1])
        p2 = Point(p[1][0],p[1][1])
        p3 = Point(p[2][0],p[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win)
    
    elif choice1 == 2:
        rect = Rectangle(Point(p[0][0], p[0][1]), Point(p[1][0],p[1][1]))
        rect.draw(win)

    print(p.shape[0])
    for i in range (p.shape[0]):
        x = p[i][0]
        y = p[i][1]
        
        if(ref_choice==1):
            dp[i][0]=x
            dp[i][1]=(-1)*y
        
        if(ref_choice==2):
            dp[i][0]=(-1)*x
            dp[i][1]=y
            
        if(ref_choice==3):
            dp[i][0]=(-1)*x
            dp[i][1]=(-1)*y
        
        if(ref_choice==4):
            dp[i][0]=y
            dp[i][1]=x
            
        if(ref_choice==5):
            dp[i][0]=(-1)*y
            dp[i][1]=(-1)*x
    print(dp)
    if choice1 == 1:
        p1 = Point(dp[0][0],dp[0][1])
        p2 = Point(dp[1][0],dp[1][1])
        p3 = Point(dp[2][0],dp[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win) 

    elif choice1 == 2:
        rect = Rectangle(Point(dp[0][0], dp[0][1]), Point(dp[1][0],dp[1][1]))
        rect.draw(win)
    
    win.getMouse()
    win.close()

def Shearing(win,choice1,p,sh_mat,sh_choice,s):
    dp = np.zeros((3,3))

    if choice1 == 1:
        p1 = Point(p[0][0],p[0][1])
        p2 = Point(p[1][0],p[1][1])
        p3 = Point(p[2][0],p[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win)
    
    elif choice1 == 2:
        rect = Rectangle(Point(p[0][0], p[0][1]), Point(p[1][0],p[1][1]))
        rect.draw(win)
    
    print(p.shape[0])
    for i in range(p.shape[0]):
        if sh_choice == 1:
            dp[i][0] = p[i][0] + s * p[i][1]
            dp[i][1] = p[i][1]

        elif sh_choice == 2:
            dp[i][0] = p[i][0]
            dp[i][1] = p[i][1] + s * p[i][0] 

    if choice1 == 1:
        p1 = Point(dp[0][0],dp[0][1])
        p2 = Point(dp[1][0],dp[1][1])
        p3 = Point(dp[2][0],dp[2][1])
        vertices = [p1,p2,p3]
        triangle = Polygon(vertices)
        triangle.draw(win) 

    elif choice1 == 2:
        rect = Rectangle(Point(dp[0][0], dp[0][1]), Point(dp[1][0],dp[1][1]))
        rect.draw(win)
    
    win.getMouse()
    win.close()


def main():
    
    print("What would you like to draw ?")
    print("1. Triangle \n2. Rectangle")
    choice1 = int(input("Enter your choice : "))
    
    if choice1 == 1:
        lim = 3
    elif choice1 == 2:
        lim = 2

    cords = []
    for i in range(lim):
        print("\nEnter value for point ",i+1)
        x = int(input("Enter the value of x : "))
        y = int(input("Enter the value of y : "))
        temp = [x,y]
        cords.append(temp)
    p = np.array(cords)
        
        
    print("Choose the Transformation")
    print("1. Translation\n2. Rotation\n3. Scaling\n4. Reflection\n5. Shearing")
    choice2 = int(input("Enter your choice : "))

    if(choice2 == 1):
        print("Translation")
        dx = int(input("Enter the translation of x : "))
        dy = int(input("Enter the translation of y : "))
        T = np.array([[dx],[dy]])
        win = GraphWin('Translation', 720, 720)
        Translation(win,choice1,p,T)
    
    elif(choice2 == 2):
        print("Rotation")
        theta = int(input("Enter the value of theta : "))
        print("1. Anticlockwise \n2. Clockwise")
        rot_choice = int(input("Enter your choice : "))
        win = GraphWin('Rotation', 720, 720)
        Rotation(win,choice1,p,theta,rot_choice)

    elif(choice2 == 3):
        print("Scaling")
        sx = int(input("Enter the scaling of x : "))
        sy = int(input("Enter the scaling of y : "))
        S = np.array([[sx,0],[0,sy]])
        win = GraphWin('Scaling', 720, 720)
        Scaling(win,choice1,p,S)

    elif(choice2 == 4):
        print("Reflection")
        print("Choose the Reflection about ")
        print("1. x-axis \n2. y-axis \n3. origin \n4. y=x \n5. y=-x")
        ref_choice=int(input("Enter your choice : "))
        win = GraphWin('Reflection', 720, 720)
        Reflection(win,choice1,p,ref_choice)
    
    elif(choice2 == 5):
        print("Shearing")
        print("Choose Shearing About")
        print("\n1. X-Axis \n2. Y-Axis")
        sh_choice = int(input("Enter your choice : "))
        theta = int(input("Enter the Shearing Angle : "))
        s = math.tan(theta)
        if sh_choice==1:
            sh_mat = np.array([[1,s],[0,1]])
        elif sh_choice==2:
            sh_mat = np.array([[1,0],[s,1]])
        win = GraphWin('Shearing', 720, 720)
        Shearing(win,choice1,p,sh_mat,sh_choice,s)



if __name__=='__main__':
    main()