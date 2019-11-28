with open('demo1.txt','a') as fo:
  fo.write("hello zoro\n")
  fo.write("hello luffy\n")
  fo.write("hello shravan")

fo=open('demo1.txt','r')
 #read first 10 characters
print("first"+fo.read(10))
print("second" ,fo.read(10)) #next 10 chars
fo.close()

fo=open('demo.txt','r')
print(fo.readline()) #when called first it will read first line
fo.close()

fo=open('demo1.txt','r')
for line in fo:
    print(line)
fo.close()

fo1=open('demo2.txt','a+')
fo1.write('hello gopal')
for line in fo1:
    print(line)
fo1.close()

fo2=open('demo.txt','rb')
print(fo2.read(10).decode(),end="")
fo2.close

fo2=open('demo4.txt','ab')
fo2.write(b'gopal')
fo2.close()
