0x0F. Python - Object-relational mapping

## Deployment

It is a requirement to start every Python file with the '#!/usr/bin/python3' as the first line.
Here is the command to do so all at once. Make sure to be in the current working directory. 

```bash
  for file in *; do echo '#!/usr/bin/python3' | cat - "$file" > temp && mv temp "$file"; done

```
