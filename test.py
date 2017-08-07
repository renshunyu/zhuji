'''
Created on 2017Äê6ÔÂ11ÈÕ

@author: renshunyu
'''

#!/usr/bin/env python
import os
for root,dirs,files in os.walk('/home/aiuap/rensy'):
    for name in dirs:
        print (os.path.join(root,name))