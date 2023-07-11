
# Higher Level Programming in Python


Python and its inner workings


## Deployment

It is a requirment to start every Python file with the '#!/usr/bin/python3' as the first line.
Here is the command to do so all at once. Make sure to be in the current working directory. 

```bash
  for file in *; do echo '#!/usr/bin/python3' | cat - "$file" > temp && mv temp "$file"; done

```


## Folders
These are the folders in the directory. 
1. 0x00. Python- Hello World.
2. 0x01-python-if_else_loops_functions
3. 0x02. Python - import & modules
4. 0x03. Python - Data Structures: Lists, Tuples
5. 0x04. Python - More Data Structures: Set, Dictionary
6. 0x07. Python - Test-driven development
7. 0x08. Python - More Classes and Objects
8. 0x09. Python - Everything is object
9. 0x0A. Python - Inheritance
10. 0x0B. Python - Input/Output
