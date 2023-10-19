import os.path
import sys
fname=input("Enter a filename: ")
if not os.path.isfile(fname):
    print("File",fname,"doesnt exists")
    sys.exit(0)
infile=open(fname,"r")
lineList=infile.readlines()
for i in range(20):
    print(i+1,":",lineList[i])
word=input("Enter the word: ")
cnt=0
for line in lineList:
    cnt+=line.count(word)
print("The word",word,"appears",cnt,"times in the file")