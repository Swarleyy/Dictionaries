# In[6]:
#to add a key and value to a dict
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Dictionary:", my_dict)

# In[10]:
#to concatenate the following dict to create a new one
dict1={1: 10, 2: 20}
dict2={3: 30, 4: 40}
dict3={5: 50, 6: 60}
new_dict={}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)
print("Updated Dictionary:",new_dict)

# In[8]:
#to check if a given key exists in dict
my_dict={101:"Amit", 102:"Rahul", 103:"Priya"}
key=int(input("Enter key to search:"))
if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exists in the dictionary")

# In[2]:
#to iterate over a dict using for loop and print the keys alone values alone and both keys and values
my_dict={101:"krishna",
         102:"amit",
         103:"rahul"}

print("Key:")
for key in my_dict:
  print(key)
print("Values")
for value in my_dict.values():
  print(value)
print("Keys and Values:")
for key,value in my_dict.items():
  print(key,value)

# In[3]:
#to prepare a dict where keys are in numbers bw 1 to 15 and values are sq of keys
my_dict={}
for i in range(1,16):
    my_dict[i]=i**2
print("Dictionary:",my_dict)

# In[4]:
#sum all the values in dict
my_dict={0: 10, 1: 20, 3: 30, 4: 40, 5: 50, 6: 60}
total=0
for value in my_dict.values():
    total=total+value
print("Sum of the values of dictionary =",total)

# In[3]:
#assign 5 elements of student info and then add and dlt 
my_dict={
101:"Amit",
102:"Rahul",
103:"Priya",
104:"Sneha",
105:"Krishna"
}
print("Original Student List:")
print(my_dict)

# In[4]:
#add student in above
my_dict[106]="Rohan"
print("\nAfter Adding Student:")
print(my_dict)

# In[6]:
#dlt student from above
my_dict={
101:"Amit",
102:"Rahul",
103:"Priya",
104:"Sneha",
105:"Krishna"
}
del my_dict[103]
print(my_dict)

# In[7]:
#display student info
print("n\Student Information:")
for roll_no,name in my_dict.items():
  print("Roll No:",roll_no,"Name:",name)

# In[9]:
#convert list into dict
list1=['name','panel','division']
list2=['krishna','3','4']
my_dict=dict(zip(list1,list2))
print('Dictionary',my_dict)

# In[10]:
my_dict={}
for i in range(1,6):
    my_dict[i]=float(input("Enter the marks"))
total=sum(my_dict.values())
mean=total/len(my_dict)
print("Mean of all values",mean)
print("Dictionary",my_dict)

# In[12]:
my_dict={
    "Name":"krishna",
    "Roll no.":15,
    "Division":4,
    "Marks":[87,92,87,85,89]
}
sorted_dict=sorted(my_dict)
print("Sorted keys",sorted_dict)

# In[13]:
students={
    "krishna":96,
    "Shruti":94,
    "Saumya":90,
    "chhavi":89,
    "Kushagra":99
}
highest_student=max(students,key=students.get)
print("student with highest marks:",highest_student)
print("highest marks:",students[highest_student])

# In[14]:
my_dict={
    "krishna":96,
    "Shruti":94,
    "Saumya":90,
    "chhavi":89,
    "Kushagra":99
}
sorted_dict=(dict(sorted(my_dict.items(),key=lambda item:item[1])))
print("Dictionary sorted by values:",sorted_dict)
