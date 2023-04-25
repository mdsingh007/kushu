from posixpath import split


def arithmetic_operation(problem):
    operand1, operator, operand2 = problem.split()
    
    if operator == "//":
        return int(operand1) / int(operand2)

    if operator == "*":
        return int(operand1) * int(operand2)

    if operator == "+":
        return int(operand1) + int(operand2)

    if operator == "-":
        return int(operand1) - int(operand2)

print(arithmetic_operation("12 - 12"))