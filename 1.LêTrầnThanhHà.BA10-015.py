numofstudents = int(input("Number of students in class are:"));
listofstudent = [];
for i in range(numofstudents):
    student_info = {};
    name_student = input("Name of student:");
    ID_student = input("ID:");
    dateofbirth = input("Date of birth:");
    student_info["ID"] = ID_student;
    student_info["Name"] = name_student;
    student_info["Date of birth"] = dateofbirth;
    listofstudent.append(student_info);
print(listofstudent);


numofcourses = int(input("Number of courses:"));
listofcourse = [];
for i in range(numofcourse):
    course_info = {};
    name_course = input("Name of course:");
    ID_course = input("ID:");
    course_info["ID"] = ID_student;
    course_info["Name"] = name_student;
    listofcourse.append(course_info);
print(listofcourse);
