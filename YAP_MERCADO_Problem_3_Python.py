from math import *
import numpy as np
import pandas as pd
#  r x c; c=2
#input n x 2, where n is th number of rows
r = int(input('Number of rows: '))

print("Values of matrix from left to right:") #enter the values of the points at one command line spaced evenly (example: 1 2 3 4 - point 1 is 1,2)
a = list(map(int,input().split()))
A = np.array(a).reshape(r,2)
X = A[:,0]
Y = A[:,1]
print(' ')
print(' ')

#size of matrix A is assigned to variable le
le = len(A)

#make a loop for the degree
for d in range(le):
    pf = np.polyfit(X,Y,d)
    pv = np.polyval(pf,X)
    e = Y - pv
    en = np.linalg.norm(e)
    x=[d,en]
    if n == 0:
         y = x
    elif y[1] >= x[1]:
        z = x[0]
    pf = np.polyfit(X,Y,z)
    #print the coefficients of the best polynomial fit
    print('The coefficients for the best fit is: ')
    print(np.around(pf,2))

        