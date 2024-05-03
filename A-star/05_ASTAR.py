# UPDATING CODE MAY CHANGE THIS IS ON HOLD

import heapq

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def is_valid_move(board, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 1:
        return False
    return True

def astar(board, start, end):
    rows, cols = len(board), len(board[0])
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (0, start, [start]))

    while open_list:
        _, current, path = heapq.heappop(open_list)
        if current == end:
            return path
        
        closed_set.add(current)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = current[0] + dr, current[1] + dc
            if is_valid_move(board, new_row, new_col) and (new_row, new_col) not in closed_set:
                new_path = path + [(new_row, new_col)]
                g = len(new_path)  # Cost from start node to current node
                h = manhattan_distance((new_row, new_col), end)
                f = g + h
                heapq.heappush(open_list, (f, (new_row, new_col), new_path))
                closed_set.add((new_row, new_col))

    return None

board = [
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]
start_index = (0, 0)
end_index = (2, 3)

path = astar(board, start_index, end_index)
if path:
    print("Path found:", path)
else:
    print("No path found")
