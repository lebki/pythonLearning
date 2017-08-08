print("Welcome")
a = 4
b = 4.21
print(a+b)
print("tomek".capitalize())

name = "Python"
machine = "HAL"

print("Nice to meet you {0}. I am {1}".format(name,machine))

p = True
b = False

i = 1
j = 2

print(str(p))
print(int(p))

folder = None

if p:
    print("True P")
else:
    print("False P")


print("wiekszy") if i>j else print("mniejszy")

names = ["Mark", "Katarina", "Jessica",4]
print(names[-1])
names.append(90)
print(names[-1])
print("Marky" in names)
print(len(names))

for name in names:
    print("Studen is {0}".format(name))

oop = 0
for name in range(len(names)):
    oop+=1
    print(oop)


for name in names:
    if name == "Jessica":
        print("Found {0}".format(name))
        break
    print("Looking for {0}".format(name))


student ={
    "name" : "Mark",
    "id" : 123
}

print("Student {0}".format(student["id"]))

try:
    name = student["names"]
except Exception as error:
    print("No names pattern")
    print(error)