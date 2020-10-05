dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
total=0
for value in dict1:
    value_list = dict1[value]
    count = len(value_list)
    total += count

print(total)
