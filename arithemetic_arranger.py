import re
def arithmetic_arranger(input):
    firstNumber = []
    operator = []
    secondNumber = []
    result = []
    if len(input)>5:
        return "Error: Too many problems"
    for arithmProblem in input:
        if "*" and "/" in arithmProblem:
            return "Error: Operator must be '+' or '-'"
        else:
            findFirstNumber = re.search(r'[0-9]+.*\+|[0-9]+.\-', arithmProblem).group()
            firstNumber.append(findFirstNumber[:-1])
            operator.append(findFirstNumber[-1])
            secondNumber.append(arithmProblem[len(findFirstNumber):])


    # print("first number, ",firstNumber)
    # print("operator ", operator)
    # print("second number, ", secondNumber)
    for numbers in firstNumber:
        print("    ", end="")
        for i in range(4):
            if 4-i > len(numbers):
                print(" ", end= "")
            else:
                print(numbers[-(4-i)], end="")
    print("") 
    count = 0
    for number in secondNumber:
        print("   ", end="")
        for i in range(5):
            if i == 0:
                print(operator[count], end="")
                count = count +1
            elif 5-i > len(number):
                print(" ", end= "")
            else:
                print(number[-(5-i)], end="")  
    print("" ,end="\n")
    for i in range(len(input)):
        print("   "+"_"*5, end="")
        if operator[i]=='+':
            result.append(int(firstNumber[i])+int(secondNumber[i]))
        else:
            result.append(int(firstNumber[i])-int(secondNumber[i]))
    print("")
    for i in range(len(input)):
        print("     "+ str(result[i]), end="")
    return 1

arithmetic_arranger(["32+698", "3801-2", "45+43", "123+49"])