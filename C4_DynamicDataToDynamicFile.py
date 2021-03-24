filename=input("enter file name")
f = open(filename,'w')
while True:
 data = input("enter the data to append")
 f.write(data + '\n')
 option = input("do you want to continue[yes/no]: ")
 print(option.lower)
 if option.lower()== 'no':
  break