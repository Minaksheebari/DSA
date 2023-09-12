from collections import deque

def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def shortest_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])

    visited = [[False for _ in range(n)] for _ in range(m)]

    queue = deque([(i, 0) for i in range(m) if matrix[i][0] == 1])

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y = queue.popleft()

        if y == n - 1:
            return True  
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y, m, n) and not visited[new_x][new_y] and matrix[new_x][new_y] == 1:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

    return False  

matrix = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

if shortest_path(matrix):
    print("There is a safe path from the first column to the last column.")
else:
    print("There is no safe path from the first column to the last column.")
