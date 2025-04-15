# PythonForDevOps
This repo is for My python practice in DevOps Journey

## Compiler Vs Interpreter
### Compiler
- one time Translation     
- preparation after translation 
- Independent Preparation/ Execution 
- if Errors, No Translation   

### Interpreter
- 'N' time Translation
- preparation while translation 
- preparation with Help/ Execute in runtime Environment
- Partial Preparation till Error

## Python is Hybrid
         
files.py  ---Compiler--->  python-byteCode  (files.pyc) ---Intermediate lang ---> PVM python virtual machine

## Python is platform Independent
Python is a platform-independent programming language. This means you can write Python code on one operating system (like Windows) and run it on another (like macOS or Linux) without any modifications to the code itself. This is because Python uses a Python Virtual Machine (PVM) to interpret and execute the code, which handles platform-specific details. 

## Programming paradigms 
- Procedural Programming 
- Object oriented Programming
- Functional Programming
- Modular Programming

# Declaration and initialisation of multiple variables:
- In python multiple variables can be declared and initialised in a
single statement.
- Example: 
a,b,c = 5,10,15
- Here:
 a=5,b=10,c=15 , values will be stored in the respective 	 	 	
 variables in the order they are declared.
name, price,weight=‘soap’,10,15
- Here:
name=‘soap’, price=10, weight=15

- Example : Assigning same value to multiple variables:
		
- Both are same x, y, z=1,1,1 or	 	 x=y=z=1 

## Python- Dynamically Typed Language

- When a variable is declared , it must be initialise as well
- Variables do not have a specific data type , it’s type depends on the value assigned to
it.

Ex :
- integer type X = 25
- float type X = 13.75
- string type X = ‘A'

- For the above example we can say that, Python is a dynamically typed language
meaning while defining a variable we don’t have to give its data type explicitly like in any
other languages such as c++ , Java

- To know what type of data is provided to the variable we use function type(x)
Ex :
- The above result is <class ‘int ’> meaning the given data type belongs to a class of
integer
- As we know every thing in python is an object and every object will have its own class
- The class is decided on the type of value assigned to the variable.

