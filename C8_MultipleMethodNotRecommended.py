f = open('MobNumber.txt','r')
print(f.read(4))
print(f.readline())
print(f.readline())
print(f.read(4))
print("remaing data:")
print(f.read())
f.close()