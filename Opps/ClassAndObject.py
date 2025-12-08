class User:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def get_Details(self):
        print(f"Name: {self.name}, Age: {self.age}, Role: {self.role}")

    def change_role(self, role):
        self.role = role



if __name__ == "__main__":
    user1 = User("jitendra", 20, "Tester")
    user1.get_Details()

    user2 = User("Ajay", 21, "Manual Tester")
    user2.get_Details()

    user3 = User("jitendra", 20, "Automation Tester")
    user3.get_Details()

    user1.change_role("Analyst")
    user1.get_Details()
