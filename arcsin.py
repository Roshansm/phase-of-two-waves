import numpy as np
def func (a,b):
    c=a/b
    arcsin_Values = np.arcsin(c)
    degree=arcsin_Values*180/np.pi
    print ("\nInverse Sine values : \n", degree)
while True:
    a=float(input())
    b=float(input())
    func (a,b)
    
