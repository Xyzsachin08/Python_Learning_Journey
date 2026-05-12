def maximum_product(arr):
    maxP = arr[0]
    minP = arr[0]
    ans = arr[0]
    
    for i in range(1,len(arr)):
        current = arr[i]
        
        tempMax = max(current,
                   current * maxP, 
                   current * minP
                   )
        tempMin = min(current, 
                   current * maxP, 
                   current * minP
                   )
        
        maxP = tempMax
        minP = tempMin
        
        ans = max(ans, maxP)
    return ans

arr = [2,3,-2,4]
print(maximum_product(arr))
    
        
        
    