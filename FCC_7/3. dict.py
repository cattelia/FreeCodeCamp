#Filing Handling and Counting w/ Dictionary

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




#Dictionary
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





