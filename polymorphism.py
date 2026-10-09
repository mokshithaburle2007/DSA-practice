"""Polymorphism in Python: overriding, and overloading via *args."""


# Method overriding
class Animal:
    def sound(self):
        print("some sound")


class Dog(Animal):
    def sound(self):
        print("bark")


# Method overloading is not built in; use variable-length arguments
def add(*args):
    return sum(args)


if __name__ == "__main__":
    Animal().sound()
    Dog().sound()
    print(add(1, 2))
    print(add(1, 2, 3, 4))
