#!/usr/bin/node
0x12. JavaScript - Warm up

## Deployment

It is a requirement to start every Javascript file with the '#!/usr/bin/node' as the first line.
Here is the command to do so all at once. Make sure to be in the current working directory. 

```bash
  for file in *; do echo '#!/usr/bin/node3' | cat - "$file" > temp && mv temp "$file"; done

```
