def inputik():
    num = input()
    return num

def kolvo_posle(data):
    row = []
    rev = data[::-1]
    for count in rev:
        if count == '.':
            break
        row.append(count)
    posle_tochki = ''.join(row)
    return len(posle_tochki)

def prov(data):
    index = data.find('.')
    if index == -1:
        flag = 0
    else:
        flag = 1
    return flag

def main(data):
    if data.endswith('.'):
        print('incorrect input, enter the number')
        return
    row = []
    for count in data:
        if count == '.':
            continue
        row.append(count)
    result = ''.join(row)
    if all(ch in '-1234567890' for ch in result):
        result = int(result)
        result *= 2
        if prov(data) == 1:
            result /= 10 ** kolvo_posle(data)
        print(f"{result:.3f}")
    else:
        print('incorrect input, enter the number')

data = inputik()
main(data)

