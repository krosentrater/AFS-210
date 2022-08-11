class Employee():
    def __init__(self, empId, fname, lname, hrPay):
        self.empId = empId
        self.fname = fname
        self.lname = lname
        self.hrPay = float(hrPay)
    
    def pay(self, hours):
        if hours <= 40:
            calculatePay = hours * self.hrPay
            print(f"{self.fname} {self.lname}'s paycheck amount is ${format(calculatePay,',.2f')}")
        elif hours > 40:
            overTime = hours - 40 # How many hours of overtime
            overTimeCalculation = overTime * (1.5 * self.hrPay) # Overtime hourly rate times amount of overtime hours
            calculateOverTimePay = (40 * self.hrPay) + (overTimeCalculation)
            print(f"{self.fname} {self.lname}'s paycheck amount is ${format(calculateOverTimePay,',.2f')}")

    def getInfo(self):
        return self.fname, self.lname, self.empId, self.hrPay

emp = Employee(input("Please enter the Employee's ID: "),\
    input("Please enter the Employee's First Name: "),\
    input("Please enter the Employee's Last Name: "),\
    input("Please enter the Employee's Hourly Pay Rate: "))

hours_worked = int(input(f"How many hours did {emp.fname} work this week? "))
emp.pay(hours_worked)