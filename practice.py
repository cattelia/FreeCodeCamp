#This is a new comment
#Figure out why Visual Studio is not opening the most recent updates.
# Vim is what you should be using. Even if it is weird.
import urllib.request, urllib.parse, urllib.error

fhand = urllib.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

for line in fhand:
    print(line.decode().strip())


'''

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
'''


#Tuples with Dictionary Tuple Output
'''
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
'''



#Filing Handling and Counting w/ Dictionary
'''
counts = dict()
file = open('mobe.txt', "r")
for line in file:
    line = line.strip()
    if line.startswith("X-DSPAM"):
    	print(line)
    #counts[line] = counts.get(line, 0) + 1
print("Counts: {}".format(counts))

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
'''



#Dictionary
'''
icts = {}
icts["cat"] = 0
icts["dog"] = 1
icts["bunny"] = 2
print(icts) 
print(icts["bunny"])

counts = dict()
friends = ["Joseph", "Seth", "Ami", "Margot", "Jerry", "Ami","Joseph","Seth","Ami"]
for name in friends:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1

print("This is the for:if:else loop for\n {}".format(counts))

counts = dict()
friends = ["Joseph", "Seth", "Ami", "Margot", "Jerry", "Ami","Joseph","Seth","Ami"]
for name in friends:
	#Does the exact same thing as the code above this but .get() sets a default if key is not there.
	counts[name] = counts.get(name, 0) + 1
print("This is the single for loop for\n {}".format(counts))
'''



#List Handling
'''
friends = ["Joseph", "Seth", "Ami", "Margot", "Jerry"]
print("Not sorted: {}".format(friends))
sorted = friends.sort()
print("Sorted: {}".format(friends))

#for friend in friends:
    #print("Happy New Year {}!".format(friend))
    
for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year {}! (Position: {})".format(friend, i))
    
a = ["a","b","c"]
b = [1,2,3]
c = a + b
'''



#Printing on the same line
'''
print("Hello ", end="")
print("{}!".format(friends[0]))
'''



#Filing Handling
'''
fhandle = open("mobe.txt")

fname = input("Enter file you want to search: ")
check = open(fname)
count = 0
for line in check:
    if line.startswith('Subject:'):
        count += 1
print("There were {} lines with the word, 'Subject:' in it.".format(count))


fhandle = open("mobe.txt")
count = 0
newline = 0
for line in fhandle:
	if line == "\n":
		newline += 1
	count += 1
print("Line count: {}\nNewline count: {}\n".format(count, newline))
#>>> <_io.TextIOWrapper name='mobe.txt' mode='r' encoding='UTF-8'>

fhand = open("mobe.txt")
#inp = fhand.read()
#print(len(inp))
#print(inp[:20])

for line in fhand:
	if line.startswith("From:"):
		print(line.strip())

str = "X-DSPAM-Confidence: 0.8475 "
#print(str)
cpos = str.find(':')
piece = str[cpos+1:].strip(" ")
piece = float(piece)
#print("{}%".format(piece))
'''



#Decorator Testing
'''
from functools import lru_cache

@lru_cache #lru - least recently used DECORATOR
def increment(number):
	print("Running code")
	return number+1

#print("\n")
#print(increment(1))
#print(increment(2))
#print(increment(5))
#print(increment(1))
#print(increment(1))
#print(increment(2))
#print("\n")
'''



# *args Testing
'''
def check(*list):
	for i in list:
		print(i)

list1 = [1,2,3,4,5]
list2 = [6,7,8]
#check(list1)
#check(list2)

smallest = None
for item in [3,41,12,9,74,15]:
    if smallest is None or item < smallest:
        smallest = item
        print("Loop: ", item, smallest) 
print("Smallest: ", smallest)
'''



#CLEAN Python Input Handling
'''
def do_this():
    print("Doing this")
    
def do_that():
    print("Doing that")
    
match input('Do this or that? '):
    case "this":
        do_this()
        
    case "that":
        do_that()
        
    case _:
        print("Invalid Input!")
'''
'''