#!/bin/env python3
import argparse, termcolor
from glob import escape

parser = argparse.ArgumentParser(description="""
█▀ ▄▄ █▀▀ ▄▀█ █░░
▄█ ░░ █▄▄ █▀█ █▄▄

[code]Box - Andrei A. Abd 2022

[*] Introduction:
    simple calculator built in python,it can do 7 difference arithmetic operators with two numbers.

[*] Source: https://github.com/codeBOX-projects

[*] Usage Examples: [First Number] [Arthimetic Operator] [Secon Number]

    > Addition       : 100  "+"  50
    > Subtraction    : 100  "-"  50
    > Multiplication : 100  "*"  50
    > Division       : 100  "/"  50
    > Modulus        : 100  "%"  50
    > Exponentiation : 100  "**" 50
    > Floor division : 100  "//" 50
                                 """,
                                 usage=termcolor.colored("python3 [first number] [arthmetic operator] [second number]",'red'),
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('num1', type=int, help="First Number.")
parser.add_argument('math_value', type=str, help="Arithmetic Operators.")
parser.add_argument('num2', type=int, help="Second Number.")
args = parser.parse_args()

def math_resulte(num1, math_value, num2):
    if math_value == "+":
        math_value = num1 + num2
        print("[+] Resulte: " + termcolor.colored(math_value, 'green'))
    elif math_value == "-":
        math_value = num1 - num2
        print("[-] Resulte: " + termcolor.colored(math_value, 'green'))
    elif math_value == "*":
        math_value = num1 * num2
        print("[*] Resulte: " + termcolor.colored(math_value, 'green'))
    elif math_value == "/":
        math_value = num1 / num2
        print("[/] Resulte: " + termcolor.colored(math_value, 'green'))
    elif math_value == "%":
        math_value = num1 % num2
        print("[%] Resulte: " + termcolor.colored(math_value, 'green'))
    elif math_value == "**":
        math_value = num1 ** num2
        print("[**] Resulte: " + termcolor.colored(math_value, 'green'))
    elif math_value == "//":
        math_value = num1 // num2
        print("[//] Resulte: " + termcolor.colored(math_value, 'green'))
    else:
        print(termcolor.colored("[!] Error: This mathematical operation is not available",'red'))
    

if __name__ == "__main__":
    try:
        math_resulte(args.num1, args.math_value, args.num2)
    except:
        pass