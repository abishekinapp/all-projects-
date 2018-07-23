class Employee:
    def set_Firstname(self,First):
        self.Firstname = First

    def set_Lastname(self,Last):
        self.Lastname = Last

    def set_salary(self,Salary):
        self.Sal= Salary

    def get_Email(self,First,Last):
        self.email = First + "." + Last + "@inapp.com"
        return self.email

obj = Employee()
First=input("enter the first name")
obj.set_Firstname(First)

Last=input("enter the last name")
obj.set_Lastname(Last)

salary=input("enter the salary")
obj.set_salary(salary)

Email_id = obj.get_Email(First,Last)
print("Email ID generated :" , Email_id)