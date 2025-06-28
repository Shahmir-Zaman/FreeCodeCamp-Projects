def arithmetic_arranger(problems, show_answers=False):
    secondRowFinal=""
    firstRowFinal=""
    dashes=""
    resultsTemp=""
    results=""
    #Situations that will return an error:
    if len(problems)>5:
        return'Error: Too many problems.'
    for problem in problems:
        for char in problem:
            if char == "*" or char =="/":
                return "Error: Operator must be '+' or '-'."
            
        problemWtihoutOperator=problem.replace("+","").replace("-","").replace(" ","")
        try:
            problemWtihoutOperator=int(problemWtihoutOperator)
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        if "+" in problem:# Checking if length of number is less then 4 by spliting the string from the Operator and then removing the space
            if len(problem.split("+")[0].strip())>4 or len(problem.split("+")[1].strip()) >4:
                return('Error: Numbers cannot be more than four digits.')
        else:
            if len(problem.split("-")[0].strip())>4 or len(problem.split("-")[1].strip()) >4:
                return('Error: Numbers cannot be more than four digits.')
    #Interface Coding
        firstRow=problem.split(" ")[0]
        secondRow=problem.split(" ")[2]
        operator=problem.split(" ")[1]
        if problem.split(" ")[1] == "-":
            if problem.split(" ")[0]<problem.split(" ")[2]:
                resultsTemp=str(int(problem.split(" ")[0])-int(problem.split(" ")[2]))
            else:
                resultsTemp=str(int(problem.split(" ")[0])-int(problem.split(" ")[2]))
        else:
            resultsTemp=str(int(problem.split(" ")[0])+int(problem.split(" ")[2]))

        if problem != problems[-1]:# To check if the problem is not the last one in the list
            # Calculate width needed for this problem
            width = max(len(firstRow), len(operator + " " + secondRow), len(resultsTemp)) + 2
            
            # First row - right aligned
            spaces_first = width - len(firstRow)
            firstRowTemp = " " * spaces_first + firstRow + "    "
            
            # Second row - right aligned  
            operator_line = operator + " " + secondRow
            spaces_second = width - len(operator_line)
            secondRowTemp = " " * spaces_second + operator_line + "    "
            
            # Dashes row
            dashesTemp = "-" * width + "    "
            
            # Results row - right aligned
            spaces_results = width - len(resultsTemp)
            resultsRowTemp = " " * spaces_results + resultsTemp + "    "
            
            firstRowFinal += firstRowTemp
            secondRowFinal += secondRowTemp
            dashes += dashesTemp
            results += resultsRowTemp


        else:
            # Calculate width needed for this problem (last problem - no trailing spaces)
            width = max(len(firstRow), len(operator + " " + secondRow), len(resultsTemp)) + 2
            
            # First row - right aligned
            spaces_first = width - len(firstRow)
            firstRowTemp = " " * spaces_first + firstRow
            
            # Second row - right aligned  
            operator_line = operator + " " + secondRow
            spaces_second = width - len(operator_line)
            secondRowTemp = " " * spaces_second + operator_line
            
            # Dashes row
            dashesTemp = "-" * width
            
            # Results row - right aligned
            spaces_results = width - len(resultsTemp)
            resultsRowTemp = " " * spaces_results + resultsTemp
            
            firstRowFinal += firstRowTemp
            secondRowFinal += secondRowTemp
            dashes += dashesTemp
            results += resultsRowTemp
    
    if show_answers== True:
        return f'{firstRowFinal}\n{secondRowFinal}\n{dashes}\n{results}'
    else:
        return f'{firstRowFinal}\n{secondRowFinal}\n{dashes}'


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print("\n")
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print("\n")
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print("\n")
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print("\n")
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
