class school:

    def __init__(self,branch,teacher,department,currentNumb,salary):
        self.branch = branch
        self.teacher =  teacher
        self.department =  department
        self.currentNumb =  currentNumb
        self.salary = salary

    def showInformation(self):
        print("-"*45)
        print("Class Information: ")
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nCurrentNumb: {}\n".format(self.branch,self.teacher,self.department,self.currentNumb))
        print("-"*45)

    def depChange(self):
        newDeparment = input("Please write your new department: ")
        print("***Old department*** : ",self.department)
        self.department = newDeparment
        print("-"*45)
        print("Class Information: ")
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nCurrentNumb: {}\n".format(self.branch,self.teacher,self.department,self.currentNumb))
        print("-"*45)
    
    def showSalary(self):
        print(f"{self.teacher} 's salary is {self.salary}")



class manager(school):
    print("Manager Panel: ")

    def __init__(self,branch,teacher,department,currentNumb,salary,seniority):
        super().__init__(branch,teacher,department,currentNumb,salary)
        self.seniority = seniority
    
    #Overriding
    def showInformation(self):
        print("-"*45)
        print("Class Information: ")
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nCurrentNumb: {}\nSeniority: {}".format(self.branch,self.teacher,self.department,self.currentNumb,self.seniority))
        print("-"*45)
    
    def incSalary(self):
        print(f"Welcome to inc salary screen teacher: {self.teacher}")
        incAmount = int(input("Please write in TL: "))
        self.salary = int(self.salary) + incAmount
        print(f"{self.teacher}'s teacher new salary is {self.salary}")

className = input("Please writing ur branch no: ")
teacherInfo = input("Please writing ur name: ")
takeDep = input("Please writing ur dep: ")
currentNo = input("Please writing ur current class student: ")
enterSalary = int(input("Please write ur salary: "))
print("Just manager")
takeSeniority = input("Write seniority: ")
if not takeSeniority:
    print("Teacher mode...")

createClass = input("Create a class:")

while True:
    if not takeSeniority:
        createClass = school(className,teacherInfo,takeDep,currentNo,enterSalary)
        askQuestion = input("1-Show Info\n2-Changedep\n3-showSalary\n")
        if askQuestion == "1":
            createClass.showInformation()
        elif askQuestion == "2":
            createClass.depChange()
        elif askQuestion == "3":
            createClass.showSalary()
        else:
            print("Not selected")
    
    else:
        print("Manager mode...")
        createClass = manager(className,teacherInfo,takeDep,currentNo,enterSalary,takeSeniority)
        askQuestion2 = input("1-Show Info\n2-incSalary\n")
        if askQuestion2 == "1":
            createClass.showInformation()
        elif askQuestion2 == "2":
            createClass.incSalary()
        else:
            print("Exiting...")
            break
        

    

    
