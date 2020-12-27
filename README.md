# High Precision Calculation
Python implemented high precision calculation
*without using any library*.

### Arithmetic Support
- Basic (Finite many bits)
    * Addition
    * Subtraction
    * Multiplication
    * Division
        * Finite many precision

### Demo

Simply run `python main.py` in the root directory of the project.

Here is a demo, and you can reproduce the same results.

```
Please select calculation type
Type 1 for addition, 2 for subtraction,
3 for multiplication, 4 for division
To exit the program, just type `exit` or `quit`
Your choice: 1
--------------------
Addition: a + b
a = -283.000000000000000123
b = 111111119999999999.98
----------Result----------
a + b = -283.000000000000000123 + 111111119999999999.98
      = 111111119999999716.979999999999999877
--------------------------
Do you want to try again? [Y/n]:
Please select calculation type
Type 1 for addition, 2 for subtraction,
3 for multiplication, 4 for division
To exit the program, just type `exit` or `quit`
Your choice: 4
--------------------
Division: a / b
a = 3.1415926
b = 11.89999991212222201
precision [default 10] = 20
----------Result----------
a / b = 3.1415926 / 11.89999991212222201
      = 0.26399938010081335411
--------------------------
Do you want to try again? [Y/n]: n
Exit the program
```

### User Friendly Design
- Command line interface
    - Clear and detailed prompt
    - Serious input validation
    - General exception handler
- Human readable result
    - Remove redundant prefix and suffix zero

### Programmer Friendly Code
- Modular design
    - High reuse
- Meaningful function and variable names
