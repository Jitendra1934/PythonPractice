class Post:
    def __init__(self, message, name):
        self.message = message
        self.name =name

    def get_details(self):
        print(f"Post : {self.message}, {self.name}")
