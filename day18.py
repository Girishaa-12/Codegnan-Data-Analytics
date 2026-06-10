#Toprint the common details of students,teaching staff,non-teaching staff,driver,cleaner and warden with the help of inheritance concept.
class Person:
    university_name = "RAGHU INSTITUTE OF TECHNOLOGY"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"University : {Person.university_name}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")


# Student Class
class Student(Person):
    def __init__(self, name, age, gender, roll_no, course):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print("\n--- Student Details ---")
        super().display()
        print(f"Roll No    : {self.roll_no}")
        print(f"Course     : {self.course}")


# Teaching Staff Class
class TeachingStaff(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def display(self):
        print("\n--- Teaching Staff Details ---")
        super().display()
        print(f"Subject    : {self.subject}")


# Non-Teaching Staff Class
class NonTeachingStaff(Person):
    def __init__(self, name, age, gender, department):
        super().__init__(name, age, gender)
        self.department = department

    def display(self):
        print("\n--- Non-Teaching Staff Details ---")
        super().display()
        print(f"Department : {self.department}")


# Driver Class
class Driver(Person):
    def __init__(self, name, age, gender, vehicle_no):
        super().__init__(name, age, gender)
        self.vehicle_no = vehicle_no

    def display(self):
        print("\n--- Driver Details ---")
        super().display()
        print(f"Vehicle No : {self.vehicle_no}")


# Cleaner Class
class Cleaner(Person):
    def __init__(self, name, age, gender, area):
        super().__init__(name, age, gender)
        self.area = area

    def display(self):
        print("\n--- Cleaner Details ---")
        super().display()
        print(f"Area       : {self.area}")


# Warden Class
class Warden(Person):
    def __init__(self, name, age, gender, hostel):
        super().__init__(name, age, gender)
        self.hostel = hostel

    def display(self):
        print("\n--- Warden Details ---")
        super().display()
        print(f"Hostel     : {self.hostel}")


# Creating Objects
s1 = Student("Girisha", 22, "Female", "223J1A44H6", "Data Science")
t1 = TeachingStaff("Haribabu", 40, "Male", "Web Development")
n1 = NonTeachingStaff("Suresh", 35, "Male", "Administration")
d1 = Driver("Ramesh", 45, "Male", "AP39AB7576")
c1 = Cleaner("Lakshmi", 30, "Female", "College Campus")
w1 = Warden("Aswini", 42, "Female", "Girls Hostel")

# Display Details
s1.display()
t1.display()
n1.display()
d1.display()
c1.display()
w1.display()
