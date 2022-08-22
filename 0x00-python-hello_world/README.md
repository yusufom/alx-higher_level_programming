# 0. Run Python file
Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable $PYFILE.
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```

# 1. Run inline
Write a Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```

# 2. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

# 3. Print integer
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

* You can find the source code here
* The output of the script should be:
	* the number, followed by Battery street,
	* followed by a new line
* You are not allowed to cast the variable number into a string
* Your code must be 3 lines long
* You have to use f-strings
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```
