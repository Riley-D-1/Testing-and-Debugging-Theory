def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input, numbers required"

print(divide_numbers(12, 2)) 
print(divide_numbers(6, 0))   
print(divide_numbers("10", 5)) 