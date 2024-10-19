def divi(n):
    if(n%5==0):
        return True
    return False
    
a=[1,2,34567,6234456,6548465,684465,3541654,5315]
divi=filter(divi,a)
print(list(divi))