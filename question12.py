# n=int(input("Enter a number:"))
# # d={x:x*x for x in range(1,n+1)}
# for x in range(1,n+1):
#     d={x:x*x}
# print(d)

# declare and assign n
n = 15

# declare dictionary 
numbers = {}

# run loop from 1 to n 
for i in range(1, n+1):
	numbers[i] = i * i

# print dictionary 
print (numbers)