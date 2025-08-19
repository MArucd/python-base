import sys

def read_initial_params():
    first_line = sys.stdin.readline().strip()
    if not first_line:
        print("Некорректный ввод")
        sys.exit(1)
    parts = first_line.split()
    if len(parts) != 2:
        print("Некорректный ввод")
        sys.exit(1)
    try:
        N = int(parts[0])
        total_time = int(parts[1])
        if N <= 0 or total_time <= 0:
            print("Некорректный ввод")
            sys.exit(1)
        return N, total_time
    except ValueError:
        print("Некорректный ввод")
        sys.exit(1)

def read_devices(N):
    devices = []
    for _ in range(N):
        line = sys.stdin.readline().strip()
        if not line:
            print("Некорректный ввод")
            sys.exit(1)
        parts = line.split()
        if len(parts) != 3:
            print("Некорректный ввод")
            sys.exit(1)
        try:
            year = int(parts[0])
            cost = int(parts[1])
            time_work = int(parts[2])
            if year <= 0 or cost <= 0 or time_work <= 0:
                print("Некорректный ввод")
                sys.exit(1)
            devices.append((year, cost, time_work))
        except ValueError:
            print("Некорректный ввод")
            sys.exit(1)
    return devices

def find_min_cost(devices, total_time):
    min_cost = None
    N = len(devices)
    
    for i in range(N):
        for j in range(i + 1, N):
            year_i, cost_i, time_i = devices[i]
            year_j, cost_j, time_j = devices[j]
            if year_i == year_j and (time_i + time_j) == total_time:
                total_cost = cost_i + cost_j
                if (min_cost is None) or (total_cost < min_cost):
                    min_cost = total_cost
    return min_cost

def main():
    N, total_time = read_initial_params()
    devices = read_devices(N)
    
    min_cost = find_min_cost(devices, total_time)
    
    if min_cost is not None:
        print(min_cost)
    else:
        print("Решения нет")

if __name__ == "__main__":
    main()