#Indexing
nums = [10, 20, 30, 40]

print(nums[0])   # 10
print(nums[2])   # 30



#Negative Indexing
print(nums[-1])  # 40
print(nums[-2])  # 30




#Slicing (Get part of list)
nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[2:])    # [30, 40, 50]
print(nums[::-1])  # reverse list




#List Methods
lst = [1, 2, 3]

lst.append(4)        # [1,2,3,4]
lst.insert(1, 10)    # [1,10,2,3,4]




#Remove elements
lst.remove(10)   # remove value
lst.pop()        # remove last
lst.pop(1)       # remove index



#Other useful methods
lst.sort()       # ascending
lst.reverse()    # reverse
len(lst)         # length
lst.count(2)     # count occurrences
lst.index(3)     # find index



#Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(matrix[1][2])  # 6



#List Comprehension
#Normal way 
squares = []
for i in range(5):
    squares.append(i*i)
    
    
#List comprehension
squares = [i*i for i in range(5)]