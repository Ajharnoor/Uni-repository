from Students import *

s0 = Students()
s1 = Students("Medhi","Miah", 21276555, "Biology")
s2 = Students("Thamid","Hussain", 21263847, "Business")
s3 = Students("Matthew","Wilson", 21287653, "Finance")

Students = [s0, s1, s2, s3]
for s in Students:
    print()
    s.showDetails()


