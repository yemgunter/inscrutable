# Ch 10.2 Classes


class Rectangle:
    def __init__(self):
        # data attributes __ makes it private
        self.__length = 0
        self.__width = 0
        

    # accessors - method to give access to data attributes
    # these retrieve
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def calc_perimeter(self):
        return 2 * self.__length + 2 * self.__width
    def calc_area(self):
        return self.__length * self.__width

    # these set values
    def set_length(self, l):
        self.__length = l
    def set_width(self, w):
        self.__width = w


def main():
    rectangle1 = Rectangle()

    length1 = int(input("Enter the length of the rectangle: "))
    rectangle1.set_length(length1)
    width1 = int(input("Enter the width of the rectangle: "))
    rectangle1.set_width(width1)

    # UNFINISHED: figure out this part to calc area and perimeter

   
    area1.set_area(area1)
    rectangle1.set_perimeter(perimeter1)

    display_rectangle(rectangle1)

    
def display_rectangle(a_rectangle):
    # call each function
    print("Length: ", a_rectangle.get_length())
    print("Width: ", a_rectangle.get_width())
    print("Perimeter: ", a_rectangle.calc_perimeter())
    print("Area: ", a_rectangle.calc_area())
    





main()
    
