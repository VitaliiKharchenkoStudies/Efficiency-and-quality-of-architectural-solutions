class UserType:
    ENGINEER = 1
    MANAGER = 2

class User:
    def __init__(self, name, age, user_type, phone, phone_code):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone = phone
        self.phone_code = phone_code

    def print_details(self):
        user_type_str = {"User type": "Engineer" if self.user_type == UserType.ENGINEER else "Manager",
                         "Name": self.name,
                         "Age": self.age,
                         "Phone": self.phone_code + self.phone
                         }
        print(user_type_str)

user = User("John", 25, UserType.ENGINEER, "9379992", "050")
user.print_details()
