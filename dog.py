# Henry Heisig (hheisig51)
# 2022-03-09
# Dog Class
# Copied from Karl Helmstetter (helmstk1)


class Dog:
    """Dog will define dogs by their breed, age, and types of tricks known."""

    kind = "canine"  # class variable shared by all instances

    # An __init__ method is for stuff that you need to run at instantiation
    # This is similar to Arduino's void setup().
    def __init__(self, breed, age):
        self.breed = breed  # instance variable unique to each instance
        self.age = age
        self.tricks = []

    # let's define two methods, addTrick and bark
    def addTrick(self, trick):  # Back in main.py, I can add any trick I want
        self.tricks.append(trick)

    def bark(self):
        return "arf!"
