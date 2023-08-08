#List Handling

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