#coding:utf-8
import os
#listDer = os.listdir(dirName)
fileName = 'text.txt'
txtFile = open(fileName)
countOfWord = 0
count = 0
#for line in txtFile:
txt = txtFile.read()
countOfWord = txt.count("Django")
print 'Count of Django - %i'%(countOfWord)
template = txt.replace("Django", '{0}')
print '_____'
print template
print '______'
result = template.format('Django 1.6')
print result
print '_____'
txtFile.close()
txtFile = open(fileName)
for l in txtFile.readlines():
    #print l
    if l.rstrip().endswith(':'):
        count+=1
print 'Count of : - %i'%(count)
txtFile.close()
dir(txt)



