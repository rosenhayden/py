#data and functions asscociated with class are called attributes and methods
#methods are functions asscociated with classes
# Attributes are data associated


#instance variables contain data that is unique to each instance of a class
class Employee:
    #this initalizes the constructor
    def __init__(self, first, last, pay):
        #sets self(our instace) to the values passed 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
    #method to get full name
    def fullname(self):
        return "{} {}".format(self.first, self.last)


#classes are the blueprint that get used by instances of that class

#employee1 will be passed in as self!
employee1 = Employee("bob", "dingus", 100)

print(employee1.email)
#need () for methods
#self is getting passed to fullname
print(employee1.fullname())
#whats happening in the background is this:
#calling employee class method fullname and passing instance of employee1
print(Employee.fullname(employee1))
