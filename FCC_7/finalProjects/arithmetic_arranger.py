#list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems, values=False):
    '''
        Errors:
            1- 5> errors, break. "Error: Too many problems."
            2- only "+" and "-". "Error: Operator must be '+' or '-'."
            3- only numbers in the.. numbers. "Error: Numbers must only contain digits."
            4- each number has max 4 digits "Error: Numbers cannot be more than four digits."
    '''
    top = ""
    bottom = ""
    dash = ""
    totals = ""

    #get items in their own lists
    for line in problems:

        #check to make sure there are <= 5 entered problems
        if len(problems) > 5:
            return("Error: Too many problems.")

        newlist = line.split()  #>>> ["32", "+", "698"]

        #check is both left and right operand are only numbers
        if newlist[0].isnumeric() == False or newlist[2].isnumeric() == False:
            return("Error: Numbers must only contain digits.")
        #check to make sure no number is greater than 4 digits
        elif len(newlist[0]) > 4 or len(newlist[2]) > 4:
            return("Error: Numbers cannot be more than four digits.")
        #check that we are only supplying addition or subtraction
        elif newlist[1] == "+" or newlist[1] == "-":
            #get answers
            if newlist[1] == "+":
                answer = str((int(newlist[0]) + int(newlist[2])))
            elif newlist[1] == "-":
                answer = str((int(newlist[0]) - int(newlist[2])))
        else:
            return("Error: Operator must be '+' or '-'.")

        
        #find distance of the operator + max number; +2 for operator and space
        distance = max(len(newlist[0]), len(newlist[2])) + 2
        top = top + newlist[0].rjust(distance) + "    "
        bottom = bottom + newlist[1] + newlist[2].rjust(distance - 1) + "    "
        dash = dash + len(newlist[1] + newlist[2].rjust(distance - 1)) * "-" + "    "
        totals = totals + answer.rjust(distance) + "    "
        
    print(top)
    print(bottom)
    print(dash)
    if values == True:
        print(totals)

#format printing

#sanity check
#print("Left Number: {}\nOperator: {}\nRight Number: {}\nAnswers: {}".format(left, operator, right, answer))

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2"])   #>>> "Error: Too many problems."
arithmetic_arranger(["32 + 698", "38016 - 2", "45 + 43", "123 + 49"])           #>>> "Error: Numbers cannot be more than four digits."
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 * 49"])            #>>> "Error: Operator must be '+' or '-'."
# Run unit tests automatically
#main(['-vv'])


'''
Left: ['32', '3801', '45', '123']
Operator: ['+', '-', '+', '+']
Right: ['698', '2', '43', '49']
Answers: [730, 3799, 88, 172] *optional

   32      3801      45      123              Left
+ 698    -    2    + 43    +  49    Operator Right
-----    ------    ----    -----    Line------Line (4 spaces)  
'''
