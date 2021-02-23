class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
    def __str__(self):
        for row in self.my_list:
            for z in row:
                print(f"{z:4}", end="")
            print()
        return ''
    def __str__(self):
        return '\n'.join(map(str, self.my_list))
    def __add__(self, other):
        for z in range(len(self.my_list)):
            for z_2 in range(len(other.my_list[z])):
                self.my_list[z][z_2] = self.my_list[z][z_2] + other.my_list[z][z_2]
        return Matrix.__str__(self)
m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))