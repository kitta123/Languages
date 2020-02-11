def January():
    return "January"
def February():
    return "February"
def March():
    return "March"
def April():
    return "April"
def May():
    return "May"
def June():
    return "June"
def July():
    return "July"
def August():
    return "August"
def September():
    return "September"
def October():
    return "October"
def November():
    return "November"
def December():
    return "December"
def default():
    return "Please Enter the Valid Number"

switcher = {
    1: January,
    2: February,
    3: March,
    4: April,
    5: May,
    6: June,
    7: July,
	8: August,
	9: September,
	10: October,
	11: November,
	12: December
    }

def switch(monthOfYear):
    return switcher.get(monthOfYear, default)()

month = int(input("Enter the number between 1 to 12 : "))
print(switch(month))

