
f = open(r'ex1.txt')
students={}
for line in f:
    line = line.replace("\n","")
    line = line.split(" ")
    name = line[0]
    grade = float(line[1])
    students.update({name:grade})

maxGrade = max(grade for grade in students.values())
almostMaxGrade = max(grade for grade in students.values() if grade < maxGrade)
thoseStudents = [student for student,grade in students.items() if grade == almostMaxGrade] 
thoseStudents.sort()
print(thoseStudents)