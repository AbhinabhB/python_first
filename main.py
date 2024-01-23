def create_matrix(int_val, m, n):
    return [[int_val] * m for _ in range(n)]


matrix1 = create_matrix(0, 2, 2)
matrix2 = create_matrix(0, 2, 2)

print("Enter elements for matrix1")
for i in range(2):
    for j in range(2):
        matrix1[i][j] = int(input(f"Enter element for row {i} column {j}: "))

print("Enter elements for matrix2")
for i in range(2):
    for j in range(2):
        matrix2[i][j] = int(input(f"Enter element for row {i} column {j}: "))