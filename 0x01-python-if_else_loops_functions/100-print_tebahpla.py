#!/usr/bin/python3
print("".join("{}{}".format(chr(i), chr(i).upper()
                            if i % 2 else "")
              for i in range(122, 96, -1)))
