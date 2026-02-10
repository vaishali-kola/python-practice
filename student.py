rolls=[1,2,3]
names=["vaishu","anu","vijaya"]
r=int(input("enter roll number:"))
if r in rolls:
    index=rolls.index(r)
    print("exists")
    print("roll:",rolls[index])
    print("name:",names[index])
else:
    print("not exists")
    n=input("enter name:")
    rolls.append(r)
    names.append(n)
    print("added successfully")
print(rolls)
print(names) 