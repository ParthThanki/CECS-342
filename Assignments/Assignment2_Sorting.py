class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.age}"

numbers = [645.41, 37.59, 76.41, 5.31, -34.23, 1.11, 1.10, 23.46, 635.47, -876.32, 467.83, 62.25]
people = [
    Person("Hal", 20), Person("Susann", 31), Person("Dwight", 19), Person("Kassandra", 21),
    Person("Lawrence", 25), Person("Cindy", 22), Person("Cory", 27), Person("Mac", 19),
    Person("Romana", 27), Person("Doretha", 32), Person("Danna", 20), Person("Zara", 23),
    Person("Rosalyn", 26), Person("Risa", 24), Person("Benny", 28), Person("Juan", 33),
    Person("Natalie", 25)
]

print(sorted(numbers))
print(sorted(people, key=lambda p: p.name))
print(sorted(people, key=lambda p: (-p.age, p.name)))
