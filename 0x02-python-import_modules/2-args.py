#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of arguments : .")
    else:
        arg_plural = "argument" if num_args == 1 else "arguments"
        print(f"Number of {arg_plural}:")
        
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
            
            
if __name__ == "__main__":
    main()