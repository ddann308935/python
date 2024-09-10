def average(x: float, y: float, z: float) -> float:
    # Remove when you attempt your answer! It's here purely so the code compiles.
    n = 0.0
    n = (x + y + z)/3.0
    return n
    
def test_average():
    s = "The average of"
    a = average(3, 11, 8)
    print(s, "3, 11 and 8 is", a)
    a = average(7, 21, 17)
    print(s, "7, 21 and 17 is", a)


def high(a: int, b: int) -> int:
    # Remove when you attempt your answer! It's here purely so the code compiles.
    if a > b:
        return a
    else:
        return b

def test_high():
    x, y = 3, 7
    print("The higher of", x, "and", y, "is", high(x, y))
    x, y = 13, 7
    print("The higher of", x, "and", y, "is", high(x, y))


def power(value1: int, value2: int) -> int:
    # Remove when you attempt your answer! It's here purely so the code compiles.
    i = 0
    n = 0
    if i < 1:
        n = value1 * value1 # power of 2
        i += 1
    while i < value2 - 1:
        n = n * value1      # power of 3
        i += 1
    return n


def test_power():
    a, b = 2, 3
    print(a, "to the power of", b, "is", power(a, b))
    a, b = 2, 8
    print(a, "to the power of", b, "is", power(a, b))
    a, b = 5, 3
    print(a, "to the power of", b, "is", power(a, b))
    a, b = 20, 6
    print(a, "to the power of", b, "is", power(a, b))


# Define a function to find the square root of a number
def square_root(val1: int) -> float:
    import math
    val1 = math.sqrt(val1)
    return val1

# Uncomment the following test function, to ensure your square root function is working correctly
def test_square_root():
    val1 = 25.0
    val2 = 9.0
    val3 = 12.0
    print("The square root of", val1, "is:", square_root(val1))		
    print("The square root of", val2, "is:", square_root(val2))
    print("The square root of", val3, "is:", square_root(val3))

# Define your functions for tasks 5 and 6 below
def print_car_sales(a: int):
    i = 0
    while i < a:
        print("X", end="")
        i += 1
    print()
    
def test_print_car_sales():
    names = ["Pam", "Leo", "Kim", "Bob"]
    num_sold = []
    i = 0
    while i < 4:
        num_sold.append(int(input("Enter cars sold by " + names[i] + ": ")))
        i += 1
    
    print()
    print("Car sales for month:")
    print()

    n = 0
    while n < 4:
        print(f"{names[n]}: ", end="")
        print_car_sales(num_sold[n])
        n += 1

def print_number_of_eggs(a: int):
    dozens = int(a / 12) 
    remaining = a % 12
    print(f"{a} eggs is {dozens} full dozen with {remaining} eggs remaining.")

def test_print_number_of_eggs():
    number_of_eggs = int(input("Please enter the number of eggs: "))
    print()
    print_number_of_eggs(number_of_eggs)


# Run all of your test functions from the following 'if' statement
if __name__ == '__main__':
    test_average()
    test_high()
    test_power()
    test_square_root()
    test_print_car_sales()
    test_print_number_of_eggs()
