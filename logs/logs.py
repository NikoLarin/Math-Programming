import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

import math

x = sp.symbols('x') # tells sympy to use x as a math symbol (ALGEBRA in python)

def single_log(base,exponent,expression):

    # we need to turn this into exponential form
    equation = sp.Eq(expression, base**exponent) #sp eqation to create (ex = ex) this makes expression = base**

    print(f'The problem is: Log{base}({expression}) = {exponent}')
    print(f'The formula is A = BASE^Exponent')
    print(f'The exponential equation is: {base**exponent} = {expression}')

    solved = sp.solve(equation, x)
    return(print(f'The answer is {solved}'))

def double_log(expression1, expression2, sign,base, exponent):
    
    if sign == '+':
        print(f'Original log: log_{base}({expression1}) + log_{base}({expression2}) = {exponent}')
        condense = sp.expand((expression1) * (expression2)) # distributes the arguements
        print(f'Condensed: Log_2({condense}) = {exponent}')
        
    elif sign == '-':
        print(f'Original log: log_{base}({expression1}) - log_{base}({expression2}) = {exponent}')
        print(f'log {expression1} / {expression2} = {exponent}')
        condense = expression1 / expression2

    else:
        sign = input("Enter a correct sign (+/-): ")

    return single_log(base, exponent, condense)

def exponential_equation(base1, base2, expression1, expression2):
    if base1 == base2:
        print(f'Bases are the same, make the expressions equal: {expression1} = {expression2}')
        solve = sp.solve(sp.Eq(expression1, expression2),x)
        
        print(f'X = {solve}')

    else:
        #Log(base1)/#log(base2)(expression1) = expression2
        quotient = sp.log(base1).evalf() / sp.log(base2).evalf()
        print(f'Change of base: Log{base1}/Log{base2}')
        
        distribute = sp.expand(quotient * expression1)
        print(f"distribute the quotient to {expression1} | {quotient}({expression1}) = {distribute}" )
        
        equation = sp.Eq(distribute, expression2)
        print(f"Solve the equation {equation}")

        solve = sp.solve(equation,x)
        print(f'x = {solve}')

def natural_log_equation(e_exponent, exponent):
    equation = (sp.Eq(sp.ln(sp.E**(e_exponent)),sp.ln(exponent).evalf()))
    return print(sp.solve(equation,x))

exponential_equation(6,4,3*x+1,5*x+2)


