# -*- coding: utf-8 -*-

def x_and_o(grid, mark):
    X_vs_O = {'X':'O', 'O':'X'}

    def winner(grid, mark):
        WINNER_WAYS = ((0, 1, 2), (3, 4, 5),
                       (6, 7, 8), (0, 3, 6),
                       (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6)
                       )
        
        for row in WINNER_WAYS:
            line = grid[row[0]]+grid[row[1]]+grid[row[2]]
            if line.count('.') == 1:
                if line.count(mark) == 2 or line.count(X_vs_O[mark]) == 2:
                    return row[line.find('.')]
        return False
   
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    FIELD = {0:(0, 0), 1:(0, 1), 2:(0, 2),
             3:(1, 0), 4:(1, 1), 5:(1, 2),
             6:(2, 0), 7:(2, 1), 8:(2, 2)
             }
    grid = ''.join(grid)
    dot_cnt = grid.count('.')
    is_first_move = True if dot_cnt == 9 else False
    if is_first_move: return FIELD[4]
    is_second_move = True if dot_cnt == 8 else False
    is_center_free = True if grid[4] =='.' else False
    if is_second_move and is_center_free:
        return FIELD[4]
    elif is_second_move:
        for i in BEST_MOVES:
            if grid[i] == '.': return FIELD[i]

    cnt_my_mark = grid.count(mark)
    cnt_enemy_mark = grid.count(X_vs_O[mark])
    was_my_first_move = True if cnt_my_mark == cnt_enemy_mark else False
    legal_moves = [ i for i in range(9) if grid[i] =='.']
    if was_my_first_move:
        if dot_cnt == 7:
            for i in (0, 2, 8, 6):
                if grid[i] == '.': return FIELD[i]
        is_winner = winner(grid, mark)
        if is_winner is not False: return FIELD[is_winner]
        
        if dot_cnt == 5:
            lines = ((0, 1, 2), (6, 7, 8),
                     (0, 3, 6), (2, 5, 8))
            for x, y in ([0, 8], [2, 6]):
                if x in legal_moves and y in legal_moves:
                     for corner in (x,y):
                         for line in lines:
                             if corner in line:
                                 row = grid[line[0]]+grid[line[1]]+grid[line[2]]
                                 cnt_mark = row.count(mark)
                                 cnt_dot = row.count('.')
                                 if cnt_mark ==1 and cnt_dot ==2:
                                     return FIELD[corner]
        for move in BEST_MOVES:
            if move in legal_moves: return FIELD[move]
    else:
        is_winner = winner(grid, mark)
        if is_winner is not False: return FIELD[is_winner]
        if dot_cnt == 6 and grid[4] == mark:
            for i in (1, 3, 5, 7):
                if i in legal_moves: return FIELD[i]
        for move in BEST_MOVES:
            if move in legal_moves: return FIELD[move]

    
print(x_and_o(( "XO.", ".X.",  "..O"), "X"))
#print(winner("XO..X....", 'X'))
