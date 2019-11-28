import os.path
filename="C:\\Users\\gkulkarni29\\Desktop\\test"
print(os.path.splitext(filename))
list=os.listdir(filename)
for i in list:
   # print(os.path.splitext(i))
    if os.path.splitext(i)[1]==".log":
            print("true")
            fo=open(filename+"\\"+i,'r')
            for j in fo:
                   print(j)




for i in os.listdir("C:\\Users\\gkulkarni29\\Desktop\\test"):
    if os.path.splitext(i)[1]==".log":
       print(open(filename + "\\" + i, 'r').read())


