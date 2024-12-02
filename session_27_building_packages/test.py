#!/usr/bin/python3

import sys

print('Number of arguments:', len(sys.argv))
print ('Argument List:', str(sys.argv))

variable = 20
another_variable = 55


print("This is a python script")
print(__name__)

def test_function(no = 0):
    print("This is a function in a python script")
    return no + 1

def say_hi(name):
    print("Hi there,", name, "!")
    
def main():
    test_variable = 10
    print(f'The test variable value is {test_variable}')
    
    
if __name__ == "__main__":
    main()