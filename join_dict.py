# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,] 
# res = {} 
# for key in list1: 
#     for value in list2: 
#         res[key] = value 
#         list2.remove(value) 
#         break 
# print(str(res))

def join_dict(list1,list2):
    my_list = {}
    i = 0
    while i < len(list1):
        a = {list1[i]:list2[i]}
        my_list.update(a)
        i = i + 1
    return my_list
print(join_dict(["one","two","three","four","five"],[1,2,3,4,5,] ))



