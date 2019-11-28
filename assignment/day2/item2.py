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
print("1.Filter by brand")
print("2.Filter by name")
print("3.Filter by category")
in1=0
in1=int(input())
value=["brand","name","category"]
print("enter option name")
name=input()

obj=filter(lambda el:el[value[in1-1]]==name,items)
for a in obj:
 print("id={id},name={name},cost={cost},brand={brand},rating={rating},discount={discount},category={category} ".format(**a))




