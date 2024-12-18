def studentInfo () :
    id = input("Enter student ID : ")
    name = input("Enter student name : ")
    dob = input("Enter student DOB : ")
    return {"id":id, "name":name, "dob":dob}
def courseInfo() :
    id = input("Enter course ID : ")
    name = input("Enter course name : ")
    return {"id":id, "name":name}
def numStudent() :
    num =int(input("Enter student number in class : "))
    student =  [ ]
    for i in range(int(num)):
        temp = studentInfo()
        student.append(temp)
    return student
def numCourse() :
    num =int(input("Enter course number in class : "))
    course = []
    for i in range(int(num)):
        temp = courseInfo()
        course.append(temp)
    return course
def listCourses(courses) :
    print("\nList of coureses")
    for course in courses :
        print("ID: {}, Name: {}".format(course["id"], course["name"]))
def listStudents(students) :
    print("\nList of students")
    for student in students :
        print("ID: {}, Name: {}".format(student["id"], student["name"])),
student['name'], student['dob']
def inputMarks(students, courses, marks):
    listCourses(courses)
    print("Enter the courses id: ")
    course = input()
    if course not in marks:
        marks[course] = { }
    listStudents(students)
    print("Enter student ID to input your mark: ")
    students = input()
    marks[course][students] = float(input("Enter mark: "))
    return marks
def showMarks(students, marks) :
    course = input("What course do you want to see ?: ")

    if courses not in mark or marks[courses] == { }:
        print("This code haven't entered the mark")
    else:
        for student in students:
            if (student["id"] in marks[course]):
                print("Student id: {}, Mark: {}".format(student["id"], marks[course][student["id"]]))
            else:
                print("Student id: {}, Mark: Not entered".format(student["id"]))
marks = {}
while (True):
    print("---ENTER YOUR CHOICE---")
    print("--0. EXIT THE PROGRAM--")
    print("--1. INPUT STUDENTS----")
    print("--2. INPUT COURSES-----")
    print("--3. LIST COURSES------")
    print("--4. LIST STUDENTS-----")
    print("--5. INPUT MARK--------")
    print("--6. SHOW MARK---------\n")


    choice = int(input())
    if (choice == 0):
        break
    elif (choice == 1):
        students = numofStudents()
    elif (choice == 2):
        courses = numofCourses()
    elif (choice == 3):
        listCourses(courses)
    elif (choice == 4):
        listStudents(students)
    elif (choice == 5):
        marks = inputMarks(students, courses, marks)
    elif (choice == 6):
        showMarks(students, marks)
    else:
        print("Invalid choice")





