f = open('MobNumber.txt','r')
line = f.readline()
while line!= '':
 print(line,end='')
 line=f.readline()