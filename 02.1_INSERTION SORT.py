# This script will implement the INSERTION-SORT
# from the Algorithms (MIT) book

#####################################################|
#IMPORTS                                             |
#____________________________________________________|
from random import shuffle

#####################################################|
#FUNCTIONS                                           |
#____________________________________________________|

#####################################################|
#DATA                                                |
#____________________________________________________|
A = range(-10,50)
shuffle(A)
print A
#####################################################|
#BODY OF SCRIPT                                      |
#____________________________________________________|

for j in xrange(1,len(A)):
    key = A[j]
    #Insert A[j] into the sorted sequence A[1... j-1]
    i = j - 1
    while (i>-1) and A[i] < key:
        A[i+1] = A[i]
        i = i -1
    A[i+1] = key



print A
    
