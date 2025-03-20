1. Boundry vaule tesing is where errors at the end of the input range are tested. For example, if a program accepts numbers between 1 and 100, boundary value testing would check inputs like 1, 100, 0 , 101. Compartively path coverage testing checks all of the possible paths in the software, ensuring all are used at least once. This allows you to cxonifrm that the less commonly used paths are still propely functional. For example consider a program that checks someones age, this type of testing would check every path to confirm their functionality. Lastly Faulty and Abnormal data which is used to see how a program handles invalid inputs, this testing makes sure that typos or unexpected inputs font cause the sofware to crash. For example, consider a caculator by testing the input with letters and symbols we can adapt the program to respond to invalid results to users in a clearer way. 

2. 
``` python
def is_safe_temperature(temp):
    return 0 <= temp <= 100
print(is_safe_temperature(0))
print(is_safe_temperature(100))
print(is_safe_temperature(101))
print(is_safe_temperature(-1))
```
3. 
``` python
def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "$5"
    elif 18 <= age <= 64:
        return "$10"
    else:
        return "Senior Discount - $7"
print(ticket_price(4))
print(ticket_price(13))
print(ticket_price(18))
print(ticket_price(65))
```
4. 
```python
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
```

Testing Debugging 
1. Compare unit testing, integration testing and system testing.
Unit testing,intergration testinf and system testing differ and test diffent parts of the program making all of them important in the debugging stage. Unit testing is where each unit is individually tested. Intergration testing involves combing some units together to test the program. System testing tests the entire system as a whole, ensuring everything works together as expected. The fact that each of the types test a diffrent part of the software leads to a more through testing and debugging process.


Reconginising errors
1. Syntax Error and Logical Error: The correct notation for multiplication is * instead of the x they used. It also is wrong becuase the correct maths equation is A = π r². Squared in python is simply **.
``` python
def calculate_area(radius):
    area = 3.14 x radius x 2
    return area

print(calculate_area(5))
print(calculate_area(3))
```
2. Logical Error: The correct equation for finding error of a rectangle/square is length*width not length+width
``` python
def calculate_area(length, width):
    return length + width

area = calculate_area(5, 3)
print(f"Area: {area}")
```

3. Runtime error: Cannot divde by zero as it causes program to crash.
```python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```
4. Syntax Error: The for loop is missing a colon.
```python
for i in range(5)
    print(i)
```
5. Logical Error: The average is found by dividing by the length of numbers not minus.
```python
def calculate_average(numbers):
    total = sum(numbers)
    return total - len(numbers)

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"Average: {average}")
```
6. Syntax Error: Forgot to import the maths module containg the Pi function.
```python
def calculate_area(diameter):
    return math.pi * diameter ** 2

print(calculate_area(5))
```