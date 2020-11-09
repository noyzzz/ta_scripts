import random
high_bound = int(input("number of groups\n")) 
not_send_exist = True if input("did all the groups send the assignment(y/n) \n") == "y" else False
print("now enter id of groups who didin't send the assignment\n")
remove_list = []
if not_send_exist:
	a = input()
	while(a != -1):
		remove_list.append(int(a));
		a = int(input("enter next group number\n "))
my_list = range(1,high_bound+1)

my_list = list(set(my_list) - set(remove_list))
random.shuffle(my_list)

pair_list = []
print(my_list)

for i in range(1,len(my_list),2):
	pair_list.append((my_list[i],my_list[i-1]))
if len(my_list) %2 != 0:
	pair_list.append((my_list[len(my_list)-1],my_list[0]))
print(pair_list)