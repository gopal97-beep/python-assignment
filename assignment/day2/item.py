items=[
    {
        "id":"1",
        "name":"ball",
        "cost":"50",
        "brand":"mrf",
        "rating":"3",
        "discount":"20",
        "category":"sports"
    },
    {

        "id":"2",
        "name":"apple",
        "cost":"20",
        "brand":"sonar",
        "rating":"4",
        "discount":"10",
        "category":"food"
    },
    {   "id":"2",
        "name":"soap",
        "cost":"40",
        "brand":"cinthol",
        "rating":"2",
        "discount":"30",
        "category":"personal"
    }
]
print("1.sort by cost")
print("2.sort by rating")
print("3.sort by discount")
in1=0
value=["cost","rating","discount"]
in1=int(input())

print("1.low to high or 2.high to low")
in2=int(input())
if in2==1:
    items.sort(key=lambda el:el[value[in1-1]])
    print(items)
elif in2==2:
    items.sort(key=lambda el: el[value[in1 - 1]])
    items.reverse()
    print(items)


