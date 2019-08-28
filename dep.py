class Employee:
    def __init__(self, name):
        self.name = name
        self.title = ""
        self.start = ""

class Company:
    def __init__(self, name):
        self.name = name
        self.address = ""
        self.type = ""
        self.employees = list()

sherwin_williams = Company("Sherwin Williams")
general_electric = Company("General Electric")

joe = Employee("Joe")
danny = Employee("Danny")
curt = Employee("Curt")
drew = Employee("Drew")
adam = Employee("Adam")

sherwin_williams.employees.append(joe)
sherwin_williams.employees.append(danny)
general_electric.employees.append(curt)
general_electric.employees.append(drew)
general_electric.employees.append(adam)

print(f"{sherwin_williams.name}'s employees:")
for employee in sherwin_williams.employees:
    print(f"* {employee.name}")
print(f"{general_electric.name}'s employees:")
for employee in general_electric.employees:
    print(f"* {employee.name}")
