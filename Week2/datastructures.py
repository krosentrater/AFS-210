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

#!Count number of items
print(len(Data1))

#!Find value of 4th item stored in data set
print(Data1[3])

#!Count the number of times 7 appears
print(Data1.count(7))




            ###?Data2###

#!Remove random element
removedItem = Data2.pop()
print(Data2)
print('Removed item: ', removedItem)

#!Print the data set
print(Data2)
Data2.add("Alpha")
print(Data2)

#!Print the data set (not sure if you meant the type or just print it!)
print(type(Data2))
print(Data2)

            ###?Data3###

#!Print data set in reverse order
reversed = []
for i in Data3:
    reversed.insert(0, i)
print(reversed)

#!Change 2nd value to "B"
Data3[1] = "B"
print(Data3)

#!Remove last item and print
print(Data3)
Data3.pop()
print(Data3)

            ###?Data4###

#! Change "active" to False
Data4.update({ "active":"False" })
print(Data4)

#! Add "address" with a value of "123 West Main Street"
Data4.update({ "address":"123 West Main Street" })
print(Data4)

#! Print the weekly salary for Joe if he worked a full 40 hour week
hourlyWage = Data4.get("hourly_wage")
salary = format(hourlyWage * 40, ',.2f')
print(f"The weekly salary for Joe is: $",salary)

#! Print the data set (not sure if you meant the type of just print the data)
print(Data4)
print(type(Data4))