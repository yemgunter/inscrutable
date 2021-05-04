class Rectangle:
    def __init__(self, l, w):
        # data attributes __ makes it private
        self.__length = l
        self.__width = w
        

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

    def __str__(self):
        return "Length: " + str(self.__length) + '\n' \
               "width: " + str(self.__width)
               
                
