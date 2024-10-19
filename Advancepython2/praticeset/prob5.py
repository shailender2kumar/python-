from functools import reduce
l=[1,2,3,4,5,6,7,8]
 
def maxi(a,b):
    if(a>b):
        return a
    return b
    

print(reduce(max,l))

    