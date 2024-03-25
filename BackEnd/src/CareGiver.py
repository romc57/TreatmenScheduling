from Person import Person


class CareGiver(Person):

    def __init__(self, f_name, l_name, available_time):
        Person.__init__(self, f_name, l_name, available_time)


