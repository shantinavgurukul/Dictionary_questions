# def my_function(lis):
#     a=[]
#     for i in range (len(lis)):
#         check_type=type(lis[i])
#         a.append(check_type)
#     return a
# list1=["shanti","komal",67,89,45.7]
# print(my_function(list1))

def my_function(lis):
    a={}
    for i in range(len(lis)):
        check_type = type(lis[i])
        # a.append(check_type)
        a[lis[i]] =check_type
    return a
list1=["shanti","komal",67,89,45.7,"jaideep","heer",9,89.0]
print(my_function(list1))

def islist():
    return [1,2,3,4]
    
new=islist()
i=0
while(i<len(new)):
    print(new[i])
    i=i+1
print(islist())