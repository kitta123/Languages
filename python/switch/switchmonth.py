class PythonSwitchStatement:
    def switch(self, month):
        default = "Invalid month"
        return getattr(self, 'case_' + str(month), lambda: default)()

    def case_1(self):return "January"
    def case_2(self):return "February"
    def case_3(self):return "March"
    def case_4(self):return "April"
    def case_5(self):return "May"
    def case_6(self):return "June"
    def case_7(self):return "July"
    def case_8(self):return "August"
    def case_9(self):return "September"
    def case_10(self):return "October"
    def case_11(self):return "November"
    def case_12(self):return "December"

s = PythonSwitchStatement()
month = int(input("Enter the number between 1 to 12 :"))
print(s.switch(month))
