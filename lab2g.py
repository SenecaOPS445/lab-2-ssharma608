#!/usr/bin/env python3

#Author: Shikshya Sharma
#Author ID: ssharma608@myseneca.ca


#Date Created:2025/02/05

import sys 

arguments = sys.argv
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])
while timer > 0:
    print (str(timer))
    timer = timer - 1

print("blast off!")


















