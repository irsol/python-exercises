## SCRIPTING

* Python Installation and Environment Setup
* Running and Editing Python Scripts
* Interacting with User Input
* Handling Exceptions
* Reading and Writing Files
* Importing Local, Standard, and Third-Party Modules
* Experimenting with an Interpreter


## Scripting With Raw Input
We can get raw input from the user with the built-in function input, which takes in an optional string argument that you can use to specify a message to show to the user when asking for input.

```
name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))
```

This prompts the user to enter a name and then uses the input in a greeting. The input function takes in whatever the user types and stores it as a string. If you want to interpret their input as something other than a string, like an integer, as in the example below, you need to wrap the result with the new type to convert it from a string.

```
num = int(input("Enter an integer"))
print("hello" * num)
```

We can also interpret user input as a Python expression using the built-in function eval. This function evaluates a string as a line of Python.

```
result = eval(input("Enter an expression: "))
print(result)
```

Float:

```
num = int(float(input("Enter an integer")))
print("hello" * num)
```


## Errors And Exceptions
Syntax errors occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

Exceptions occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.


## Try Statement
We can use try statements to handle exceptions. There are four clauses you can use (one more in addition to those shown in the video).

try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

#### Specifying Exceptions
We can actually specify which error we want to handle in an except block like this:
```
try:
    # some code
except ValueError:
    # some code
```
Now, it catches the ValueError exception, but not other exceptions. If we want this handler to address more than one type of exception, we can include a tuple after the except with the exceptions.

```
try:
    # some code
except ValueError, KeyboardInterrupt:
    # some code
```
Or, if we want to execute different blocks of code depending on the exception, you can have multiple except blocks.

```
try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
```