from dog import Dog

Rex = Dog("Golden", 8)      # make a Dog instance, Rex
Spot = Dog("Pit Bull", 12)  # make another Dog instance, Spot
Rex.addTrick("roll over")   # add a trick to Rex
Spot.addTrick("sit")        # add a trick to Spot
Spot.addTrick("play dead")  # add another trick to Spot

print("Spot:")
print(Spot.kind)        # print kind, which is inherited by all Dogs
print(Spot.breed)       # breed is specified at instantiation
print(Spot.age)         # age is specified at instantiation


print(Spot.tricks)      # all dogs have a tricks array
print()                 # this is just to separate Rex and Spot


# Wouldn't it look nicer if we printer Rex's info on one line?

print("Rex:")
print(Rex.kind, ", ", Rex.breed, ", ", Rex.age, ", ", Rex.tricks) 
Spot.age += 1                       # you can modify Dog properties
print("Spot's new age:", Spot.age)  # see?
print(Spot.bark())          # the bark method returns "arf"