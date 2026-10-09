"""Types of inheritance."""


class Parent:
    def show(self):
        print("parent")


# Single
class Child(Parent):
    pass


# Multiple
class Mother:
    def skill(self):
        print("cooking")


class Father:
    def work(self):
        print("engineer")


class Kid(Mother, Father):
    pass


# Multilevel: Parent -> Child -> GrandChild
class GrandChild(Child):
    pass


# Hierarchical: one parent, many children
class Child2(Parent):
    pass


# Hybrid: combination of the above
class Hybrid(Child, Child2, Mother):
    pass


if __name__ == "__main__":
    GrandChild().show()
    Kid().skill()
    Kid().work()
    Hybrid().show()
