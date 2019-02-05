grades = ("freshman","sophmore","junior","senior")

students = []

import csv

with open('example_students.csv',newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter = ' ')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f"Column names are {", ".join(row)}")
            line_count += 1
        else:
            students.append(Student({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]})
            line_count += 1
    print(f'Processed {line_count} lines.')

class Student:
    def __init__(self, fName,mName,lName, age, guid,grade,gpa):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.age = age
        self.guid = guid
        self.grade = grade
        self.gpa = gpa

    def printName(self):
        return (self.fName+" " + self.mName+ " " + self.lName)

print("There are " + line_count + " students")
print(students[0])
# p1 = Student("John","Dinkle","Ain", 36,1,2.5)

# print(p1.name)
# print(p1.age)

#print(vars(p1))    //print all class variables
# print(p1.printName())
