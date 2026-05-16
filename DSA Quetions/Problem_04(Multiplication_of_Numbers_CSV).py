s = "1,2,0,3,-2"

nums = s.split(',')
product = 1
for x in nums:
    num = int(x)
    if num !=0:
        product = product*num
print(product)