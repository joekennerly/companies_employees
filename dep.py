class Employee:
    def __init__(self, name):
        self.name = name
        self.title = ""
        self.start = ""
    def __str__(self):
        return f'{self.name}'

class Company:
    def __init__(self, name):
        self.name = name
        self.address = ""
        self.type = ""
        self.employees = list()
    def __str__(self):
        new_emps = "\n".join([ f' *{emp.name} ' for emp in self.employees])
        return f'{self.name} has the following employees:\n{new_emps}'

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

print(sherwin_williams)
print(general_electric)
