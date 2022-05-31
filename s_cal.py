#!/bin/env python3
import argparse, termcolor
from glob import escape

parser = argparse.ArgumentParser(description="Example: [first number] [arithmetic operators] [second number] ")
parser.add_argument('num1', type=int, help="First Number.")
parser.add_argument('math_value', type=str, help="Arithmetic Operators.")
parser.add_argument('num2', type=int, help="Second Number.")
args = parser.parse_args()

def math_resulte(num1, math_value, num2):
    if math_value == "+":
        math_value = num1 + num2
        print(termcolor.colored(math_value, 'green'))
    elif math_value == "-":
        math_value = num1 - num2
        print(termcolor.colored(math_value, 'green'))
    elif math_value == "*":
        math_value = num1 * num2
        print(termcolor.colored(math_value, 'green'))
    elif math_value == "/":
        math_value = num1 / num2
        print(termcolor.colored(math_value, 'green'))
    elif math_value == "%":
        math_value = num1 % num2
        print(termcolor.colored(math_value, 'green'))
    elif math_value == "**":
        math_value = num1 ** num2
        print(termcolor.colored(math_value, 'green'))
    elif math_value == "//":
        math_value = num1 // num2
        print(termcolor.colored(math_value, 'green'))
    else:
        print(termcolor.colored("[!] Error: This mathematical operation is not available",'red'))
    

if __name__ == "__main__":
    try:
        math_resulte(args.num1, args.math_value, args.num2)
    except:
        pass