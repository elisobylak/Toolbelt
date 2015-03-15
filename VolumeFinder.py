__author__ = 'Eli Sobylak'
#Finds the dimensions for some select shapes given a volume in cubic feet
import math

input = int(input("Please enter a volume in cubic feet: "))
pi = math.pi

def cube ():
    vcube = str(round((nthroot(input,3.0)),2))
    print("Cube: "+" "+vcube+"ft width"+" "+vcube+"ft height"+" "+vcube+"ft length")

def sphere ():
    rsphere = str(round((nthroot(3 * input/(4 * pi),3)),3))
    print("Sphere: "+rsphere+"ft Radius")


def nthroot (x, n):     #Newton-Raphson method#
        r = 1
        for i in range(16):
                r = (((n - 1) * r) + x / (r ** (n - 1))) / n
        return r

cube()
sphere()
