import math

num = input()
if num.isdigit() and int(num) > 0:
    num = int(num)
    for count in range(num):
        kolvo = count + 1
        row = []
        for nomer in range(kolvo):
            nomer_fac = math.factorial(nomer)
            znam = nomer_fac * math.factorial(count - nomer)
            nom_w = math.factorial(count) // znam  
            row.append(str(nom_w)) 
        print(' '.join(row)) 
else:
    print('Natural number was expected')
