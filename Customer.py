from Person import Person


class Customer(Person):

    def __init__(self, title, first_name, surname, birthdate, gender, address, telephone_number, email,
                 customer_reference):
        super().__init__(title, first_name, surname, birthdate, gender)
        self._address = address
        self._telephone_number = telephone_number
        self._customer_reference = customer_reference
        self._email = email

kristen = Customer("miss", "kristen", "wiig", "4/5/1970", "female", "67 comedy road, new york, 1005", "716-743-1871", "jellybean@gmail.com", "555432")

print(kristen.__str__())

print(kristen._email)