#!/usr/bin/python3
print("".join("{} ".format(chr(i)) for i in range(ord('a'), ord('z')+1)
               if chr(i) not in {'q', 'e'}), end="")
