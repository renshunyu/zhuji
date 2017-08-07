# coding: UTF-8
'''
Created on 2017年7月16日

@author: renshunyu
'''
import logging
import random

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')


#a=[3,45,1,2,46,4,3,2,3,87]
#logging.debug(random.randint(1,10000))
#a = [random.randint(1,10000) for i in range(1,10000)]
#logging.info(a)
#for i in range(0,len(a)-1):
#    for j in range(0,len(a)-i-1):
#        if a[j] > a[j+1] :
#            temp = a[j+1]
#            a[j+1] = a[j]
#            a[j] = temp
#logging.info(a)

#b = [random.randint(1,10000) for i in range(1,10000)]
#logging.info(b)
#for i in range(0,len(b)-1):
#    temp = b[i]
#    for j in range(i,len(b)-1):
#        if temp > b[j+1]:
#            temp =b[j+1]
#            index = j+1
#    b[index] = b[i]
#    b[i] = temp
#logging.info(b)

#c = [random.randint(1,10000) for i in range(1,10000)]
#logging.info(len(c))
#logging.info(c)
#for i in range(1,len(c)):
#    temp = c[i]
#    for j in range(0,i):
#        if c[i-1-j]>temp:
#            c[i-j]=c[i-1-j]
#            if i-1-j == 0:
#                c[i-1-j]=temp
#                break
#            continue
#        else:
#            c[i-j]=temp
#            break
#logging.info(c)

d = [random.randint(1,10000) for i in range(1,10000)]
#d = [3,45,1,2,46,4,3,2,3,87]
def parttition(x,y,z):
    mid = x[y]
    i=y+1
    j=0
    while i+j-1<z:
        if x[i]>mid:
            temp = x[z-j]
            x[z-j]=x[i]
            x[i] = temp
            j = j+1
        else:
            x[i-1]=x[i]
            i = i+1
    x[i-1] = mid
    return i-1
def sort(x,y,z):
    if y<z:
        m = parttition(x,y,z)
        sort(x,y,m-1)
        sort(x,m+1,z)

sort(d,0,len(d)-1)
logging.info(d)
        
        
        
    
    
    
        
    


            