def Studentcount():
    student_count = int(input("Number of students in class are:"));
    return student_count

class Student:
    def __init__ (self, ids, names, dateofbirth):
        self.ids = ids;
        self.names = names;
        self.dateofbirth = dateofbirth;

    
    def get_ids(self):
        return self.ids
        
    def get_names(self):
        return self.names
        
    def get_dateofbirth(self):
        return self.dateofbirth

    def set_ids(self, _ids):
        self.ids = _ids

    def set_names(self, _names):
        self.names = _names
        
    def set_dateofbirth(self, _dateofbirth):
        self.dateofbirth = _dateofbirth
        
    def displayStudent(self):
        print(f"- Student ID: {self.ids}")
        print(f"- Student Name: {self.names}")
        print(f"- DoB: {self.dateofbirth}")

def student_info():
    id_s = input("Student ID:");
    name_s = input("Student name:");
    dateofbirth_s = input("Date of birth:");
    return id_s, name_s, dateofbirth_s

def Coursecount():
    course_count = int(input("Number of course:"));
    return course_count


class Course:
    def __init__ (self, idc, namec ):
        self.idc = idc;
        self.namec = namec;
        
    def get_idc(self):
        return self.idc
        
    def get_namec(self):
        return self.namec
        

    def set_ids(self, _idc):
        self.idc = _idc

    def set_namec(self, _namec):
        self.namec = _namec
        
    def displayStudent(self):
        print(f"- Course ID: {self.idc}")
        print(f"- Course Name: {self.namec}")
def course_info():
    id_c = input("Course ID:");
    name_c = input("Course name:");
    return id_c, name_c