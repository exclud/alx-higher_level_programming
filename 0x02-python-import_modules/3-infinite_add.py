#!/usr/bin/python3
import sys

def main():
    args_as_ints = [int(arg) for arg in sys.argv[1:]]
    
    print(sum(args_as_ints))
    
if __name__ == "__main__":
    main()
   