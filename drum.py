import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
out_file = open("myfile.json", "w")
# a=write(o)  
# store=json.dumps(dict1,indent = 6)
  
# # out_file.close()
# print(store)
json.dumps(out_file,indent=4)
print(out_file)