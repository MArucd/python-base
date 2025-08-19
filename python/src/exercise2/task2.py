
def chacha():
    num = int(input())
    num_norm = num
    num_rev = 0
    while num > 0:
        num_last = num % 10
        num_rev = num_rev * 10 + num_last
        num = num // 10
    if num_norm == num_rev:
        print("True")
    else:
        print("False")


chacha()
