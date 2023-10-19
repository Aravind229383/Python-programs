class Employee:
    def __init__(self):
        self.name=" "
        self.empId=" "
        self.dept=" "
        self.salary=0
    def getEmpDetails(self):
        self.name=input("Enter the employee name: ")
        self.empId=input("Enter the employee id: ")
        self.dept=input("Enter the employee department: ")
        self.salary=int(input("Enter the salary of the employee: "))
    def showEmpDetails(self):
        print("Employee details")
        print("Name: ",self.name)
        print("EmpId: ",self.empId)
        print("Dept: ",self.dept)
        print("Salary: ",self.salary)
    def updtsalary(self):
        self.salary=int(input("Enter the new salary"))
        print("Updated salary: ",self.salary)
e1=Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtsalary()
