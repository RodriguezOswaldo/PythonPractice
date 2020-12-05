import math

# Add your code here

# TODO -> Add welcome function here


def displayWelcome():
    print "welcome to my game"
# TODO -> Add circle area function here
def calcAreaCircle(radius):
    PI = 3.1415
    return PI * radius * radius
# TODO -> Add circle perimeter function here
def calcPerimeterCircle(radius):
    pass
# TODO -> Add square area function here
def calcAreaSquare(side):
    pass
# TODO -> Add Square perimeter function here
def calcPerimeterSquare(side):
    pass
# TODO -> Add rectangle area function here
def calcAreaRect(width, height):
    pass
# TODO -> Add rectangle perimeter function here
def calcPerimeterRect(width, height):
    pass
# TODO -> Add triangle area function here
def calcAreaTriangle(base, height):
    pass
# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))