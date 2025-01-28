
my_list = [10, 20, 30, 40, 50]
my_list1= [1, 2, 3, 4, 5]

#cmp(my_list,my_list1)
print("length of list:",len(my_list))
 
print("minimum number in list:",min(my_list))

print("maximum number in list:",max(my_list))

popped_element = my_list.pop()
print(f"Element popped:",popped_element)
print(f"List after pop:",my_list)




print("Accessing the third item:", my_list[2])  


my_list.append(60)  
print("List after adding an item:", my_list)

my_list.extend([40,50])  
print("List after extend an item:", my_list)


my_list.remove(20) 
print("List after removing an item:", my_list)


del my_list  

