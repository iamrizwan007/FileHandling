f = open('abc.txt','r')
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)
print()

f = open('abc.txt','w')
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)

print()

f = open('abc.txt','a')
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)

print()

f = open('abc.txt','r+')
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)

print()

f = open('abc.txt','w+')
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)

print()

f = open('abc.txt','a+')
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)

print()

f = open('abc.txt','x')	#error as file already exists, file should not be available
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File Closed: ',f.closed)
print('Is File Readable: ',f.readable())
print('Is File Writable: ',f.writable())

f.close()
print('File closed: ',f.closed)