## PRIMM Activity
### Python If Statements

Take a minute or two to examine the Python code below.

```python
price = 59.99
if price >= 49.99:
  print('You can buy that tool for less at Home Depot!')
```

### Questions
Answer these questions about the code.  Be specific in your answers!

1. Using the code snippet shown above, what would the output be?

The output would be "You can buy that tool for less at Home Depot!"

2. Change the item price to 39.50.  Now what would the output or look like?

The output would be nothing

3. What do you notice about the code that immediately follows an if statement?  How is that code formatted or arranged?
The code after an if statement is indented, showing that it is code executed if the if statement comes out true.

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
```

4. What does the `%` operator do in the conditional test shown above?

The % operator checks if the remainder after dividing the number by 2 is either a 1 or 0.

5. How does the code determine if a number is even or odd?

The code determines if a numer is even or odd by checking the remainder after dividing by 2. 
If the remainder is 1, the number is odd. If the remainder is 0, the number is even.