#Solution 1
In computer software, a general-purpose programming language (GPL) is a programming language designed to be 
used for building software in a wide variety of application domains, across a multitude of hardware configurations 
and operating systems. Python was conceived as a language that emphasized code readability and extensibility.
The former allowed non-software engineers to easily learn and write computer programs, while the latter allowed domain specialists to 
easily create libraries suited to their own use cases. For these reasons, Python has been used across a wide range of domains and hence
act as a general purpose Programming Language.
When compiled, other languages turn into Assembly and run directly in the processor. Hence, being an interpreted language, 
which is not subject to the processor, makes Python a high-level programming language.Also, Python is a high-level programming 
language that is known for its ease of readability.

#Solution 2
Python is a dynamically typed language.It doesn’t know about the type of the variable until the code is 
run. So declaration is of no use. What it does is, It stores that value at some memory location and then 
binds that variable name to that memory container. And makes the contents of the container accessible 
through that variable name. So the data type does not matter. As it will get to know the type of the 
value at run-time.


#Solution 3
PRO'S:-
Python is easy to learn and Read,Python enhances productivity.It has a vast collection of libraries.
Also it is free, open-source, and has a vibrant community.

CON'S:-
Python has speed limitations.While your program runs in Python, it has to do more work in 
line-by-line execution, so the process will be slow.Python is not so strong with mobile computing.
It can have runtime errors and consumes a lot of memory space.

#Solution 4
Python can be used in various domains like artificial intelligence, machine learning,deep learning
Web development,Robotics,Scientiic Programming,Data analysis,Data Enginnering and Data Science.

# Solution 5
Variable is a name given to specific Memory Location.A variable 
declaration always contains two components: the type of the variable and its name.
Ex- int x

#Solution 6

We can take the Input using the input() function from the user.
Ex- x=input('Enter your Value :')

#Solution 7

The default data type is String.

# Solution 8

Type Casting is the method to convert the variable data type into a certain data type in order 
to do the operation required to be performed by users. 

#Solution 9

No, we cannot take multiple inputs from the user using single input() function as it only takes one argument.
We have to use multiple input statements.


#Solution 10

Keywords in Python are unique reserved words that cannot use a keyword as 
a variable, function, or other identifiers.The keywords are always available
you'll never have to import them into your code.

#Solution 11

We cannot use a keyword as a variable name, function name, or any other identifier. 
They are used to define the syntax and structure of the Python language.It's 
because keywords have predefined meanings.


#Solution 12

Indentation refers to the spaces at the beginning of a code line.Python uses indentation 
to indicate a block of code.In another words, all the statements with the same space to 
the right, belong to the same code.


#Solution 13

The basic way to do output is the print statement.
Ex- print('Hello World')

#Solution 14

In Python, operators are special symbols that designate that some sort of computation 
should be performed. The values that an operator acts on are called operands.

#Solution 15

/ operator is used for float division and // operator is used for integer division.

#Solution 16

print('iNeuron'*4)

# Solution 17

x=int(input('Enter Your Number: '))
if x%2==0:
    print('The Number is even')
else:
    print('The Number is odd')

# Solution 18

The logical operators and, or and not are also referred to as boolean operators. While and as well as or operator needs two 
operands, which may evaluate to true or false, not operator needs one operand evaluating to true or false.Boolean and 
operator returns true if both operands return true.Boolean or operator returns true if any one operand is true.
The not operator returns true if its operand is a false expression and returns false if it is true.

# Solution 19

1
0
False
1

#Solution 20

A conditional statement is used to handle conditions in your program.We have different types of conditional statements like 
if, if-else, elif, nested if, and nested if-else statements.

#Solution 21

The if/elif/else structure is a common way to control the flow of a program.
If the condition following the keyword if evaluates as true, the block of code will execute.
We can also add an else response that will execute if the condition is false.
Multiple conditions can be checked by including one or more elif checks after your initial if statement. Just keep in mind 
that only one condition will execute:

# Solution 22

age=int(input("Enter person's age: "))
if age>=18:
    print('I can Vote')
elif age<0:
    print('Invalid age')
else:
    print("I can't Vote")
    
# Solution 23

numbers = [12, 75, 150, 180, 145, 525, 50]
sum=0
for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        sum+=numbers[i]
print(sum)

#Solution 24

x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
z=int(input("Enter value of z: "))

if x>y and x>z:
    print('The greatest numer is x : ',x)
elif y>x and y>z:
    print('The greatest numer is y : ',y)
elif z>x and z>y:
    print('The greatest numer is z : ',z)

# Solution 25

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    
    if i>150:
        continue
    if i>500:
        break
    if i%5==0:
        print(i)
