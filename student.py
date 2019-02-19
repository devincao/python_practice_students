grades = ("freshman","sophmore","junior","senior")

students = []

import csv

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
        return (str(self.fName)+" " + str(self.mName)+ " " + str(self.lName))

with open('example_students.csv',newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter = ',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]})
            students.append(Student({row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}))
            line_count += 1
    print(f'Processed {line_count} lines.')

print("There are " + str(line_count) + " students")
# print(vars(students[0]))

for student in students:
    print(student.printName())
    print(student.guid)

searchID = input("Enter ID of student to identify: ")
for student in students:
    if str(student.fName).find(searchID) != -1:
        print(student.fName)
    # else:
        # print(student.mName)
print("Searched ID: " + searchID)
# p1 = Student("John","Dinkle","Ain", 36,1,2.5)

# print(p1.name)
# print(p1.age)

#print(vars(p1))    //print all class variables
# print(p1.printName())
