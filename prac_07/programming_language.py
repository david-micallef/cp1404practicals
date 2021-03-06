class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=True, year=''):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}".format(self=self)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
