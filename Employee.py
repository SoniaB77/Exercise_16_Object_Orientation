from Person import Person


class Employee (Person):

    def __init__(self, title, first_name, surname, birthdate, gender, department, job_role, id_number):
        super().__init__(title, first_name, surname, birthdate, gender)
        self._department = department
        self._job_role = job_role
        self._id_number = id_number


will = Employee("mr", "will", "ferrell", "19/08/1876", "m", "IT", "IT Technician", "56891")

print(will.__str__())

print(will._department)
