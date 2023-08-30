#def arithmetic_arranger(problems, values=False):
'''
    Errors:
        1- 5> errors, break. "Error: Too many problems."
        2- only "+" and "-". "Error: Operator must be '+' or '-'."
        3- only numbers in the.. numbers. "Error: Numbers must only contain digits."
        4- each number has max 4 digits "Error: Numbers cannot be more than four digits."
'''

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
values = False  #optional
left = []
operator = []
right = []
answer = []  #optional if values = True

#get items in their own lists
for line in list:

    #check to make sure there are <= 5 entered problems
    if len(list) > 5:
        print("Error: Too many problems.")
        break

    newlist = line.split()  #>>> ["32", "+", "698"]

    #check is both left and right operand are only numbers
    if newlist[0].isnumeric() == False or newlist[2].isnumeric() == False:
        print("Error: Numbers must only contain digits.")
        break
    else:
        #check to make sure no number is greater than 4 digits
        if len(newlist[0]) > 4 or len(newlist[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            break
        else:
            left.append(newlist[0])
            right.append(newlist[2])

    #check that we are only supplying addition or subtraction
    if newlist[1] == "+" or newlist[1] == "-":
        operator.append(newlist[1])
        #get answers
        if newlist[1] == "+":
            answer.append(int(newlist[0]) + int(newlist[2]))
        elif newlist[1] == "-":
            answer.append(int(newlist[0]) - int(newlist[2]))
    else:
        print("Error: Operator must be '+' or '-'.")
        break


#format printing
'''
Left: ['32', '3801', '45', '123']
Operator: ['+', '-', '+', '+']
Right: ['698', '2', '43', '49']
Answers: [730, 3799, 88, 172] *optional

   32      3801      45      123              Left
+ 698    -    2    + 43    +  49    Operator Right
-----    ------    ----    -----    Line------Line (4 spaces)  
'''

for i in left:
    print("{:>}".format(i), end="    ")

#sanity check
#print("Left Number: {}\nOperator: {}\nRight Number: {}\nAnswers: {}".format(left, operator, right, answer))

#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# Run unit tests automatically
#main(['-vv'])
