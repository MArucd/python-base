N, x = map(float, input().split())
N = int(N)

num_row = []

count = 0

while count < N + 1:
    num = float(input())
    if count < N:
        num_row.append(num)
    count += 1

lennum = len(num_row)

for i in range(lennum):
    num_row[i] = num_row[i] * (N - i) * (x ** ((N - 1) - i))


print(f"{sum(num_row):.3f}")

