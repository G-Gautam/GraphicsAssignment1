'''
Module Name: GraphicsWindow
Author: Gautam Gupta
Student #: 250897104
DOC: 01-22-2021

Purpose: 
To draw and display an image on a custom sized canvas made from lines given the start and end point. 
This module implements the Bresenham's algorithm to pick and draw points in between the target points.

Parameters:
width, height: Canvas's size (default value at 640, 480 respectively)
'''

import operator
from PIL import Image
from matrix import matrix

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    '''
    Module Name: drawLine
    Author: Gautam Gupta
    DOC: 01-22-2021

    Purpose: This method implements the Bresenham's algorithm for drawing a straight line between any 2 points

    Parameters: (point1, point2, color)
    point1, point2: A numpy matrix of the custom matrix class. 
                    It consists of 2 columns and 1 row, each containing a number value
    color: A 3 number tuple with values ranging between 0 and 255.

    Output: This method calls the drawPoint method for each computed point to form a straight line between point1 and point2.
    '''
    def drawLine(self,point1,point2,color): 
        # Convert points from matrix to integer lists
        p1 = [int(point1.get(0,0)), int(point1.get(1,0))]
        p2 = [int(point2.get(0,0)), int(point2.get(1,0))]

        delta = point2.__sub__(point1)
        delta_x = delta.get(0,0)
        delta_y = delta.get(1,0)

        # Deciding variables for different slope cases
        steep = negative = False

        # Inverse line if slope > 1
        # X will always be incremented while y_next = y || y + 1
        if(abs(delta_x) < abs(delta_y)):
            delta_x, delta_y = delta_y, delta_x
            p1[0], p1[1] = p1[1], p1[0]
            p2[0], p2[1] = p2[1], p2[0]
            steep = True

        # X positively increments and thus the points are reversed if change in x < 0
        if delta_x < 0:
            return self.drawLine(point2, point1, color)

        # Y may be decremented if the line is negative
        if delta_y < 0:
            negative = True

        delta_x = abs(delta_x)
        delta_y = abs(delta_y)

        p_i = 2 * delta_y - delta_x
        y = p1[1]

        for i in range(p1[0], p2[0]+1):    
            draw_point = [i, y]
            if steep:
                # Undo the inversion before drawing
                draw_point.reverse()
            self.drawPoint(draw_point, color)
            # Determine new p_i and value of increment
            p_i, increment = self.bresenhamIncrement(delta_x, delta_y, p_i)
            if increment:
                # Decrement y if the two points have a negative slope
                if negative:
                    y -= 1
                else:
                    y += 1

    '''
    Module Name: bresenhamIncrement
    Author: Gautam Gupta
    DOC: 01-22-2021

    Purpose: This method is a helper function to determine if the next y value will be incremented or remain unchanged.
             It implements the Bresenham's algorithm

    Parameters: (delta_x, delta_y, p_i)
    delta_x: Positive integer value of change in X
    delta_y: Positive integer value of change in Y
    p_i: An integer of change in Y in relativity to change in X - Bresenhams algorithm's component

    Output: This method returns the new computed p_i for the subsequent point and a boolean value (increment) to determine if y_next = y || y+-1
    '''
    def bresenhamIncrement(self, delta_x, delta_y, p_i):
        increment = False
        if(p_i < 0):
            p_i += 2*delta_y
        else:
            p_i += 2*delta_y - 2*delta_x
            increment = True
        return p_i, increment

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height