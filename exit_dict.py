# dict={'name':'Raju', 'marks':56}
# if "name" in dict:
#     print("exit")
# else:
#     print("not exit")


# def my_dict_exit(dict):
#     if "name" in dict:
#         return("exit")
#     else:
#         return("not exit")
# print(my_dict_exit(dict))


summ = 0
count = 1
while input("Enter q to quit or any other key to continue") != 'q':
    summ = summ+input()
    count=count+1
print (summ/(count*1.0))