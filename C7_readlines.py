f = open('MobNumber.txt','r')
l = f.readlines()
print(l)
for line in l:
 print(line,end='')
f.close()