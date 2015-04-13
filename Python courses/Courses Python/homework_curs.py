# coding:utf-8
import os
import re
dirName = 'Papka'
listDer = os.listdir(dirName)
for fileName in listDer:
    if '.txt' in fileName:  # нахождение подстроки в строке 'if substring in string'
        #os.path.splitext(path) - разбивает путь на пару (root, ext), где ext
        # начинается с точки и содержит не более одной точки.
        textFile = open(dirName+"/"+fileName)
        print textFile
        count = 0
        #try:
        for line in textFile:
            if re.findall("""[p|P]ython""", line):
                count+=1
                print line
        #except:
         #   f.close(dirName+"/"+fileName)
        print count
