class up_Str:
    def __init__(self):
        self.x=""
    def get_string(self):
        self.x=input()
    def print_string(self):
        print(self.x.upper())
x=up_Str()
x.get_string()
x.print_string()