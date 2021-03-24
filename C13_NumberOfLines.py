import os
filename = input("file name: ")
if os.path.isfile(filename):
 f = open(filename,'r')
 count = 0
 for line in f:
  count = count+1
print("no.of lines", count)