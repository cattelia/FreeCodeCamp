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

    #check to make sure there are <= 5 entered problems
    if len(problems) > 5:
        return ("Error: Too many problems.")

    #get items in their own lists
    for line in problems:

        newlist = line.split()  #>>> ["32", "+", "698"]

        #check is both left and right operand are only numbers
        if newlist[0].isnumeric() == False or newlist[2].isnumeric() == False:
            return ("Error: Numbers must only contain digits.")
        #check to make sure no number is greater than 4 digits
        elif len(newlist[0]) > 4 or len(newlist[2]) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        #check that we are only supplying addition or subtraction
        elif newlist[1] == "+" or newlist[1] == "-":
            #get answers
            if newlist[1] == "+":
                answer = str((int(newlist[0]) + int(newlist[2])))
            elif newlist[1] == "-":
                answer = str((int(newlist[0]) - int(newlist[2])))
        else:
            return ("Error: Operator must be '+' or '-'.")
        #find distance of the operator + max number; +2 for operator and space

        distance = max(len(newlist[0]), len(newlist[2])) + 2
        top = top + newlist[0].rjust(distance) + "    "
        bottom = bottom + newlist[1] + newlist[2].rjust(distance - 1) + "    "
        dash = dash + len(newlist[1] + newlist[2].rjust(distance - 1)) * "-" + "    "
        totals = totals + answer.rjust(distance) + "    "

    if values == False:
        arranged_problems = top + "\n" + bottom + "\n" + dash + "\n" 
    else:
        arranged_problems = top + "\n" + bottom + "\n" + dash + "\n" + totals

    return arranged_problems