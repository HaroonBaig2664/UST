class Employee:
    def __init__(self,name,empid): #(double underscores has to come)
        self.name = name
        self.empid = empid

    def greet(self):
        print('Thanks for joining Ust Global Company {} !!'.format(self.name))

#Create an employee Object
emp1 = Employee("Haroon Baig",191569)

print('Name: ', emp1.name)
print('Employee ID : ',emp1.empid)
emp1.greet()

# Create another Employee Object
emp2 = Employee('Ruksar Mehdi', 191568)

print('Name:',emp2.name)
print('Employee ID : ', emp2.empid)
emp2.greet()

emp2.country = 'India'  #instance variable can be created manually.
print(emp2.country)

#Modify object Properties
emp1.name = 'Haroon Baig'
print(emp1.name)

#delete object Properties
del(emp1.empid)
# This will give an Error - Attribute Error
emp1.empid

#delete an object
del(emp1)
#this will give an Error - Name error
emp1
