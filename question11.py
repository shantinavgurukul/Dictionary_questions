my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
first_max=0
sec_max=0
third_max=0
for i in my_dict:
    for j in my_dict:
        if my_dict[j]>first_max:
            first_max=my_dict[j]
        if first_max>my_dict[j] and my_dict[j]>sec_max:
            sec_max=my_dict[j]
        if sec_max>my_dict[j] and my_dict[j]>third_max:
            third_max=my_dict[j]
print(first_max)  
print(sec_max)
print(third_max)



