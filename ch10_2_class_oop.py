# Ch 10.2 Classes


class Rectangle:
    def __init__(self):
        # data attributes __ makes it private
        self.__length = 0
        self.__width = 0
        self.__perimeter = 0
        self.__area = 0

    # accessors - method to give access to data attributes
    # these retrieve
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def get_perimeter(self):
        return self.__perimeter
    def get_area(self):
        return self.__area

    # these set values
    def set_length(self, l):
        self.__length = l
    def set_width(self, w):
        self.__width = w
    def set_perimeter(self, p):
        self.__perimeter = p
    def set_area(self, a):
        self.__area = a



def main():
    rectangle1 = Rectangle()

    length1 = int(input("Enter the length of the rectangle: "))
    rectangle1.set_length(length1)

    # directly accessed from data attribute - blasphemy!
    # and ignored
    rectangle1.__length = 99

    # use the rectangle
    length1 = rectangle1.get_length()
    print("Length is", length1)
    





main()
    
