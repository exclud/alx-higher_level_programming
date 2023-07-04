#!/usr/bin/python3
def magic_string():
    result = "BestSchool"
    for i in range(1, 11):
        print(", ".join([result] * i) + "$")
