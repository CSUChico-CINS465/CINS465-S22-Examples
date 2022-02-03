print("Hello World")

x = 2
x = 3.0
x = "string"
x = False
# def x(x):
#     print(x)

# x(x)
# print(x + str(1))


def fun(a, b=0):
    print(a)
    print(b)

# fun(2)


a = [1, 2, 3, 4]
a.append(5)
a.insert(0, 6)
a = [7] + a
a += [8]
# i = 0
# while i < len(a):
#     print(a[i])
#     i+=1

# a = list()
# for i in range(len(a)):
#     a[i]+=1
# a = [x + 1 for x in a]
# for x in a:
#     print(x)

tp = (1, 2, 3)
# a = [x+1 for x in tp]
# for i in a:
#     print(i)

d = {
    "key": "value",
    "key2": "value2"
}
d["key3"] = 3
d[2] = 2
d[3.0] = 4
d[True] = 5
d[tp] = 6
d[tuple(a)] = fun
# print(d)
# d[tuple(a)](3,4)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(self.name)

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old."

# child class
class Employee(Person):
    def __init__(self, name, age, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, age)

    def __str__(self):
        return self.name + " is " + self.post



p1 = Employee("John", 36, 50000, "Widget Technician")

print(p1)
