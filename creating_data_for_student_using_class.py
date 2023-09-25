'''Assignment 6 by DEV YADAV'''
class Subject:
    def __init__(self, sub, credit):
        self.sub=sub
        self.credit=credit
    def __str__(self):  #because of printing the screen
        return self.sub+" contains credit=" +str(self.credit)

class Student:
    def __init__(self, fname, lname):  
        self.fname=fname
        self.lname=lname
        self.subject=[]
    def addSubject(self, subject):
        self.subject.append(subject)
    def __str__(self):
        return self.fname+" "+self.lname 

def main():
    print("Enter the name of the students and subjects they choose")
    print("press enter to quit..")
    students=[]
    while True:
        studentfname=input("\nFirst name of the student(click enter to quit): ")
        if studentfname !="":
            studentlname=input("Surname/lastname of the student: ")
        elif studentfname=="":
            break
        student=Student(studentfname, studentlname)  #it creates a new list of student
        students.append(student)
        while True:
            subject=input("Enter the name of subject(click enter to quit): ")
            if subject=="":
                break
            credit=input("Enter credits of subject(3/1.5/15): ")
            subject=Subject(subject, credit)# it creats a new subject object
            student.addSubject(subject)
    for student in students:
        print(student," tooks the subject: ")
        for subject in student.subject:
            print("\t",subject)

main()
            
