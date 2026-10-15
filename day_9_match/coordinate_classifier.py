x = int(input("Enter x co-ordinate:")) 
y = int(input("Enter y co-ordinate:"))

tpl = (x,y)

match tpl:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("Y-Axis")
    case (x, 0):
        print("X-Axis")
    case (x,y):
        print("General Point")
    case _:
        print("Invalid!")