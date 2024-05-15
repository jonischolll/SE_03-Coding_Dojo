# Model
class NameModel:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

# View
class NameView:
    def display_name_prompt(self):
        return input("Enter your name: ")

    def display_greeting(self, name):
        print(f"Hello {name}!")

# Controller
class NameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        name = self.view.display_name_prompt()
        self.model.set_name(name)
        name = self.model.get_name()
        self.view.display_greeting(name)

# Configuration
class Config:
    def __init__(self):
        self.logger = Logger()

# Logger
class Logger:
    def log(self, message):
        print(message)

# Manual Dependency Injection
config = Config()
model = NameModel()
view = NameView()
controller = NameController(model, view)
controller.run()

