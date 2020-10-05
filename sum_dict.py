my_dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
       }
# sum=0 
# for x in my_dict:
#     # sum=0
#     sum=sum+my_dict[x]
# print(sum)
def my_dict_sum(sum):
    sum=0
    for x in my_dict:
        sum=sum+my_dict[x]
    return sum
print(my_dict_sum(my_dict))



# a=[67,89,56,45,23]
# # b=len(a)
# # print(b)
# for i in range(len(a)):
#     print(a[i])

