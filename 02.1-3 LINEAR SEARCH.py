#####################################################|
#NOTES                                               |
#____________________________________________________|
"EXERCISE 2.1-3 of the Algorithms MIT book"

"""
-> LOOP INVARIANT:  <-
    j holds either (-1) or an index i such that A[i] == v

    INITIALIZATION:
    Loop invariant is true before first iteration since j is set to -1
    before first iteration

    MAINTENANCE:
    Inside loop the j is left as it was before the iteration i:
    ( j = -1 or j = k such that A[k] = v )
    or:
    (j is changed in the iteration to j = i  such that A[i] == v )

    TERMINATION:
    Loop terminates when i > A.length
    At this point j is either -1 or k such that A[k] == v   ,
    since the last loop iteration preserved the invariant.
    The algorithm has iterated over A and found a match
    or it has returned with j == -1 unchanged
    


"""
#####################################################|
#IMPORTS                                             |
#____________________________________________________|
from random import shuffle,choice

#####################################################|
#FUNCTIONS                                           |
#____________________________________________________|


#####################################################|
#DATA                                                |
#____________________________________________________|
A = range(0,50)
shuffle(A)
print "A = " , A

#####################################################|
#BODY OF SCRIPT                                      |
#____________________________________________________|
v = choice([choice(A),choice(A),choice(A),choice(A),-100])
j = -1

for i in xrange(0, len(A)): #MAIN LOOP
    if A[i] == v:
        j = i




#MESSAGE
if j == -1:
    m = " not found in A"

else:
    m = " found in A at index " + str(j)
    


message = "\nvalue " + str(v) +m

print message


