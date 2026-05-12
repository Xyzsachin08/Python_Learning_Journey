def minimumu_rotation(arr1,arr2):
    n = len(arr1)
    
    if n != len(arr2):
        return -1
    
    for i in range(n):
        rotation = arr1[i: ]  + arr1[ :i]
        
        if rotation == arr2:
            left_side = i
            right_side = n-i
            
            return min(left_side,right_side)
    
    return -1

arr1 = [3,4,5,1,2]
arr2 = [1,2,3,4,5]
print("minimum rotations is : ",minimumu_rotation(arr1,arr2))
            
        