class Shape:
    def __init__(self, shape):
        self.curr_pos = 0
        if shape == 'L':
            self.name = 'L'
            self.num = 1
            self.color = 'orange'
            self.pos = [[4,1], [4,0], [5,0], [6,0]]
            self.rot = {0: [[-2,0], [-1,-1], [0,0], [1,1]], 1:[[0,-2], [1,-1], [0,0], [-1,1]] , 2: [[2,0], [1,1], [0,0], [-1,-1]] , 3: [[0,2], [-1,1], [0,0], [1,-1]]}
            self.next = [[187,235], [187,209], [187,183], [213,183]]
            
        elif shape == 'J':
            self.name = 'J'
            self.num = 2
            self.color = 'blue'
            self.pos = [[4,0], [5,0], [6,0], [6,1]]
            self.rot = {0: [[-1,-1], [0,0], [1,1], [0,2]], 1: [[1,-1], [0,0], [-1,1], [-2,0]] , 2: [[1,1], [0,0], [-1,-1], [0,-2]] , 3: [[-1,1], [0,0], [1,-1], [2,0]]}
            self.next = [[213,235], [213,209], [213,183], [187,183]]
            
        elif shape == 'I':
            self.name = 'I'
            self.num = 3
            self.color = 'cyan'
            self.pos = [[3,0], [4,0], [5,0], [6,0]]
            self.rot = {0:[[-2,-1], [-1,0], [0,1], [1,2]] , 1:[[1,-2], [0,-1], [-1,0], [-2,1]] , 2:[[2,1], [1,0], [0,-1], [-1,-2]] , 3: [[-1,2], [0,1], [1,0], [2,-1]] }
            self.next = [[199,248], [199,222], [199,196], [199,170]]
            
        elif shape == 'S':
            self.name = 'S'
            self.num = 4
            self.color = 'red'
            self.pos = [[4,1], [5,1], [5,0], [6,0]]
            self.rot = {0:[[-1,-1], [0,0], [1,-1], [2,0]] , 1:[[1,-1], [0,0], [1,1], [0,2]] , 2:[[1,1], [0,0], [-1,1], [-2,0]] , 3:[[-1,1], [0,0], [-1,-1], [0,-2]] }
            self.next = [[173,196], [199, 222], [225,222], [199, 196]]
            
        elif shape == 'Z':
            self.name = 'Z'
            self.num = 5
            self.color = 'green'
            self.pos = [[4,0], [5,0], [5,1], [6,1]]
            self.rot = {0:[[0,-2], [1,-1], [0,0], [1,1]] , 1: [[2,0], [1,1], [0,0], [-1,1]], 2:[[0,2], [-1,1], [0,0], [-1,-1]] , 3:[[-2,0], [-1,-1], [0,0], [1,-1]] }
            self.next = [[173,222], [199, 222], [225,196], [199, 196]]
            
        elif shape == 'T':
            self.name = 'T'
            self.num = 6
            self.color = 'dark orchid'
            self.pos = [[4,0], [5,0], [5,1], [6,0]]
            self.rot = {0:[[-1,-1], [0,0], [-1,1], [1,1]] , 1: [[1,-1], [0,0], [-1,-1], [-1,1]] , 2: [[1, 1], [0,0], [1,-1], [-1,-1]] , 3: [[-1,1], [0,0], [1,1], [1,-1]]}
            self.next = [[173,222], [199, 222], [225,222], [199, 196]]
            
        elif shape == 'O':
            self.name = 'O'
            self.num = 7
            self.color = 'yellow'
            self.pos = [[4,0], [5,0], [5,1], [4,1]]
            self.next = [[187, 222], [213,222],[187,196],[213,196]]
            