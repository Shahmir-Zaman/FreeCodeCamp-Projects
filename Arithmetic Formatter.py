def arithmetic_arranger(problems, show_answers=False):
    secondRow=""
    firstRow=""
    dashes=""
    dashesTemp=""
    resultsTemp=""
    results=""
    firstRowTemp=""
    secondRowTemp=""
    #Situations that will return an error:
    if len(problems)>5:
        return'Error: Too many problems.'
    for problem in problems:
        for char in problem:
            if char == "*" or char =="/":
                return "Error: Operator must be '+' or '-'."
        
        #Checking to find out if the problem only contains digits
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
        
        #Extracting Operends and operator
        operend1=problem.split(" ")[0]
        operend2=problem.split(" ")[2]
        operator=problem.split(" ")[1]

        #Making the problem right aligned and equally spaced
        maxLength=max(len(operend1),len(operend2))
        firstRowTemp=operend1.rjust(maxLength+2)+"    "
        secondRowTemp=operator+operend2.rjust(maxLength+1)+"    "
        dashesTemp="-"*(len(secondRowTemp)-4)+"    "
        #Getting the results
        if operator == "+":
            resultsTemp=str(int(operend1)+int(operend2)).rjust(maxLength+2)+"    "
        else:
            resultsTemp=str(int(operend1)-int(operend2)).rjust(maxLength+2)+"    "

        #Compiling all the lines:
        firstRow+=firstRowTemp
        secondRow+=secondRowTemp
        dashes+=dashesTemp
        results+=resultsTemp
        
    # Remove extra spaces at the end
    firstRow = firstRow.rstrip()
    secondRow = secondRow.rstrip()
    dashes = dashes.rstrip()
    results = results.rstrip()

    # Return the arranged strings
    if show_answers:
        return f"{firstRow}\n{secondRow}\n{dashes}\n{results}"
    else:
        return f"{firstRow}\n{secondRow}\n{dashes}"


print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))


