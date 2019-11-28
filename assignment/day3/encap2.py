class product:
    def __init__(o,id1,n,c,b,d,ca):
        o.id=id
        o.name=n
        o.cost=c
        o.brand=b
        o.discount=d
        o.category=ca




obj1=product("1","apple","20","sonar","20","food")
obj2=product("2","ball","40","mrf","30","sports")
obj3=product("3","soap","10","cinthol","10","self")
item=product.__dict__
print(item)


print("1.sort by cost")
print("2.sort by rating")
print("3.sort by discount")
in1=0

in1=int(input())

print("1.low to high or 2.high to low")
in2=int(input())
if in2==1:
    value = ["cost", "rating", "discount"]



    item.sort(key=lambda el: el[value[in1 - 1]])
    print(item)
elif in2==2:
    value = ["cost", "rating", "discount"]
    item.sort(key=lambda el: el[value[in1 - 1]])

    item.reverse()
    for a in item:
        print(a.name)






