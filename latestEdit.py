import sys
print("\n\n")
print("******************************************************************************************************")
print("*  ************************************************************************************************  *")
print("*  *                             STUDENT MANAGEMENT SYSTEM                                        *  *")
print("*  ************************************************************************************************  *")
print("******************************************************************************************************")
class deverror(Exception):
    pass
class student:
    def __init__(self):
        self.name=str(input("enter student name:"))
        self.age=int(input("enter student age: "))
        self.studyYear=int(input("enter in which year the student is studying(like 2018,2019...):"))
        self.finishYear=int(input("year of passing(like 2018,2019...): "))
        self.dept=str(input("enter the department: "))
        #self.address=input("enter the address: ")
        

    def show(self):
        print("Student name:",self.name)
        print("Student age:",self.age)
        print("Student study year:",self.studyYear)
        print("Year of passing: ",self.finishYear)
        print("Student department:",self.dept)
        #print("student address:",self.address)


class result(student):
    def __init__(self):
        student.__init__(self)
        self.m=int(input("Enter your Math no:"))
        self.c=int(input("Enter your Chemistry no:"))
        self.p=int(input("Enter your Physics no:"))
        #print("percentage required for passing:50%")
        #self.per=int(input("percentage required for passing:50%"))

    def percentage(self):
        return (self.m+self.c+self.p)/3
    #def yearIncreament(self):
     #   self.year+=1
       # return self.year

    def rslt(self):
        if self.percentage()>=50:
            self.studyYear+=1
            self.age+=1
            if self.percentage()<=65 and self.percentage()>=50:
                return("pass")
            elif self.percentage()>65 and self.percentage()<=80:
                return("good")
            elif self.percentage()>80:
                return("excellent")
            #self.yearIncreament()
            #return("pass")
        else:
            self.studyYear+=1
            self.finishYear+=1
            self.age+=1
            return("fail")
    def readmission(self):
        self.feesRequired=40000
        print("Fees required for admission: 40000")
        self.feesGiven=int(input("Enter Fees for Admission: "))
        self.withintime=input("say yes or no if the fees is given within time or not\n: ")
        if self.feesGiven==self.feesRequired and self.withintime=="yes":
            print("Admission is Successful\nAfter Admission Student Details:\n\n")
            student.show(self)
        if self.feesGiven<self.feesRequired or self.withintime=="no":
            print("Admission Is Not Done")
        
        
        

    def show1(self):
        print("\n\n")
        student.show(self)
        print("Marks for Math=",self.m)
        print("Marks for Chemistry=",self.c)
        print("Marks For physics=",self.p)
        print("Average percentage is:",self.percentage())
        print("Percentage required for passing:50%")
        print("Aggregate result is:",self.rslt())
        try:
            if self.studyYear>self.finishYear and self.percentage()>=50:
                raise deverror
            else:
                print("Fill Up Your Admission Details:\n")
                self.readmission() 
                #student.show(self)
        except deverror:
            print("Course is completed for ",self.name)

class newadmissionProcess(student):
    def __init__(self):
        #super(newadmissionProcess,self).__init__()
        student.__init__(self)
        self.fat=str(input("Enter your father's  name: "))
        self.ph_no=int(input("Enter your ph no(must be 10 digit): "))
        self.address=str(input("Enter the address: "))
    def admissionprocess(self):
        self.feesRequired=40000
        print("Fees required for admission: 40000")
        self.feesGiven=int(input("Enter fees for admission: "))
        print("\nChoose one of the following\n")
        s=int(input("1.Are you satisfied?\n2.do you want to reEnter your details?\n3.I dont want to admit in this college\n:"))
        if s==1:
            if self.feesGiven==self.feesRequired:
                print("admission is successful\nstudent details----->\n\n")
                student.show(self)
                print("Father's name: ",self.fat)
                print("Ph_no: ",self.ph_no)
                print("Student address:",self.address)
                self.std=str(self.studyYear)
                self.fin=str(self.finishYear)
                self.no=str(self.ph_no)
                print(("Your id no is: %s/%s-%s/%s") % (self.dept,self.std[len(self.std)-2:len(self.std)],self.fin[len(self.fin)-2:len(self.fin)],self.no[7:]))
               # print(self.dept,"/",self.studyYear%2000,"-",self.finishYear%2000)
            if self.feesGiven<self.feesRequired:
                print("Admission is not done")
        if s==2:
            return -1
        if s==3:
            print("Thank You")
        
        
    
            
x=int(input("Are you a new comer or not?\npress 1 for yes\npress 2 for no\n:"))
if x==2:
    #print("student1 details>>>>>>")
    #s=student("dev",21,"cse",3,"Bagnan")
    #s.show()
    print("\n\nENTER YOUR DETAILS")
    r=result()
    r.show1()
if x==1:
    #print("")
    #print("student2 details>>>>>>")
    #r1=result("sayan",22,"ece",4,"kol",70,60,100)
    #r1.show1()
    print("\nENTER STUDENT DETAILS FOR ADMISSION\n")
    for i in range(1,100):
        a=newadmissionProcess()
        ob1=a.admissionprocess()
        if ob1==-1:
            continue
        else:
            break
