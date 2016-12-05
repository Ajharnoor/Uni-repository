class People():
    def __init__(self, name, age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def showDetails(self):
        print (self.name, self.age,self.gender)


Harry=People("harry",23,"male")
print(Harry.gender)

nick=People("nick",23,"male")
print(nick.name)

