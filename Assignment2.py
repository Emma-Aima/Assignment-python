#Write the following code in the code editor below:

#Create an empty list called my_list
My_list = []

#Append the following items to my_list: 10, 20, 30, 40
for i in [10, 20, 30, 40]:
    My_list.append(i)

#Insert the value 15 at the second position in the list
My_list.insert(1, 15)

#Extend my list with another list: [50, 60, 70]
My_list.extend([50, 60, 70])

#Remove the last elements from my_list.
My_list.pop()

#Sort my_list in ascending order.
My_list.sort()

#Find and print the index of the value 30 in my_list.
print(My_list.index(30))

#Print the length of my_list.
print(len(My_list))