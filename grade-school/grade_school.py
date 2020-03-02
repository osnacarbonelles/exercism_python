class School(object):
    def __init__(self):
        self.roll = {}

    def add_student(self, name, grade):
        if grade in self.roll:
            self.roll[grade] = sorted(self.roll[grade] + [name])
        else:
            self.roll[grade] = [name]

    def roster(self):
        return [y for x in sorted(list(self.roll)) for y in self.roll[x]]

    def grade(self, grade_number):
        return self.roll.get(grade_number, [])
