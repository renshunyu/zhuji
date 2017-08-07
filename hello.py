#coding:UTF-8
'''
Created on 2017年7月18日

@author: renshunyu
'''
import os
print(dir())
print(__builtins__)
print(__doc__)
print(__file__)
print(__name__)
print(__package__)
print(dir(os))

for i in dir():
    print("print("+i+")")