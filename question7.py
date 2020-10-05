uniques_number=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]

temp_list = []
for item in uniques_number:
    for value in item.values():
        temp_list.append(value)
print(set(temp_list))
# list1 =[] # create empty list
# for val in uniques_number.values(): 
#   if val in list1: 
#     continue 
#   else:
#     list1.append(val)

# print (list1)