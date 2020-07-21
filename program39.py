#Parant class, Base class,Super class
#Child class ,Drived class, Sub class
#Inheritance------

class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can Message")

class samsang(Phone):

    def photo(self):
        print("You can take photo")

s = samsang()
s.call()
s.message()
s.photo()
print(issubclass(samsang,Phone,))

#Parent Class , Super Class , Base Class
#Child Class , Sub class , Drived Class
#Inheritance------

class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class Apple(Phone):
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")
    def photo(self):
        print("You csn photo")

s = Apple()
s.call()
s.message()
s.photo()
print(issubclass(Apple,Phone))




