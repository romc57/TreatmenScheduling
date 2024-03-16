class Person:

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.available_days = None

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.f_name + ' ' + self.l_name
