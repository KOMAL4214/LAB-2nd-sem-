class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __add__(self,other):
        combined_salary= self.salary + other.salary
        return f"Combined salary of {self.name} and {other.name} is {combined_salary}"
        
    def __sub__(self,other):
        salary_difference= self.salary - other.salary
        return f" salary difference of {self.name} and {other.name} is {salary_difference}"
    
    def __str__(self):
        return f"employee name:{self.name}, employee salary:{self.salary}"
emp1=Employee("pavan",1000000)
emp2=Employee("alice",200000)

print(emp1+emp2)
print(emp1-emp2)
