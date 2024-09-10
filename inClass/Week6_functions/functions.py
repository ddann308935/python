# Two types of functions: one that returns a value and one that doesn't

# Function Signature: function_name(parameters)

# Function Declaration
# class function_name(parameter: type_hints):
#     function_body

# Function Declaration
def greetings(n: str):
    print("Hi: " + n)

# Function call
name = "Bob"
greetings(name)
# Alternatively
greetings("Bob")

# Function Declaration with a return value and type hinting
def average(a: int, b: int) -> float:
    c = 0.0
    c =(a + b) / 2.0
    return c

# Function call
x, y = 3, 8
z = 0.0
z = average(x, y)

# Passing arguments by position
z = average(3, 8)
# Passing arguments by keywords
z = average(b=8, a=3)

# Scope

def add_numbers(x, y):
    total = x + y
    return total
print(total) 
# variable is out of scope

def multiply_numbers(x, y):
    total = x + y
    return total 
# Different function, so variable name can be used again

# Global statement

total = 0
def add_numbers(x, y):
    # Use the global variable 'total' within this function
    global total
    total = x + y

add_numbers(4, 2)

print(total)
# Prints the value 6

