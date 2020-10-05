Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
# del (Dic[3]["A"])
# print(Dic)

def my_dict_del(Dic):
    del (Dic[3]["A"])
    return Dic
print(my_dict_del(Dic))



























# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# c = float(input("Input third number: "))
# if a > b:
#     if a < c:
#         median = a
#     elif b > c:
#         median = b
#     else:
#         median = c
# else:
#     if a > c:
#         median = a
#     elif b < c:
#         median = b
#     else:
#         median = c

# print("The median is", median)