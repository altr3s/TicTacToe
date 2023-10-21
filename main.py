def matrix_is_full(matrix: list) -> bool:
    if '-' in matrix[0] or '-' in matrix[1] or '-' in matrix[2]:
        return False
    return True


def valid_win(matrix: list) -> bool:
    if matrix[0][0] == matrix[0][1] == matrix[0][2] != '-' or \
    matrix[1][0] == matrix[1][1] == matrix[1][2] != '-' or \
    matrix[2][0] == matrix[2][1] == matrix[2][2] != '-' or \
    matrix[0][0] == matrix[1][0] == matrix[2][0] != '-' or \
    matrix[0][1] == matrix[1][1] == matrix[2][1] != '-' or \
    matrix[0][2] == matrix[1][2] == matrix[2][2] != '-' or \
    matrix[0][0] == matrix[1][1] == matrix[2][2] != '-' or \
    matrix[0][2] == matrix[1][1] == matrix[2][0] != '-':
        return True


def tic_tac_toe(matrix: list, player: int):
    print('\n'.join('\t'.join(map(str, row)) for row in matrix))
    if matrix_is_full(matrix):
        print('Draw!')
        return False
    move = list(map(int, input().split()))
    if matrix[move[0] - 1][move[1] - 1] != "-":
        print("Place is occupied. Please take another.")
        tic_tac_toe(matrix, player)
    else:
        matrix[move[0] - 1][move[1] - 1] = "X" if player == 1 else "O"
    if valid_win(matrix):
        print(f'Player {player} win! Game is over!')
        return False
    return tic_tac_toe(matrix, 1 if player == 2 else 2)


matrix = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
if __name__ == '__main__':
    print('Game is Start! Choose your move.')
    tic_tac_toe(matrix, 1)
