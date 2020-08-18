import numpy as np
import cv2
import math

def scaling(img,coords):
    img = img
    scaling_factor = 2
    new_x = coords[0][0] * scaling_factor
    new_y = coords[0][1] * scaling_factor
    new_length = coords[1][0] * scaling_factor
    new_breadth = coords[1][1] * scaling_factor
    new_coords = []
    t1 = tuple()
    t2 = tuple()
    t1 = ((new_x,new_y))
    t2 = ((new_length,new_breadth))
    new_coords.append(t1)
    new_coords.append(t2)
    print(new_coords)
    img = cv2.rectangle(img,(coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),(0,255,0),3)
    img = cv2.rectangle(img,(new_x,new_x),(new_length,new_breadth),(0,0,255),3)
    cv2.imshow("Scaling",img)
    cv2.waitKey(0)


def get_data():
    coords = []
    x = int(input("Enter the X - Coordinate : "))
    y = int(input("Enter the Y - Coordinate : "))
    length = int(input("Enter the Length of the Rectangle : "))
    breadth = int(input("Enter the breadth of the Rectangle : "))
    t1 = tuple((x,y))
    t2 = tuple((length,breadth))
    coords.append(t1)
    coords.append(t2)
    print(coords)
    return coords


if __name__=='__main__':
    img = np.zeros((1024,1024,3), np.uint8)
    img.fill(255)
    coords = get_data()
    scaling(img,coords)