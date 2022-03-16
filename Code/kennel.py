# Henry Heisig (hheisig51)
# 2022-03-09
# Dog Class
# Borrowed from Karl Helmstetter (helmstk1), modified by Henry Heisig (hheisig51)

from dog import Dog

Rex = Dog("Golden", 8)  # make a Dog instance, Rex
Spot = Dog("Pit Bull", 12)  # make another Dog instance, Spot
Rex.addTrick("roll over")  # add a trick to Rex
Spot.addTrick("sit")  # add a trick to Spot
Spot.addTrick("play dead")  # add another trick to Spot

print(f"\nSpot:")
print(Spot.kind)  # print kind, which is inherited by all Dogs
print(Spot.breed)  # breed is specified at instantiation
print(Spot.age)  # age is specified at instantiation

# ln 14 was modified
# Added a `\n` new line to separate the printing from the terminal command

print(f"{Spot.tricks}\n")  # all dogs have a tricks array
# print()  # this is just to separate Rex and Spot

# ln 23 was commented out, and line 22 was modified.
# Instead of ln 23 printing a new line, ln 22 does that with `\n`

# Wouldn't it look nicer if we printer Rex's info on one line?

print("Rex:")
# print(Rex.kind, ", ", Rex.breed, ", ", Rex.age, ", ", Rex.tricks)
print(f"{Rex.kind}, {Rex.breed}, {Rex.age}, {Rex.tricks}\n")

# ln 31 was commented out, and replaced by ln 32.
# The old print function on ln 31 put spaces before the commas

Spot.age += 1  # you can modify Dog properties
print("Spot's new age:", Spot.age)  # see?
print(f"{Spot.bark()}\n")  # the bark method returns "arf"
