l=[1,2,3,4,5]
# square= lambda x:x*x
# sqlist=map(square,l)
# print(list(sqlist))
# #filter
def even(n):
    if (n%2 ==0):
        return True
    return False
onlyEven=filter(even,l)
print(list(onlyEven))
#reduceEXample
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))
