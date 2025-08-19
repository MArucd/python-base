row_N, col_M = map(int, input().split())

A = []
for i in range(row_N):
    A.append(list(map(int, input().split())))

i = 0
j = 0
total_sum = A[i][j] 
while i < row_N - 1 or j < col_M - 1:
    if j < col_M - 1 and (i == row_N - 1 or A[i][j + 1] >= A[i + 1][j]):
        j += 1
    else:
        i += 1

    total_sum += A[i][j]

print(total_sum)
