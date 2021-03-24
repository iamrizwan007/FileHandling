import os
file = input("enter file name: ")
if os.path.isfile(file)==True:
 print("file exists:",file)
 with open(file,'r') as f:
  text = f.read()
  print("Content of the file is:")
  print('*'*40)
  print(text)
  print('*'*40)
else:
 print("file does not exist")
