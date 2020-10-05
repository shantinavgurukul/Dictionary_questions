# def adjacentElementsProduct(inputArray):
#     for i in range(0, len(inputArray)-1):
#         lis=(inputArray[i]*inputArray[i+1])
#         return lis
# print(adjacentElementsProduct(lis))

# def adjacentElementsProduct(inputArray):
#     lst1 = 0
#     for i in range(0, len(inputArray)-1):
#         lst2 = inputArray[i] * inputArray[i+1]
#         if lst2 > lst1:
#             lst1 = lst2
#     return lst1
# print(adjacentElementsProduct([3, 6, -2, -5, 7,3]))

# def table(n,i):
#   print (n*i)
#   i=i+1
#   if i<=10:
#     table(n,i)
# table(12,1)

# def power(a,b):
#   if b == 1:
#     return a
#   else:
#     return (a*power(a,b-1))
# print( power(6,2))
# def shapeArea(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     for i in range(2,n+1):
#         return (shapeArea(n-1)+(n-1)*4)
# # print(shapeArea(3))
# def shapeArea(n):
#     if n>=10**4 or n<1:
#         return False

#     return (n**2+(n-1)**2)
# print(shapeArea(4))
# def shapeArea(n):
#     if n == 1:
#         return 1
#     return n**2 + (n-1)**2
# print( shapeArea(3))


# statues = [6, 2, 3, 8]
# i=2
# c=0
# a=max(statues)
# # print(a)
# while(i<a):
#     if i not in statues:
#         c=c+1
#     i=i+1
# print(c)
# a=max(statues)
# b=2
# c=0
# for i in range(b,a):
#     if i not in statues:
#         c+=1
        
# print(c)
def almostIncreasingSequence(sequence):
    j=0
    k=0
    i=1
    m=1
    jflag=0
    kflag=0

    dupsequence = list(sequence)

    while i < len(sequence):
        difference = sequence[i]-sequence[i-1]
        if (difference) <= 0:
            j = j+1
            del sequence[i]
            i = 0
            if j > 1:
               jflag = 1
               break

        i = i + 1

    while m < len(dupsequence):
        if (dupsequence[m]-dupsequence[m-1]) <= 0:
            k = k+1
            del dupsequence[m-1]
            m = 0
            if k > 1:
                kflag = 1
                break

        m = m + 1

    if kflag == 0 or jflag == 0:
        return True

    if jflag ==1 and kflag==1:
        return False
print(almostIncreasingSequence([1,2,3,1]))

        









