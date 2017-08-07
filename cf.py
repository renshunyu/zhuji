# coding: UTF-8
'''
Created on 2017年7月13日

@author: renshunyu
'''
import os
import os.path
import shutil

rootdir = "J:\\movie\\test\\"

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#    for dirname in  dirnames:                       #输出文件夹信息
#        print "parent is:" + parent
#        print  "dirname is" + dirname

    for filename in filenames:                        #输出文件信息
        print "parent is:" + parent
        print "filename is:" + filename
        print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
        if parent == rootdir:
            print parent+"hah"
        else:
            print parent+"fghs"
            if not os.path.exists(rootdir+filename):
                shutil.move(os.path.join(parent,filename),rootdir)
            else:
                if not os.path.exists(rootdir+"temp\\"+filename):
                    shutil.move(os.path.join(parent,filename),rootdir+"temp\\")
                else:
                    pass

                         

