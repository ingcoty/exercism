class Matrix:
    def __init__(self, matrix_string):
        self.mat = []
        self.cols = len(matrix_string.split('\n'))
        self.rows = len(matrix_string.split('\n')[0].split())
        data = matrix_string.split()
        datanum = []

        for elm in data:
            datanum.append(int(elm))

        for col in range(self.cols):
            line = []
            for row in range(self.rows):
                line.append(datanum[0])
                datanum.pop(0)
            self.mat.append(line)

        print(self.mat)

    def row(self, index):
        return(self.mat[index-1])

    def column(self, index):
        column = []
        for item in self.mat:
            column.append(item[index-1])

        return(column)
