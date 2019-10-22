from numpy import linspace, zeros, mean
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from random import randint, randrange, uniform


h = np.array([1.60,1.85, 1.75, 1.80])


H = np.array([0.50, 0.70, 1.90,  1.75])

family_member_no = np.array(range(0,4))

plt.plot(family_member_no, h)
plt.plot(family_member_no, H)

plt.xlabel('Number of family members')
plt.ylabel('Height (m)')
plt.show()



######################Exercice 1.2

def volume(L):

    """A function that returns the volume of a cube given
    the lenght of the sides """

    vol = L**3

    return vol

print(volume(4))


#Exercise 1.3

def cir_and_area(radius):
    """"A function that returns the circumference and the area of a Circle"""

    Cir = 2 * pi * radius

    Area = pi * radius**2

    return Cir, Area

print(cir_and_area(2))


#Exercise 1.4

def some_volume():
    """A function that returns some Volume every time it's called"""

    L = linspace(1,3,3)

    V = [l**3 for l in L]

    plt.plot(L, V)
    plt.ylabel('Volume')
    plt.xlabel('Length')

    plt.show()

some_volume()

#Exercise 1.5

def averages(*args):
    """A functions that returns the averages of the arguments"""
    
    numbers = []

    for i in args:
        numbers.append(i)

    media = mean(numbers)

    return media

print(averages(1,2,3,4,5))

#Exercise 1.8

def mult_by_pi(number):
    """function that prints a value multiplied by pi"""
   
    result = pi * number

    print("Multiplying {number} and {p} gives {result}".format(number = number,result = result, p = pi))

mult_by_pi(2)


#Exercise 1.10

def clearly_random(how_many = 3):
    """a function that returns a certain amount of sudo-random numbers
    accourdingly to the how_many argument"""

    numbers = []

    i = 0
    while i < how_many:
        numbers.append(uniform(0,10)) 
        i += 1

    print(numbers)

clearly_random()


#Exercise 2.5 - Area of a Polygon

def poly_area(x, y): #x and y are either list or arrays
    """A function that returns the area of a polygon
    given the arrays/lists x and y are the vertices"""

    x_result = []
    y_result = []

    i = 0
         
    for i in x:
        if i != len(x):
            x_result.append(x[i] * y[i + 1])
        else:
            x_result.append(x[-1] * y[0])


    
    for j in y:
        if i != len(x):
            y_result.append(y[j] * x[ j + 1])
        else:
            y_result.append(y[-1] * x[0])

    print (x_result, y_result) 


a = [1, 2, 3]

b = [3, 2, 1]

poly_area(a, b)
