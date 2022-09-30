class Dog:
    age = 3

    def __init__(self, name):
        self.name = name
        # self.age = 24

d = Dog('哈士奇')

print(Dog.age)
print(d.name, d.age)
print('是吗')