#Filing Handling

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



file = open("Deck.txt", "r+")
for line in file:
	line = line[2:]
	file.write(line)
file.close()


import fileinput

#Rewrite a MTG Deck list to remove "1 " and rewrite over line.
with fileinput.input("Deck.txt", inplace=True) as file:
	for line in file:
		new_line = line.replace(line, line[2:])
		print(new_line, end='')
fileinput.close()
