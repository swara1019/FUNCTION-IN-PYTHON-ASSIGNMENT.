#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1)Write a Python function to find the maximum of three numbers.
num1 = int(input("enter the first number="))
num2 = int(input("enter the second number="))
num3 = int(input("enter the third number="))
maximum_number = max(num1,num2,num3)
print("maximum number is =",maximum_number)


# In[2]:


#Q.2) Write a Python function to sum all the numbers in a list.
list1 = [34,67,89,23,65]
add_number = sum(list1)
print("sum of the numbers in list =",add_number)


# In[3]:


#Q.3) Write a Python function to multiply all the numbers in a list.
list2 = [1,2,5,6,9]
result = 1
for number in list2:
    result *= number
print("multiplication of all the number in list is =",result)


# In[4]:


#Q.4) Write a Python program to reverse a string. 
string = input("enter the string word which you want to reverse=")
reversed_string = string[::-1]
print(reversed_string)


# In[5]:


#Q.5) Write a Python function to calculate the factorial of a number (a non-negative
#integer). The function accepts the number as an argument.
def factorial(number):
    if number<0:
        print("factorial of negetive number is not defined")
    elif number==0 or number==1:
        print("factorial of entered number is = 1")
    else:
        final_factorial = 1
        for i in range(2,number + 1):
            final_factorial *= i
    print("factorial of entered number is =",final_factorial)
number = int(input("enter the number = "))
factorial(number)


# In[6]:


#Q.6) Write a Python function to check whether a number falls within a given range.
start_range = int(input("enter the start range = "))
end_range = int(input("enter the end range = "))
number_to_check = int(input("enter the number="))
if start_range<=number_to_check<=end_range:
    print("yes entered number is in specified range")
else:
    print("not in range")


# In[7]:


#Q.7) Write a Python function that accepts a string and counts the number of upper and lower case 
#letter.
def count_lower_upper(word):
    lower_count = 0
    upper_count = 0
    for char in word:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return lower_count, upper_count
input_word = input("Enter a word or sentence: ")
lower_count, upper_count = count_lower_upper(input_word)
print("Number of lowercase letters:", lower_count)
print("Number of uppercase letters:", upper_count)


# In[8]:


#Q.8) Write a Python function that takes a list and returns a new list with distinct elements
#from the first list.
def get_unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list
# Example usage:
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result = get_unique_elements(sample_list)
print("Sample List:", sample_list)
print("Unique List:", result)


# In[9]:


#Q.9) Write a Python function that takes a number as a parameter and checks whether the
#number is prime or not. 
def check_prime(number):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if (number % i) == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    else:
        print("Not prime")
number = int(input("Enter the number: "))
check_prime(number)


# In[10]:


#Q.10) Write a Python program to print the even numbers from a given list.
list5 = [23,53,67,24]
even_list =[]
for x in list5:
    if x%2==0:
        even_list.append(x)
        print("all the even number are in list = ",even_list)


# In[11]:


#Q.11) Write a Python function to check whether a number is "Perfect" or not.
def is_perfect_number(number):
    if number <= 0:
        return False    
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number
# Example usage:
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")


# In[12]:


#Q.12) Write a Python function that checks whether a passed string is a palindrome or not.
def is_palindrome(string):
    # Compare the original string with its reverse
    return string == string[::-1]
# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")


# 

# In[13]:


#


# In[14]:


#Q.13) Write a Python function that prints out the first n rows of Pascal's triangle. 
#Note:Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        triangle.append(row)
    return triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(len(triangle[-1]) * 2 - 1))
# Example usage:
n = int(input("Enter the number of rows for Pascal's triangle: "))
triangle = generate_pascals_triangle(n)
print_pascals_triangle(triangle)


# In[15]:


#Q.14)Write a Python function to check whether a string is a pangram or not.
#Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
def is_pangram(string):
    # Convert the string to lowercase
    string = string.lower()

    # Check if all the letters from 'a' to 'z' are present in the string
    return all(letter in string for letter in 'abcdefghijklmnopqrstuvwxyz')

# Example usage:
input_string = input("Enter a string: ")
if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")


# In[16]:


#Q.15) Accept hyphen-separated sequence of words as input and prints the words in a hyphen-separated 
#sequence after sorting them alphabetically
input_sequence = input("Enter a hyphen-separated sequence of words: ")
# Split the input sequence into a list of words
words = input_sequence.split('-')
# Sort the words alphabetically
sorted_words = sorted(words)
# Join the sorted words into a hyphen-separated sequence
result = '-'.join(sorted_words)
# Print the result
print("Expected Result:", result)


# In[17]:


#Q.16) Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30.
def create_squares_list():
    numbers = range(1, 31)
    squares = [x**2 for x in numbers]
    return squares
# Example usage:
squares_list = create_squares_list()
print("List of squares:", squares_list)


# In[1]:


#Q.17) Write a Python program to create a chain of function decorators (bold, italic,underline etc.)
def make_formatting_decorator(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

@make_formatting_decorator('b')
@make_formatting_decorator('i')
@make_formatting_decorator('u')
def greet(name):
    return f"Hello, {name}!"

# Example usage:
formatted_greeting = greet("John")
print("Formatted Greeting:", formatted_greeting)


# In[1]:


#Q.18) Write a Python program to execute a string containing Python code.
def execute_python_code(code_string):
    try:
        exec(code_string)
    except Exception as e:
        print(f"Error: {e}")
# Example usage:
python_code = """
print("Hello, World!")
for i in range(5):
    print(f"Value of i: {i}")
"""
execute_python_code(python_code)


# In[2]:


#Q.19) Write a Python program to access a function inside a function.
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    # Return the inner function
    return inner_function
# Call the outer function and get the inner function
inner_func = outer_function()
# Call the inner function outside the outer function
inner_func()


# In[3]:


#Q.20) Write a Python program to detect the number of local variables declared in a function.  Sample Output: 3
def sample_function(x, y, z):
    a = 10
    b = "Hello"
    c = [1, 2, 3]
    
    # Use locals() to get a dictionary of local variables
    local_variables = locals()
    
    # Subtract the number of parameters
    num_local_variables = len(local_variables) - 3
    
    return num_local_variables
# Call the function and print the result
result = sample_function(1, 2, 3)
print(f"Number of local variables: {result}")


# In[5]:


#Q.21) Write a Python program that invokes a function after a specified period of time.
import time
import math

def calculate_square_root(number):
    result = math.sqrt(number)
    print(result)

def invoke_function_after_delay(delay, number):
    print(f"Square root after {delay} milliseconds:")
    time.sleep(delay / 1000.0)  # Convert milliseconds to seconds
    calculate_square_root(number)

# Sample usage
invoke_function_after_delay(1000, 16)  # Delay of 1000 milliseconds (1 second)
invoke_function_after_delay(2000, 100)  # Delay of 2000 milliseconds (2 seconds)
invoke_function_after_delay(500, 25000)  # Delay of 500 milliseconds (0.5 seconds)


# In[ ]:




