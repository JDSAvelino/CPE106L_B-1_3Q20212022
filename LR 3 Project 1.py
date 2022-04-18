class Students(object):

    def __init__(self, name, number):
        self.name = name
        self.grade = []
        for count in range(number):
            self.grade.append(0)

    def getName(self):
        return self.name
    def setScore(self, i, score):
        self.grade[i - 1] = score
    def getScore(self, i):
        return self.grade[i - 1]
    def getAverage(self):
        return sum(self.grade) / len(self.grade)
    def getHighScore(self):
        return max(self.grade)
    def __eq__(self,student):
        return self.name==student.name
    def __lt__(self,student):
        return self.name<student.name
    def __ge__(self,student):
        return self.name>=student.name
    def __str__(self):
        return "Student Name: " + self.name  + "\nResult: " + \
               " ".join(map(str, self.grade))

def main():
    student = Students("Abraham", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 95)
    print(student)
    print('\nSecond Student: ')
    student2=Students('John Derick',5)
    print(student2)
    for i in range(1, 6):
        student.setScore(i, 90)
    print('\nThird Student: ')
    student3 = Students('Vince', 5)
    print(student3)
    for i in range(1, 6):
        student.setScore(i, 99)
    print('\nIs Student 1 equal to Student 2')
    print(student == student2)
    print('Is student 1 greater than Student 2')
    print(student>=student2)
    print('Is Student 1 less than Student 2')
    print(student<student2)
    print('\nIs Student 1 equal to Student 3')
    print(student == student3)
    print('Is student 1 greater than Student 3')
    print(student >= student3)
    print('Is Student 1 less than Student 3')
    print(student < student3)
    print('Is Student 2 less than Student 3')
    print(student2 < student3)
    print('Is Student 2 greater than Student 2')
    print(student2 < student3)
    print('Is Student 2 equal to Student 3')
    print(student2 == student3)


if __name__ == "__main__":
    main()
