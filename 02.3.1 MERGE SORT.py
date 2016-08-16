#####################################################|
#NOTES                                               |
#____________________________________________________|

"""
This script implements the Merge-Sort algorithm for sorting
lists of numbers.
"""

#####################################################|
#IMPORTS                                             |
#____________________________________________________|
from math import floor, ceil
from random import shuffle #used to initialize a random list A


#####################################################|
#FUNCTIONS                                           |
#____________________________________________________|

#This helper function merges two SORTED sub-arrays of A
def MERGE(A,p,q,r):
    sentinel = 99999999999999999

    
    L = A[p:(q+1)]     # |Pythonic way of subarray assign
    R = A[(q+1):(r+1)] # |without for loops

    L.append(sentinel) # |Append Sentinel Values
    R.append(sentinel) # |

    
    for k in xrange(p,r+1):
        if L[0] <= R[0]:
            A[k] = L.pop(0) #| Pythonic way of getting first entry of
        else:               #| L and R. 
            A[k] = R.pop(0) #|


#This function implements the merge-sort algorithm
def MERGE_SORT(A,p,r):
   
    if p < r:                   #DO nothing if base case
        q = int(floor((p+r)/2)) #where to CHOP A: ++>Has to be an int, used for list index<++
        MERGE_SORT(A,p,q)       #recurse on 1st CHOP
        MERGE_SORT(A,q+1,r)     #recurse on 2nd CHOP
        MERGE(A,p,q,r)          #Merge two chops

#####################################################|
#BODY OF SCRIPT                                      |
#____________________________________________________|


A = range(0,10000)    #Prepare a shuffled list
shuffle(A)
print "A= ",A


MERGE_SORT(A,0,len(A)-1)    #SORT A 

print "A= ", A
