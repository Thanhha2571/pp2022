class Student:
    def __init__(self, studentid, studentname, studentDoB):
        self.studentid = studentid
        self.studentname = studentname
        self.studentDoB = studentDoB

    def get_studentid(self):
        return self.studentid

    def get_studentname(self):
        return self.studentname

    def get_studentDoB(self):
        return self.studentDoB

    def set_studentid(self, studentid):
        self.studentid = studentid

    def set_studentname(self, studentname):
        self.studentname = studentname

    def set_studentDoB(self, studentDoB):
        self.studentDoB = studentDoB

    def displayStudentInfo(self):
        print("- Student ID:" +self.studentid + ", Student name:" + self.studentname + ", Student DoB:" +self.studentDoB)
        

class Course:
    def __init__(self, courseid, coursename):
        self.courseid = courseid
        self.coursename = coursename

    def get_courseid(self):
        return self.courseid

    def get_coursename(self):
        return self.coursename

    def set_courseid(self, courseid):
        self.courseid = courseid

    def set_coursename(self, coursename):
        self.coursename = coursename

    def displayCourseInfo(self):
        print("- Course ID:" + self.courseid + ", Course name:" +self.coursename)


def numberofstudent():
    numberofstudent = int(input("Number of students in class:"))
    return numberofstudent


def StudentInfo():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_DoB = input("Enter student DoB: ")
    return student_id, student_name, student_DoB


def numberofcourse():
    numberofcourse = int(input("Number of courses:"))
    return numberofcourse


def CourseInfo():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return course_id, course_name



if __name__ == "__main__":
    students = []
    courses = []

    numberofstudent = numberofstudent()
    for i in range(0, numberofstudent):
        studentid, studentname, studentDoB = StudentInfo()
        students.append(Student(studentid, studentname, studentDoB))
    print("LIST ALL OF STUDENTS:\n")
    for student in students:
        student.displayStudentInfo()
    
    
    numberofcourse = numberofcourse()
    for i in range(0, numberofcourse):
        courseid, coursename = CourseInfo()
        courses.append(Course(courseid, coursename))


    print("LIST ALL OF COURSES:\n")
    for course in courses:
        course.displayCourseInfo()
