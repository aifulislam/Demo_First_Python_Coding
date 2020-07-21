#Matrix-----------
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for row in matrix:
    for col in row:
        print(col)

matrix[0][0] = 10
matrix[0][1] = 11
matrix[0][2] = 12
print('Matrix[0][0] : ',matrix[0][0])
print('Matrix[0][1] : ',matrix[0][1])
print('Matrix[0][2] : ',matrix[0][2])
print('Matrix[1][0] : ',matrix[1][0])
print('Matrix[1][1] : ',matrix[1][1])
print('Matrix[1][2] : ',matrix[1][2])
print('Matrix[2][0] : ',matrix[2][0])
print('Matrix[2][1] : ',matrix[2][1])
print('Matrix[2][2] : ',matrix[2][2])

