0x0B.Python - Input/Output

Since it is a requirment to start every executable python file using "#!/usr/bin/python3" Use this command to do it once.  

Use the command for file in *; do echo '#!/usr/bin/python3' | cat - "$file" > temp && mv temp "$file"; done
