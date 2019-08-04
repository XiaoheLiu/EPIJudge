from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    i = j = n_dir = 0
    result = []
    M = len(square_matrix)

    # Improvement 1: change while to for loop
    # while i < m and j < m and square_matrix[i][j] != 0:
    for _ in range(M*M):
        result.append(square_matrix[i][j])
        square_matrix[i][j] = 0
        next_i, next_j = i + directions[n_dir][0], j + directions[n_dir][1]
        if (next_i >= M) or (next_j >= M) or (square_matrix[next_i][next_j] == 0):
            n_dir = (n_dir + 1) % 4
            # Improvement 2: change next_i/j only if changing direction
            next_i, next_j = i + directions[n_dir][0], j + directions[n_dir][1]
        # i, j = i + directions[n_dir][0], j + directions[n_dir][1]
        i, j = next_i, next_j

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
