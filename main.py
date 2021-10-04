import Jacobi
import Input
import Menu


# print(x)
matrix = Menu.menu(Menu.input_matrix)
print("Your matrix")
for i in matrix:
    print(i)
n = Input.number("Input accuracy: ")
x, steps = Jacobi.jacobi(matrix, n)
length = int(len((str(n).split('.')[-1])))
if x is not None:
    print("Jacobi result:", [round(float(i), length) for i in x])
    print("Steps:")
    for i in steps:
        print([round(float(s), length) for s in i])
else:
    print("Speed is to low, please change coefficients!!")