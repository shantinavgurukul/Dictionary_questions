# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

thislist1={}
thislist1['name']="ravina"
thislist1['age']=22
thislist1['school name']="RSKVkalyanpuri"
thislist1['Id number']=123453213
thislist1['class']="BCOM"
# print(thislist1['age'])
x=thislist1.get("age")
# print(x)
# for x in thislist1:
#     print(thislist1[x])


for x,y in thislist1.items():
    print(x,y)



