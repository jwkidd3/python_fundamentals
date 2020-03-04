def calculate(operand1, operand2, operator, **kwargs):
    if kwargs.get('float') == True:
        operand1 = float(operand1)
        operand2 = float(operand2)
    else:
        operand1 = int(operand1)
        operand2 = int(operand2)

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if type(operand1) == float:
             return operand1 / operand2
        else:
            return operand1 // operand2

import sys

if len(sys.argv) >= 4:  
    if len(sys.argv) == 5:
        print(calculate(sys.argv[1], sys.argv[2], 
				sys.argv[3], float=True))
    else:
        print(calculate(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
    print("usage:", sys.argv[0], "operand operand operator")
