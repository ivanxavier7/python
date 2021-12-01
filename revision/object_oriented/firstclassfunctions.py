def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):   # passamos função como argumento
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)
