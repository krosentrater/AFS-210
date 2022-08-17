# Tuple
Data1 = (7, False, "Apple", True, 7, 98.6)

# Set
Data2 = {'July', 4, 8, "Tango", 4.3, "Bingo"}

# List
Data3 = ["A", 7, -1, 3.14, True, 7]

# Dictionary
Data4 = {
    "name" : "Joe",
    "age" : 26,
    "active" : True,
    "hourly_wage" : 14.75
}



            ###?Data1###
print(len(Data1))
print(Data1[3])
print(Data1.count(7))


            ###?Data2###
removedItem = Data2.pop()
Data2.add("Alpha")
print(Data2)

            ###?Data3###
reversed = []
for i in Data3:
    reversed.insert(0, i)
print(reversed)
Data3[1] = "B"
Data3.pop()
print(Data3)

            ###?Data4###
Data4.update({ "active":"False" })
Data4.update({ "address":"123 West Main Street" })
hourlyWage = Data4.get("hourly_wage")
salary = format(hourlyWage * 40, ',.2f')
print(f"The weekly salary for Joe is: $",salary)
print(Data4)