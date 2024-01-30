import draw_map
import os
import sys
import math
import datetime

class maze_solver:
    maze = []
    n_bonus_point = 0
    bonus_point = []
    start = [-1, -1]
    end = [-1, -1]
    def read_map(self, file_name):
        f = open(file_name,'r')
        split = f.read().split('\n')
        if split == ['']:
            return
        self.n_bonus_point = int(split[0])
        for i in range(self.n_bonus_point):
            temp = split[i+1].split(' ')
            temp = [int(x) for x in temp]
            self.bonus_point.append(temp)
        
        for i in range(self.n_bonus_point + 1, len(split)):
            self.maze.append(list(split[i]))
        
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'S':
                    self.start = [i, j]
                    self.maze[i][j] = ' '
                    break
            if self.start != [-1, -1]:
                break
        
        for i in range(len(self.maze)):
            if self.maze[i][0] == ' ':
                self.end = [i, 0]
                break
            if self.maze[i][len(self.maze[i]) - 1] == ' ':
                self.end = [i, len(self.maze[i]) - 1]
                break
        
        for i in range(len(self.maze[0])):
            if self.maze[0][i] == ' ':
                self.end = [0, i]
                break
            if self.maze[len(self.maze[0]) - 1][i] == ' ':
                self.end = [len(self.maze[0]) - 1, i]
                break
        f.close()
    
    def __str__(self) -> str:
        return str(self.maze)
    
    def bfs_solve(self):
        if self.n_bonus_point == 0:
            queue = []
            queue.append(self.start)
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while queue:
                current = queue.pop(0)
                if current == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0] + i, current[1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        queue.append(new)
                        visited.append(new)
                        parent[str(new)] = current
            if current != self.end:
                return []
            path = []
            while current != self.start:
                path.append(current)
                current = parent[str(current)]
            path.append(self.start)
            return path[::-1]
        return []

    def dfs_solve(self):
        if self.n_bonus_point == 0:
            stack = []
            stack.append(self.start)
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while stack:
                current = stack.pop()
                if current == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0] + i, current[1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        stack.append(new)
                        visited.append(new)
                        parent[str(new)] = current
            if current != self.end:
                return []
            path = []
            while current != self.start:
                path.append(current)
                current = parent[str(current)]
            path.append(self.start)
            return path[::-1]
        return []
    
    def ucs_solve(self):
        if self.n_bonus_point == 0:
            queue = []
            queue.append([self.start, 0])
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while queue:
                current = queue.pop(0)
                if current[0] == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0][0] + i, current[0][1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        queue.append([new, current[1] + 1])
                        visited.append(new)
                        parent[str(new)] = current
                queue.sort(key = lambda x: x[1])
            if current[0] != self.end:
                return []
            path = []
            while current[0] != self.start:
                path.append(current[0])
                current = parent[str(current[0])]
            path.append(self.start)
            return path[::-1]
        return []
    
    def greedy_solve_manhattan(self):
        if self.n_bonus_point == 0:
            queue = []
            queue.append([self.start, 0])
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while queue:
                current = queue.pop(0)
                if current[0] == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0][0] + i, current[0][1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        queue.append([new, abs(new[0] - self.end[0]) + abs(new[1] - self.end[1])])
                        visited.append(new)
                        parent[str(new)] = current
                queue.sort(key = lambda x: x[1])
            if current[0] != self.end:
                return []
            path = []
            while current[0] != self.start:
                path.append(current[0])
                current = parent[str(current[0])]
            path.append(self.start)
            return path[::-1]
        return []

    def greedy_solve_euclid(self):
        if self.n_bonus_point == 0:
            queue = []
            queue.append([self.start, 0])
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while queue:
                current = queue.pop(0)
                if current[0] == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0][0] + i, current[0][1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        queue.append([new, math.sqrt((new[0] - self.end[0]) ** 2 + (new[1] - self.end[1]) ** 2)])
                        visited.append(new)
                        parent[str(new)] = current
                queue.sort(key = lambda x: x[1])
            if current[0] != self.end:
                return []
            path = []
            while current[0] != self.start:
                path.append(current[0])
                current = parent[str(current[0])]
            path.append(self.start)
            return path[::-1]
        return []
    
    def greedy_solve(self, heuristic: str):
        if heuristic == 'manhattan':
            return self.greedy_solve_manhattan()
        elif heuristic == 'euclid':
            return self.greedy_solve_euclid()
        else:
            return []
        
    def Astar_solve_manhattan(self):
        if self.n_bonus_point == 0:
            queue = []
            queue.append([self.start, 0])
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while queue:
                current = queue.pop(0)
                if current[0] == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0][0] + i, current[0][1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        queue.append([new, abs(new[0] - self.end[0]) + abs(new[1] - self.end[1])])
                        visited.append(new)
                        parent[str(new)] = current
                queue.sort(key = lambda x: x[1])
            if current[0] != self.end:
                return []
            path = []
            while current[0] != self.start:
                path.append(current[0])
                current = parent[str(current[0])]
            path.append(self.start)
            return path[::-1]
        return []  
    
    def Astar_solve_euclid(self):
        if self.n_bonus_point == 0:
            queue = []
            queue.append([self.start, 0])
            visited = []
            visited.append(self.start)
            parent = {}
            parent[str(self.start)] = None
            while queue:
                current = queue.pop(0)
                if current[0] == self.end:
                    break
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (i != 0 and j != 0):
                            continue
                        new = [current[0][0] + i, current[0][1] + j]
                        if new[0] < 0 or new[1] < 0 or new[0] >= len(self.maze) or new[1] >= len(self.maze[0]) or self.maze[new[0]][new[1]] == 'x' or new in visited:
                            continue
                        queue.append([new, math.sqrt((new[0] - self.end[0]) ** 2 + (new[1] - self.end[1]) ** 2)])
                        visited.append(new)
                        parent[str(new)] = current
                queue.sort(key = lambda x: x[1])
            if current[0] != self.end:
                return []
            path = []
            while current[0] != self.start:
                path.append(current[0])
                current = parent[str(current[0])]
            path.append(self.start)
            return path[::-1]
        return []
    
    def Astar_solve(self, heuristic: str):
        if heuristic == 'manhattan':
            return self.Astar_solve_manhattan()
        elif heuristic == 'euclid':
            return self.Astar_solve_euclid()
        else:
            return []
    
    def reset(self):
        self.n_bonus_point = 0
        self.bonus_point = []
        self.start = [-1, -1]
        self.end = [-1, -1]
        self.maze = []
        
    def write_path_to_file(self, path, filedirectory):
        with open(filedirectory, 'w') as f:
            f.write(str(len(path)) + '\n')
            for i in path:
                f.write(str(i[0]) + ' ' + str(i[1]) + '\n')
        f.close()
        
def main(algorithm: str = '', heuristic: str = ''):
    files = os.listdir('./input/level_1')
    maze = maze_solver()
    if algorithm == 'bfs':
        for file in files:
            print('Start solving ' + file + 'by BFS')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/bfs', 'bfs')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/bfs/bfs.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
    elif algorithm == 'dfs':
        for file in files:
            print('Start solving ' + file + 'by DFS')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/dfs', 'dfs')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/dfs/dfs.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
    elif algorithm == 'ucs':
        for file in files:
            print('Start solving ' + file + 'by UCS')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/ucs', 'ucs')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/ucs/ucs.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
    elif algorithm == 'greedy':
        for file in files:
            print('Start solving ' + file + 'by Greedy with ' + heuristic + ' heuristic')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/gbfs', 'gbfs_heuristic_' + '1' if heuristic=='manhattan' else '2')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/gbfs/gbf_heuristic_' + '1' if heuristic=='manhattan' else '2' + '.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
    elif algorithm == 'astar':
        for file in files:
            print('Start solving ' + file + 'by A* with ' + heuristic + ' heuristic')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/astar', 'astar_heuristic_' + '1' if heuristic=='manhattan' else '2')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/astar/astar_heuristic_' + '1' if heuristic=='manhattan' else '2' + '.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
    else:
        for file in files:
            # bfs
            print('Start solving ' + file + 'by BFS')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/bfs', 'bfs')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/bfs/bfs.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
            # dfs
            print('Start solving ' + file + 'by DFS')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/dfs', 'dfs')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/dfs/dfs.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
            # ucs
            print('Start solving ' + file + 'by UCS')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/ucs', 'ucs')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/ucs/ucs.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            path = []
            # greedy
            print('Start solving ' + file + 'by Greedy with manhattan heuristic')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/gbfs', 'gbfs_heuristic_1')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/gbfs/gbfs_heuristic_1.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
            print('Start solving ' + file + 'by Greedy with euclid heuristic')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/gbfs', 'gbfs_heuristic_2')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/gbfs/gbfs_heuristic_2.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
            # Astar
            print('Start solving ' + file + 'by A* with manhattan heuristic')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/astar', 'astar_heuristic_1')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/astar/astar_heuristic_1.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []
            print('Start solving ' + file + 'by A* with euclid heuristic')
            maze.read_map('input/level_1/' + file)
            start = datetime.datetime.now()            
            path = maze.bfs_solve()
            end = datetime.datetime.now()
            draw_map.draw_maze('input/level_1/' + file ,path, 'output/level_1/' + file + '/astar', 'astar_heuristic_2')
            maze.write_path_to_file(path, 'output/level_1/' + file.split('.')[0] + '/astar/astar_heuristic_2.txt')
            print('Solved ' + file + ' in ' + str(end - start))
            maze.reset()
            path = []        
    
if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Too many arguments")
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()