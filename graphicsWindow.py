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
        p1 = [int(point1.get(0,0)), int(point1.get(1,0))]
        p2 = [int(point2.get(0,0)), int(point2.get(1,0))]

        steep = negative = False

        delta_x = p2[0] - p1[0]
        delta_y = p2[1] - p1[1]

        if abs(delta_y) > abs(delta_x): 
            p1[0], p1[1] = p1[1], p1[0]
            p2[0], p2[1] = p2[1], p2[0]
            delta_x = p2[0] - p1[0]
            delta_y = p2[1] - p1[1]
            steep = True

        p_i = 2 * delta_y - delta_x
        y = p1[1]

        for i in range(p1[0], p2[0]+1):    
            draw_point = [i, y]
            if steep:
                draw_point.reverse()
            self.drawPoint(draw_point, color)
            p_i, increment = self.bresenhamIncrement(delta_x, delta_y, p_i)
            if increment:
                y += 1

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