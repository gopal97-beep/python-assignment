class person:
    """this is for oop"""
    team="konoha" #class level encapsulation
    def sayjhi(p):
        print("santoruo"+p.name+" "+p.lname)


    def __init__(o,f,l):
        o.name = f
        o.lname = l
    def __del__(self):
        print("destructor called for"+self.name+self.lname+self.team)


'''print(type(obj))
#person.sayjhi()
obj.name="gopal" #object level encapsulation
obj.lname="kulkarni"
print(person.team)
obj.team="enies lobby" #object level property preceeds(higher priority)
print(obj.lname+" "+obj.name+" "+obj.team)
print(obj.__class__.team) #to get class level property
obj.__class__.sayjhi(obj)
obj.sayjhi() #translates to person.sayhi(obj)
'''
"""
person.team="wano"
obj2=person()
obj.name="itachi" #object level encapsulation
obj.lname="uchiha"
print(person.team)
print(obj.lname+" "+obj.name+" "+obj.team)
"""

"""
obj.setval("sasuke","uchiha")

obj.sayjhi()
"""
obj=person("d","Roger")
obj.sayjhi()
#obj.__del__()
setattr(obj,"pan","ADSA")
print(obj.pan)
print(getattr(obj,"pan"))
print(hasattr(obj,"pan"))
delattr(obj,"pan")
print(hasattr(obj,"pan"))
print(person.__name__)
print(person.__module__)
print(person.__doc__)
print(person.__dict__)

print(obj.__class__.__name__)
print(obj.__module__)
print(obj.__doc__)
print(obj.__dict__)