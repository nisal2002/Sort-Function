old_list = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
new_list=[]

while len(old_list)>0:
    minimum=min(old_list)
    new_list.append(minimum)
    old_list.remove(minimum)
else:
    print(new_list)