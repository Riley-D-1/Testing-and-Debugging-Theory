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


Compare unit testing, integration testing and system testing.

Compare
Show how things are similar or different.