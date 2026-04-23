"""
Mathematical Functions Module
Complete set of mathematical operations and utilities
"""

# Define what gets exported with "from maths import *"
__all__ = [
    'addition', 'subtraction', 'multiplication', 'division', 'modulo', 'power',
    'square_root', 'factorial', 'is_prime', 'is_even', 'is_odd',
    'gcd', 'lcm', 'average', 'find_max', 'find_min', 'sum_list',
    'percentage', 'celsius_to_fahrenheit', 'fahrenheit_to_celsius',
    'circle_area', 'circle_circumference', 'triangle_area', 'rectangle_area'
]

# ==================== BASIC ARITHMETIC ====================
def addition(a, b):
    """Add two numbers"""
    return a + b

def subtraction(a, b):
    """Subtract two numbers"""
    return a - b

def multiplication(a, b):
    """Multiply two numbers"""
    return a * b

def division(a, b):
    """Divide two numbers (with zero-check)"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def modulo(a, b):
    """Get remainder after division"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b

def power(base, exponent):
    """Calculate base to the power of exponent"""
    return base ** exponent

def square_root(n):
    """Calculate square root of a number"""
    if n < 0:
        return "Error: Cannot calculate square root of negative number!"
    return n ** 0.5

# ==================== NUMBER PROPERTIES ====================
def is_even(n):
    """Check if a number is even"""
    return n % 2 == 0

def is_odd(n):
    """Check if a number is odd"""
    return n % 2 != 0

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Error: Cannot calculate factorial of negative number!"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# ==================== ADVANCED MATH ====================
def gcd(a, b):
    """Calculate Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Calculate Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

# ==================== LIST/STATISTICS ====================
def sum_list(numbers):
    """Calculate sum of a list of numbers"""
    return sum(numbers)

def average(numbers):
    """Calculate average of a list of numbers"""
    if not numbers:
        return "Error: Empty list!"
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """Find maximum number in a list"""
    if not numbers:
        return "Error: Empty list!"
    return max(numbers)

def find_min(numbers):
    """Find minimum number in a list"""
    if not numbers:
        return "Error: Empty list!"
    return min(numbers)

# ==================== UTILITY FUNCTIONS ====================
def percentage(part, whole):
    """Calculate percentage"""
    if whole == 0:
        return "Error: Whole cannot be zero!"
    return (part / whole) * 100

# ==================== TEMPERATURE CONVERSIONS ====================
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# ==================== GEOMETRY ====================
def circle_area(radius):
    """Calculate area of a circle"""
    if radius < 0:
        return "Error: Radius cannot be negative!"
    pi = 3.14159265359
    return pi * radius * radius

def circle_circumference(radius):
    """Calculate circumference of a circle"""
    if radius < 0:
        return "Error: Radius cannot be negative!"
    pi = 3.14159265359
    return 2 * pi * radius

def triangle_area(base, height):
    """Calculate area of a triangle"""
    if base < 0 or height < 0:
        return "Error: Base and height must be positive!"
    return (base * height) / 2

def rectangle_area(length, width):
    """Calculate area of a rectangle"""
    if length < 0 or width < 0:
        return "Error: Length and width must be positive!"
    return length * width