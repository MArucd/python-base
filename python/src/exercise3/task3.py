def read_matrix(filename):
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.strip().split())) for line in f]
    # print(matrix)
    return matrix

def get_neighbors(r, c, n):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            yield nr, nc

def bfs(start_r, start_c, matrix, visited):
    from collections import deque
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True
    shape_coords = []
    while queue:
        r, c = queue.popleft()
        shape_coords.append((r,c))
        for nr, nc in get_neighbors(r,c,len(matrix)):
            if not visited[nr][nc] and matrix[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr,nc))
    return shape_coords

def is_square(coords):
    flag = True
    rows = [r for r,c in coords]
    cols = [c for r,c in coords]
    min_r,max_r = min(rows), max(rows)
    min_c,max_c = min(cols), max(cols)
    height = max_r - min_r + 1
    width = max_c - min_c + 1
    if height != width:
        flag = False
    for r in range(min_r,max_r+1):
        for c in range(min_c,max_c+1):
            if (r,c) not in coords:
                flag = False
    return flag

def main():
    filename = 'input.txt'
    matrix = read_matrix(filename)
    n = len(matrix)
    visited = [[False]*n for _ in range(n)]
    squares_count = 0
    circles_count = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 1 and not visited[r][c]:
                shape_coords = bfs(r,c,matrix,visited)
                if len(shape_coords) > 1:
                    if is_square(shape_coords):
                        squares_count += 1
                    else:
                        circles_count += 1
    print(squares_count, circles_count)

if __name__ == "__main__":
    main()
