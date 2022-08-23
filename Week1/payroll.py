class Employee():
    def __init__(self, empId, fname, lname, hrPay):
        self.empId = int(empId)
        self.fname = fname
        self.lname = lname
        self.hrPay = float(hrPay)
    
    def pay(self, hours):
        if hours <= 40:
            calculatePay = float(hours * self.hrPay)
            format_float_regular = "{:.2f}".format(calculatePay)
            return format_float_regular
        elif hours > 40:
            overTime = hours - 40 # How many hours of overtime
            overTimeCalculation = overTime * (1.5 * self.hrPay) # Overtime hourly rate times amount of overtime hours
            calculateOverTimePay = float((40 * self.hrPay) + (overTimeCalculation))
            format_float_over = "{:.2f}".format(calculateOverTimePay)
            return format_float_over


    def getFirstName(self):
        return self.fname
    
    def getLastName(self):
        return self.lname
    
    def getEmpId(self):
        return self.empId
    
    def getHrPay(self):
        return self.hrPay

    def setHourlyPay(self, hrPay):
        if hrPay <= 0:
            return
        self.hrPay = hrPay

emp = Employee(input("Please enter the Employee's ID: "),\
    input("Please enter the Employee's First Name: "),\
    input("Please enter the Employee's Last Name: "),\
    input("Please enter the Employee's Hourly Pay Rate: "))

hours_worked = float(input(f"How many hours did {emp.getFirstName()} work this week? "))
print(f"{emp.getFirstName()} {emp.getLastName()}'s paycheck amount is ${emp.pay(hours_worked)}")