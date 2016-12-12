class Students():
    def __init__(self,firstname="Ajhar",lastname="Noor",studentID=21276244,course="Information Technology"):
        self.firstname=firstname
        self.lastname=lastname
        self.studentID=studentID
        self.course=course

    def showDetails(self):
        print("firstname\t", self.firstname)
        print("lastname\t", self.lastname)
        print("studentID\t", self.studentID)
        print("course\t", self.course)


