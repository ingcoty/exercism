class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David",
                                          "Eve", "Fred", "Ginny", "Harriet",
                                          "Ileana", "Joseph", "Kincaid", "Larry"]):

        students.sort()
        self.students = students
        self.plants_class = {"R": "Radishes",
                             "C": "Clover", "G": "Grass", "V": "Violets"}
        self.owner = []
        rows = diagram.split()

        for row in rows:
            self.owner.append(([row[i:i+2] for i in range(0, len(row), 2)]))

    def plants(self, student):
        print(self.students)
        index = self.students.index(student)
        plants_str = ''
        for dat in self.owner:
            plants_str += (dat[index])

        plant_list = []
        for letter in plants_str:
            plant_list.append(self.plants_class[letter])

        return(plant_list)