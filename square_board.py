from typing import Tuple
Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    moves = [(side-1, x) for x in range(side-1, -1, -1)]
    moves.extend([(x, 0) for x in range(side-2, -1, -1)])
    moves.extend([(0, x) for x in range(1, side)])
    moves.extend([(x, side-1) for x in range(1, side-1)])
    move = (token + steps) % len(moves)
    return moves[move]

if __name__ == '__main__':
    print("Example:")
    print(square_board(4, 1, 4))
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)

    print("Coding complete? Click 'Check' to earn cool rewards!")
