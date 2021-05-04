# Ch 10.2 Classes

import rectangle_class

def main():
    

    length1 = int(input("Enter the length of the rectangle: "))
    
    width1 = int(input("Enter the width of the rectangle: "))
    
    rectangle1 = rectangle_class.Rectangle(length1, width1)

    print(rectangle1)
    
    display_rectangle(rectangle1)
    
    rectangle1.set_length(100)

    display_rectangle(rectangle1)

    
def display_rectangle(a_rectangle):
    # call each function
    print("Length: ", a_rectangle.get_length())
    print("Width: ", a_rectangle.get_width())
    print("Perimeter: ", a_rectangle.calc_perimeter())
    print("Area: ", a_rectangle.calc_area())
    





main()
    
