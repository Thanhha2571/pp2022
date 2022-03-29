def Studentcount():
    return int(input("Number of students in class are:"));


def student_info(numberofstudents):
    students_list = [];
    for i in range(numberofstudents):
        print("Info of student", (i+1), ":");
        id_s = input("Student ID:");
        name_s = input("Student name:");
        dateofbirth = input("Date of birth:");
        students_list.append ({"- Student ID":id_s, "Student name":name_s, "DoB":dateofbirth})
    print(students_list);

def Coursecount():
   return int(input("Number of course:"));


def course_info(numberofcourses):
    courses_list = [];
    for i in range(numberofcourses):
        print("Info of course", (i+1), ":");
        id_c = input("ID course:");
        name_c = input("Name of course:");
        courses_list.append ({" - Course ID":id_c, "Name":name_c});
    print(course_info);
    
def findCourse(courses_list,id_c):
    id_mark = int(intput("Select ID course:"));
    for course in courses_list:
        if id_mark == id_c:
            return name_c;

def addMark():
    

numberofstudents = Studentcount();
students_list = student_info(numberofstudents);
numberofcourses = Coursecount();
course_list = course_info(numberofcourses);