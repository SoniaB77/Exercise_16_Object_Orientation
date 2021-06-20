class Person:

    def __init__(self, title, first_name, surname, birthdate, gender):
        self._title = title
        self._first_name = first_name
        self._surname = surname
        self._birthdate = birthdate
        self._gender = gender.lower()

    def __str__(self):
        return "Name: " + self._surname + "\nGender: " + self._gender




#We can also customize the __str__ method itself by overriding it.

# class SalaryNotInRangeError(Exception):
#     """Exception raised for errors in the input salary.
#
#     Attributes:
#         salary -- input salary which caused the error
#         message -- explanation of the error
#     """
#
#     def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.salary} -> {self.message}'
#
#
# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)