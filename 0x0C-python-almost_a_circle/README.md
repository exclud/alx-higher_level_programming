
# Python - Almost a Circle

Getting Ready for the AirBnB project. 

All Python files are executable and use the pycodestyle (version 2.8.*)

Modules, Classses and Functions are also documented to explain their purpose. 
## Deployment

Since it is a requirment to start every executable python file using "#!/usr/bin/python3" Use this command to do it once.  

```bash
for file in *; do echo '#!/usr/bin/python3' | cat - "$file" > temp && mv temp "$file"; done
```


## Running Tests

To run tests, run the following command

```bash
  python3 -m unittest discover tests
```

Example using to test each single file
```bash
  python3 -m unittest tests/test_models/test_base.py
```
 