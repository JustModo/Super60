class Address:
    
    def __init__(self,street:str,city:str,zip:int) -> None:
        self.street = street
        self.city = city
        self.zip = zip
    
    def getDetails(self) -> None:
        print(f"Address:\nStreet:{self.street}\nCity:{self.city}\nZipcode:{self.zip}")

class Employee:

    # def __init__(self,name:str,emp_id:int,address:Address) -> None:
    #     self.name = name
    #     self.emp_id = emp_id
    #     self.address = address
    def __init__(self,address:Address):
        self.name = ""
        self.emp_id = 0
        self.address = ""
        self.role : str
        self.bs : int
        self.hra : int

    def getDetails(self) -> None:
        print(f"Name:{self.name}")
        print(f"Employee ID:{self.emp_id}")
        print(f"Role: {self.role}")
        print(f"Basic Salary: {self.bs}")
        print(f"HRA: {self.hra}")
        self.address.getDetails()

class EmployeeReport:
    def __init__(self) -> None:
        self.day:int
        self.month:int
        self.year:int
    
    def set_report_date(self):
        self.day = int(input("Day:"))
        self.month = int(input("Month:"))
        self.year = int(input("Year:"))

    
    
def store_data(emp:Employee) -> None:
    emp.name = str(input("Enter Name: "))
    emp.emp_id = int(input("Enter Name: "))
    emp.address = Address(input("Enter Street: "),input("Enter City: "),int(input(ZipCode: )))
    emp.bs = int(input("Enter Basic Salary: "))
    emp.role = input("Enter role of the Employee: ")
    emp.hra = int(input("Enter the HRA: "))

if __name__=="__main__":
    emp = []
    n = int(input("Enter the number of employees:"))
    for i in range(0,n):
        store_data(emp[i])
    for i in range(0,n):
        
        


    