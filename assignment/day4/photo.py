fo=open('C:\\Users\\gkulkarni29\\Pictures\\download.jpg','rb')
f1=open('copy2.jpg','wb+')
data=b''
for i in fo:
    data+=i

f1.write(data)
f1.close()
fo.close()