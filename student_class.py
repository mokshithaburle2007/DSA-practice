"""Class, __init__ and self."""


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name =", self.name)
        print("Age =", self.age)
        print("Gender =", self.gender)


if __name__ == "__main__":
    s = Student("Arjun", 19, "male")
    s.display()
