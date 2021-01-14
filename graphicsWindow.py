'''
Module Name: GraphicsWindow
Author: Gautam Gupta
Student #: 250897104
DOC: 01-22-2021

Purpose: 
To draw and display an image on a custom sized canvas made from lines given the start and end point. 
This module implements the Bresenham's algorithm to pick and draw points in between the target points.
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
        if(abs(delta_x) < abs(delta_y)):
            delta_x, delta_y = delta_y, delta_x
            p1[0], p1[1] = p1[1], p1[0]
            p2[0], p2[1] = p2[1], p2[0]
            steep = True

        if delta_x < 0:
            return self.drawLine(point2, point1, color)

        if delta_y < 0:
            negative = True

        delta_x = abs(delta_x)
        delta_y = abs(delta_y)

        p_i = 2 * delta_y - delta_x
        y = p1[1]

        for i in range(p1[0], p2[0]+1):    
            draw_point = [i, y]
            if steep:
                draw_point.reverse()
            self.drawPoint(draw_point, color)
            p_i, increment = self.bresenhamIncrement(delta_x, delta_y, p_i)
            if increment:
                if negative:
                    y -= 1
                else:
                    y += 1

    # Helper function to compute if y_next will increment or stay the same
    # Accepts and returns p_i value for subsequent computations 
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