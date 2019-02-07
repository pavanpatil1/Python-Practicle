import math

class Point(object):

    def __init__(self,x,x1,y,y1):

        self.x = x
        self.x1 = x1
        self.y = y
        self.y1 = y1


    @property 
    def x(self):
        return self.__x


    @x.setter
    def x(self,x):
        if x != None and x > 0:
            self.__x = x
        else:
            raise('Invalid')  


    @property 
    def x1(self):
        return self.__x1


    @x1.setter
    def x1(self,x1):
        if x1 != None and x1 > 0:
            self.__x1 = x1
        else:
            raise('Invalid') 


    @property 
    def y(self):
        return self.__y


    @y.setter
    def y(self,y):
        if y != None and y > 0:
            self.__y = y
        else:
            raise('Invalid')


    @property 
    def y1(self):
        return self.__y1


    @y1.setter
    def y1(self,y1):
        if y1 != None and y1 > 0:
            self.__y1 = y1
        else:
            raise('Invalid')   


    @staticmethod
    def cal(x,x1,y,y1):

        return math.sqrt(math.pow(x1 - x,2)+ math.pow(y1 - y,2)*1.0)


def main():
    
    pp = Point(1,2,3,4)
    print "Distance is"
    print Point.cal(1,2,1,2)

if __name__ == '__main__':
    main()





