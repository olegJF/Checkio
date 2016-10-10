# -*- coding: utf-8 -*-

def is_move (pos, move, matrix):
    x, y = pos[0] + move[0], pos[1] + move[1]
    if matrix[x][y] == 0: return True
    return False

def delete_move (pos, road, matrix):
    MOVE_BACK = {"S": (-1, 0), "N": (1, 0), "W": (0, 1), "E": (0, -1)}
    move = MOVE_BACK[road[-1]]
    x, y = pos[0], pos[1]
    matrix[x][y] = 1
    road = road[:-1]
    pos = pos[0] + move[0], pos[1] + move[1]
    return pos, road, matrix

def checkio(maze_map):
    MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
    PERPENDICULAR = {'S': ('E', 'W'), 'N' : ('W', 'E'), 'W' : ('S', 'N'), 'E' : ('N', 'S')}
    pos = (1, 1)
    goal = (10, 10)
    road = ''
    visited = []

    while pos != goal: #for i in range(15): #
        if not road:
            for direction in list(MOVE.keys()):
                if is_move (pos, MOVE[direction], maze_map):
                    move = MOVE[direction]
                    pos = pos[0] + move[0], pos[1] + move[1]
                    road = road + direction
                    visited.append(pos)
                    break
        else:
            possible_direction = road[-1]
            if is_move (pos, MOVE[possible_direction], maze_map):
                move = MOVE[possible_direction]
                pos = pos[0] + move[0], pos[1] + move[1]
                if pos not in visited:
                    road = road + possible_direction
                    visited.append(pos)
                else:
                    maze_map[pos[0]][pos[1]] = 1
                    pos = pos[0] - move[0], pos[1] - move[1]
            else:
                left, right = PERPENDICULAR[possible_direction]
                if (not is_move (pos, MOVE[left], maze_map)) and (not is_move (pos, MOVE[right], maze_map)):
                    #print('del')
                    pos, road, maze_map = delete_move (pos, road, maze_map)
                else:
                    if is_move (pos, MOVE[left], maze_map):
                        possible_direction = left
                    else:
                        possible_direction = right
                
                    move = MOVE[possible_direction]
                    pos = pos[0] + move[0], pos[1] + move[1]
                    if pos not in visited:
                        road = road + possible_direction
                        visited.append(pos)
                    else:
                        maze_map[pos[0]][pos[1]] = 1
                        pos = pos[0] - move[0], pos[1] - move[1]   
        #print(pos)            
                
                
    return road
print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))

if __name__ == '__main__':
    #This code using only for self-checking and not necessary for auto-testing
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        #copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False
    
