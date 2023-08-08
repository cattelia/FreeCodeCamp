#Sorting List of Tuples
d = {"a":10, "b":1, "c":22}
print(d.items())



#Sorting Tuples in Dictionary
d = {"a":10, "b":1, "c":22}
d.items()
#dict_items([{"a":10, "b":1, "c":22}])
sorted(d.items())
#>>> [{"b":1, "a":10, "c":22}]


d = {"a":10, "b":1, "c":22}
t = sorted(d.items())
print(t)
#>>> [{"b":1, "a":10, "c":22}]
for k, v in sorted(d.items()):
    print(k,v)



c = {"a":10, "b":1, "c":22}
#initialize an empty list
tmp = list()
for k,v in c.items():
    #flip the key and value in the list of tuples
    tmp.append((v, k))
tmp = sorted(tmp, reverse=True)
print(tmp)




#Find the most common words in a file
fhand = open("mobe.txt") #open a file as read only
counts = dict() #initilize an empty dict
for line in fhand:
    words = line.split() #split by spaces
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #If no word exists in dict, at it at 1 or +1 on existing words.
    
lst = list()
for key, val in counts.items(): 
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)




#Do this by a list comprehension. Let's go back to our "c" variable.
c = {"a":10, "b":1, "c":22}
print( sorted ( [ (v,k) for k, v in c.items() ] )) #generator for all of the elements
# [(1, 'b'), (10, 'a'), (22, 'c')]
#Let's try it without sorted()
print( [ (v,k) for k, v in c.items() ] )
# [(10, 'a'), (1, 'b'), (22, 'c')]





#Tuples with Dictionary Tuple Output

#Tuples are immutable, which means that they cannot be modified, meaning we can modify slots.
#CANNOT: .sort(), .append(), .reverse() | CAN: 

a = ("Joseph", "Seth", "Ami", "Margot", "Jerry")
(x, y) = (4, "Joe")

d = dict()
d['Joseph'] = 1
d['Seth'] = 2
d['Ami'] = 3
d['Margot'] = 4
d['Jerry'] = 5
for (k,i) in d.items():
    print(k,i)
