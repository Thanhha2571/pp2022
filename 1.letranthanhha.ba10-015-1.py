def numberofstudents():
    numberofstudents = int(input("Number of students in class"))
    return numberofstudents

def StudentInfo(numberofstudents):
    students = []
    for i in range(0,numberofstudents):
        student_id = input("Enter student ID:")
        student_name = input("Enter student name:")
        student_dob = input("Enter DoB:") 
        student ={
            "Student ID": student_id,
            "Student name": student_name,
            "DoB": student_dob,
            "marks": {}
        }
        students.append(student)
    return students
    
def StudentList(students):
    print("LIST OF ALL STUDENTS")
    for student in students:
        print(students)
        
def numberofcourses():
    numberofcourses = int(input("Number of courses"))
    return numberofcourses

def CourseInfo(numberofstudents):
    courses = []
    for i in range(0,numberofcourses):
        course_id = input("Enter course ID:")
        course_name = input("Enter course name:")
         
        course ={
            "Course ID": course_id,
            "Course name": course_name,
    
        }
        courses.append(course)
    return courses
def CourseList(courses):
    print("LIST OF ALL COURSES")
    for course in courses:
        print(courses)
        
def SelectCourse():
    CourseList(course)
    courseid = input("Enter course ID:")
    return courseid
    print(f"Enter marks of course {courseid} for students: ")
    for student in students:
        mark = float(input(f"- Student {student['student_name']}:"))
        student ["marks"][courseid] = mark
numberofstudents = numberofstudents();
students = StudentInfo(numberofstudents)
StudentList(students)
numberofcourses = numberofcourses();
courses = CourseInfo(numberofstudents)
CourseList(courses)
SelectCourse(courses)
print(students)
