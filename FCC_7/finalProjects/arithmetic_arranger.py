#from multiprocessing import Pool

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
number1 = []
operator = []
number2 = []
answer = []
#count how many errors fed to the function. Should return error at 5.
errors = 0

#get items in their own lists
for line in list:
    newlist = line.split()

    #get answers
    if newlist[1] == "+":
        answer.append(int(newlist[0]) + int(newlist[2]))
    elif newlist[1] == "-":
        answer.append(int(newlist[0]) - int(newlist[2]))
    else:
        #error message to user showing it cannot solve * or /
        print("Error: Operator must be '+' or '-'.")
        errors += 1
        if errors == 5:
            print("Error: Too many problems.")
            break


    number1.append(newlist[0])
    operator.append(newlist[1])
    number2.append(newlist[2])




print(number1, operator, number2, answer)


'''
        if i == "+":
            answer.append(int(i[0]) + int(i[2]))
        elif i == "-":
            answer.append(int(i[0]) - int(i[2]))
        else:
            print("I cannot solve this operator.")

'''