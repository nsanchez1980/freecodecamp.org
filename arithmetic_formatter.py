def arithmetic_arranger(problems, display_solutions = ""):

    import re
    operands = []
    operators = []
    solutions = []
    whichisbigger = []
    sumaoresta = []
    check = []
    index = 0
    arranged_problems = ""
    primera_linea = ""
    segunda_linea = ""
    tercera_linea = ""
    cuarta_linea = ""

    #check for # of problems
    if len(problems)>5:
        return("Error: Too many problems.")

    #extract data and perfom calculations
    while index < len(problems):
        operands.append(re.findall("[0-9]+", problems[index]))
        operators.append(re.findall("[+-]", problems[index]))
        if int(operands[index][0])>int(operands[index][1]):
            whichisbigger.append(True)
        else:
            whichisbigger.append(False)
        if str(operators[index]).find('+') == 2:
            sumaoresta.append(True)
            solutions.append(int(operands[index][0])+int(operands[index][1]))
            check.append(problems[index].split("+"))
            try:
                a = int(check[index][0])
                b = int(check[index][1])
            except:
                return ("Error: Numbers must only contain digits.")
        elif str(operators[index]).find('-') == 2:
            sumaoresta.append(False)
            solutions.append(int(operands[index][0])-int(operands[index][1]))
            check.append(problems[index].split("-"))
            try:
                a = int(check[index][0])
                b = int(check[index][1])
            except:
                return ("Error. Numbers must only contain digits.")            
        else:
            return("Error: Operator must be '+' or '-'.")
        if int(operands[index][0])>9999 or int(operands[index][1])>9999:
            return("Error: Numbers cannot be more than four digits.")
        index = index + 1

    index = 0
    while index < len(problems):
        if whichisbigger[index]:
            #el de arriba es más grande
            if index==0:
                primera_linea = str(operands[index][0]).rjust(len(str(operands[index][0]))+2, " ")
                if sumaoresta[index]:
                    segunda_linea = "+ " + str(operands[index][1]).rjust(len(str(operands[index][0])), " ")
                else:
                    segunda_linea = "- " + str(operands[index][1]).rjust(len(str(operands[index][0])), " ")
                tercera_linea = "".rjust(len(str(operands[index][0]))+2, "-")
                if display_solutions:
                    cuarta_linea = str(solutions[index]).rjust(len(str(operands[index][0]))+2, " ")             
            else:
                primera_linea = primera_linea + str(operands[index][0]).rjust(len(str(operands[index][0]))+6, " ")
                if sumaoresta[index]:
                    segunda_linea = segunda_linea + "    +"+ str(operands[index][1]).rjust(len(str(operands[index][0])) + 1, " ")
                else:
                    segunda_linea = segunda_linea + "    -"+ str(operands[index][1]).rjust(len(str(operands[index][0])) + 1, " ")
                tercera_linea = tercera_linea + "    " + "".rjust(len(str(operands[index][0]))+2, "-")  
                if display_solutions:
                    cuarta_linea = cuarta_linea + "    " + str(solutions[index]).rjust(len(str(operands[index][0]))+2, " ")             
        else:
            #el de abajo es más grande o son los dos iguales, segual
            if index==0:
                primera_linea = str(operands[index][0]).rjust(len(str(operands[index][1]))+2, " ")
                if sumaoresta[index]:
                    segunda_linea = "+ " + str(operands[index][1]).rjust(len(str(operands[index][1])), " ")
                else:
                    segunda_linea = "- " + str(operands[index][1]).rjust(len(str(operands[index][1])), " ")  
                tercera_linea = "".rjust(len(str(operands[index][1]))+2, "-")              
                if display_solutions:
                    cuarta_linea = str(solutions[index]).rjust(len(str(operands[index][1]))+2, " ")             
            else:
                primera_linea = primera_linea + str(operands[index][0]).rjust(len(str(operands[index][1]))+6, " ")
                if sumaoresta[index]:
                    segunda_linea = segunda_linea + "    + " + operands[index][1]
                else:
                    segunda_linea = segunda_linea + "    - " + operands[index][1]
                tercera_linea = tercera_linea + "    " + "".rjust(len(str(operands[index][1]))+2, "-")
                if display_solutions:
                    cuarta_linea = cuarta_linea + "    " + str(solutions[index]).rjust(len(str(operands[index][1]))+2, " ")             
        index = index + 1

    #format the string to match the required solution
    

    arranged_problems = primera_linea + "\n" + segunda_linea + "\n" + tercera_linea
    if display_solutions == True:
        arranged_problems = arranged_problems + "\n" + cuarta_linea
    


    return arranged_problems


print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))

