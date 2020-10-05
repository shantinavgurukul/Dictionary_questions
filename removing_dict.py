# a= [1,2,3,4,5]
# a = a + [6]
# print(a)
# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)



# a = " harshita is a girl"
# ab = a.split()
# print(ab)
# b = a.title()
# print(b)
# def delete_(details):

#     del (details['place'])
#     return details

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# print(delete_(person))

# list1=["s",56,89.2,"f"]
def my_function(lis):
    a=[ ]
    for ele in range(len(lis)):
        type_ele=(type (lis [ele]))
        list_ele=lis[ele]
        a.append(type_ele)
        a.append(list_ele)
    return a
list1=[23,"dfg",6.8]
fyn=my_function(list1)
print(fyn)




# def my_function(shanti):
#     for i in range(0,len(list1)):
#         a=[]
#         a.append(list1[i])
#         a.append(type(i))
#     return a
# list1=["s",56,89.2,"f"]
# print(my_function(list1))



