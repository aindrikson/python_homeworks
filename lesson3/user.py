class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def sayName(self):
        print("Меня зовут ", self.name)

    def sayLastname (self):
        print("Моя фамилия ", self.lastname)

    def sayFullname(self):
        print("Мое полное имя ", self.name, self.lastname)