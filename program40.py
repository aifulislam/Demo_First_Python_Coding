#Method Overriding----------

class Phone:
    def __init__(self):
        print("I am a phone class")

class Apple(Phone):
    #init
    pass
s = Apple()

#Method Overriding----------

class car:
    def __init__(self):
        print("I am a class of car")

class BMW(car):
    #init
    pass

c = BMW()

#Method Overriding----------

class laptop:
    def __init__(self):
        print("It is laptop class")

class Apple(laptop):
    pass

l = Apple()
print(issubclass(Apple,laptop))