# Dictionary of the plants used in this exercise:
plant = {
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass",
    "V": "Violets"
}

  class Garden(object):
    # initializing students in __init__() solves the arguments error.
    def __init__(self, diagram, students="Bob Alice Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()):
        self.students = sorted(students)
        self.diagram = diagram
    def plants(self, name):
        diagram = self.diagram.split("\n")
        # ps is plants diagram of the student:
        ps = ""
        # i is index of student name in students:
        i = self.students.index(name)
        ps += diagram[0][i*2:i*2+2]
        ps += diagram[1][i*2:i*2+2]
        # plants is the final result:
        plants = ""
        for p in ps:
            plants += plant[p] + " "
        return plants.split()
