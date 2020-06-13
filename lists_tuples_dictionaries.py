# 1.)ASSIGNING ELEMENTS TO A LIST:

#Method 1- using .append():

l1= []
l1.append(1)
l1.append(2)
print(l1)
'''
Output: 
[1,2]
'''

l2=[3,4,5]
l1.append(l2)
print(l1)
'''
Output:
[1,2,[3,4]]
'''

fruits=['Pineapple','Strawberry']
fruits.append('Mango')
print(fruits)
'''
Output:
['Pineapple','Strawberry','Mango']
'''

#Method 2- using .extend():

fruits2=['Cherry','Watermelon']
fruits.extend(fruits2)
print(fruits)
'''
Output:
['Pineapple','Strawberry','Mango','Cherry','Watermelon']
'''

#Method 3- using .insert():

fruits.insert(0, 'Muskmelon')
print(fruits)
'''
Output:
['Muskmelon','Pineapple','Strawberry','Mango','Cherry','Watermelon']
'''

#Method 4- using list():

mylist=list(2,3,5,7)
print(mylist)
'''
Output:
[2,3,5,7]
'''

# 2.)ACCESSING ELEMENTS FROM A TUPLE:

tup=(1,2,3,'Sushi','Puppy',5,'Rain',7,11)
tup[0]
''' Output: 1'''
tup[2:5]
'''Output: (3,'Sushi','Puppy')'''
tup[::2]
'''Output: (1,3,'Puppy','Rain',11)'''
tup[::-1]
'''Output: (11,7,'Rain',5,'Puppy','Sushi',3,2,1)'''

# 3.)DELETING DICTIONARY ELEMENTS:

#Method 1- using .pop():
'''
Removes the element and returns the popped element, unless specified otherwise.
'''

dict= {'k1':123,'k2':['a','b','c'],'k3':{'insideKey':100},'k4':food}
dict.pop('k2')
print(dict)
'''Output: {'k1':123,'k3':{'insideKey':100},'k4':food}'''
 
#Method 2- using del:

del dict['k1']
print(dict)
'''Output: {'k3':{'insideKey':100},'k4':food}
