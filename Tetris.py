import turtle
import random
import Shape
import functools

random.seed()
game = turtle.Screen()
blocks = turtle.Turtle()
ready = turtle.Turtle()
updates = turtle.Turtle()
updates.up()
updates.ht()
updates.speed(0)
shapes = ['L', 'J', 'I', 'S', 'Z', 'T', 'O']
board = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
         


def draw_grid():
    game.tracer(2,0)
    grid = turtle.Turtle()
    grid.ht()
    grid.speed(0)
    grid.shape('square')
    grid.up()
    grid.goto(-136, 271)
    grid.down()
    grid.goto(124, 271)
    grid.goto(124, -249)
    grid.goto(-136, -249)
    grid.goto(-136, 271)
    curr_sq = 271
    for i in range(19):
        curr_sq -= 26
        grid.goto(-136, curr_sq)
        grid.goto(124, curr_sq)
        grid.goto(-136, curr_sq)
    grid.up()
    grid.goto(-136,271)
    grid.down()
    curr_sq = -136
    for i in range(9):
        curr_sq += 26
        grid.goto(curr_sq, 271)
        grid.goto(curr_sq, -249)
        grid.goto(curr_sq, 271)
        
    grid.up()
    grid.goto(150, 271)
    grid.down()
    grid.begin_fill()
    grid.goto(249,271)
    grid.goto(249,146)
    grid.goto(150,146)
    grid.goto(150,271)
    grid.end_fill()
    grid.up()
    grid.goto(150,125)
    grid.write("Score:", font=("Arial", 10, "bold"))
    grid.goto(150,105)
    grid.write("Level:", font=("Arial", 10, "bold"))
    grid.goto(150,85)
    grid.write("Lines Left:", font=("Arial", 10, "bold"))
    
    

def find_coords():
    coords = []
    yVal = 258
    for i in range(20):
        xVal = -123
        row = []
        for j in range(10):
            row.append((xVal, yVal))
            xVal += 26
        coords.append(row)
        yVal -= 26
    return coords

def choose_block(last):
    tetro = random.randint(0,6)
    if shapes[tetro] == last:
        tetro = random.randint(0,6)
    return shapes[tetro]

def draw_shape(shape, coords):
    blocks.ht()
    blocks.speed(0)
    blocks.color(shape.color)
    blocks.up()
    blocks.shape('square')
    blocks.shapesize(1.2,1.2)

    
    for posi in shape.pos:
        curr_pos = coords[posi[1]][posi[0]]
        blocks.goto(curr_pos[0], curr_pos[1])
        blocks.stamp()
    game.update()
    
def is_loss(shape):
    for coord in shape.pos:
        if not(board[coord[1]][coord[0]] == 0):
            return True
    return False

def check_collision(shape):
    for coord in shape.pos:
        if coord[1] == 19 or (not(board[coord[1] + 1][coord[0]] == 0)):
            return True
    return False

def fall(shape,coords):
    if check_collision(shape):
        return
    else:
        for coord in shape.pos:
            coord[1] += 1
        blocks.clearstamps(-4)
        draw_shape(shape,coords)
        game.update()

def update_board(shape):
    for coord in shape.pos:
        board[coord[1]][coord[0]] = shape.num

def can_move(shape, key):
    for coord in shape.pos:
        if key == 'r':
            check = coord[0] == 9 or (not(board[coord[1]][coord[0] + 1] == 0))
        else:
            check = coord[0] == 0 or (not(board[coord[1]][coord[0] - 1] == 0))
            
        if check:
            return False
        
    return True

def go_right(shape,coords):
    if can_move(shape, 'r'):
        for coord in shape.pos:
            coord[0] += 1
        blocks.clearstamps(-4)
        draw_shape(shape,coords)
        game.update()
    else:
        return
        #do nothing

def go_left(shape,coords):
    if can_move(shape, 'l'):
        for coord in shape.pos:
            coord[0] -= 1
        blocks.clearstamps(-4)
        draw_shape(shape,coords)
        game.update()
    else:
        return
        #do nothing


def collisions(shape):
    offset = [0,0]
    for coord in shape.pos:
        if coord[0] < 0:
            offset = [1,0]
        if coord[0] > 9:
            offset = [-1,0]
    return offset

def undo_rot(shape, moves, offset, direc):
    if direc == 'cc':
        for row in range(4):
            shape.pos[row][0] += moves[row][0] - offset[0]
            shape.pos[row][1] += moves[row][1] - offset[1]
    else:
        for row in range(4):
            shape.pos[row][0] -= moves[row][0] - offset[0]
            shape.pos[row][1] -= moves[row][1] - offset[1]
        shape.curr_pos -= 1

def flip_clock(shape,coords):
    if shape.name == 'O':
        return
    
    shape.curr_pos += 1
    if shape.curr_pos == 4:
        shape.curr_pos = 0
        
    moves = shape.rot[shape.curr_pos]
    for row in range(4):
        shape.pos[row][0] += moves[row][0]
        shape.pos[row][1] += moves[row][1]

    extra = collisions(shape)
    if not(extra == [0,0]):
        for row in range(4):
            shape.pos[row][0] += extra[0]
            shape.pos[row][1] += extra[1]

    for row in range(4):
        if not(board[shape.pos[row][1]][shape.pos[row][0]] == 0):
                undo_rot(shape, moves, extra, 'cl')
                return
            
    blocks.clearstamps(-4)
    draw_shape(shape,coords)
    

def flip_count(shape,coords):
    
    if shape.name == 'O':
        return

    moves = shape.rot[shape.curr_pos]
    for row in range(4):
        shape.pos[row][0] -= moves[row][0]
        shape.pos[row][1] -= moves[row][1]
    
    extra = collisions(shape)
    if not(extra == [0,0]):
        for row in range(4):
            shape.pos[row][0] += extra[0]
            shape.pos[row][1] += extra[1]

    for row in range(4):
        if not(board[shape.pos[row][1]][shape.pos[row][0]] == 0):
                undo_rot(shape, moves, extra, 'cc')
                return

    shape.curr_pos -= 1
    if shape.curr_pos == -1:
        shape.curr_pos = 3
        
    blocks.clearstamps(-4)
    draw_shape(shape,coords)
    

def match_board(coords):
    colors = {1: "orange", 2:"blue", 3:"cyan", 4:"red", 5:"green", 6:"dark orchid", 7: "yellow"}
    blocks.clearstamps()
    blocks.ht()
    blocks.speed(0)
    blocks.up()
    blocks.shape('square')
    blocks.shapesize(1.2,1.2)
    for row in range(20):
       for col in range(10):
           if not(board[row][col] == 0):
                block_col = colors[board[row][col]]
                blocks.color(block_col)
                curr_pos = coords[row][col]
                blocks.goto(curr_pos[0], curr_pos[1])
                blocks.stamp()


def check_row(coords, score):
    scores = score[0]
    level = score[1]
    to_next = score[2]
    speed = score[3]


    count = 0
    lines = 0
    for i in range(20):
        if board[i].count(0) == 0:
            count += 1
            board.pop(i)
            board.insert(0,[0,0,0,0,0,0,0,0,0,0])

    if count == 0:
        return score
    
    if count == 1:
        lines = 40
        
    elif count == 2:
        lines = 100
        
    elif count == 3:
        lines = 300

    elif count == 4:
        lines = 1200

    to_add = lines * (level + 1)
    scores += to_add
    to_next -= count

    if to_next <= 0:
        level += 1
        to_next = 10 * (level + 1)
        mod = (5 * (level // 5) + 1)
        mod2 = level * ((level % 5)+ 1)

        if mod2 > 25:
            mod2 = 25

        if level >= 15:
            mod = 16
        
        speed -= mod * mod2

    
    
    match_board(coords)
    updates.clear()
    updates.goto(200, 125)
    updates.write(str(scores))
    updates.goto(200,105)
    updates.write(str(level))
    updates.goto(225, 85)
    updates.write(str(to_next)) 
    game.update()

    
    score = [scores, level, to_next, speed]
    return score


def draw_next(shape):
    ready.up()
    ready.ht()
    ready.shape('square')
    ready.color(shape.color)
    ready.shapesize(1.2,1.2)
    ready.clear()
    for coord in shape.next:
        ready.goto(coord[0],coord[1])
        ready.stamp()
                       
def speed_up(shape, coords):
    fall(shape,coords)
    fall(shape,coords)
    fall(shape,coords)


#Game Running



draw_grid()
coords = find_coords()
curr_shape = choose_block('I')
next_shape = Shape.Shape(curr_shape)
score = [0, 0, 10, 400]
updates.goto(200, 125)
updates.write(str(score[0]))
updates.goto(200,105)
updates.write(str(score[1]))
updates.goto(225, 85)
updates.write(str(score[2]))
while True:
    game.tracer(0,2)
    shape = next_shape
    curr_shape = choose_block(curr_shape)
    next_shape = Shape.Shape(curr_shape)
    
    draw_next(next_shape)
    
    if is_loss(shape):
        break
    draw_shape(shape, coords)
    game.update()
    fall_part = functools.partial(fall, shape, coords)
    right_part = functools.partial(go_right, shape, coords)
    left_part = functools.partial(go_left, shape, coords)
    clock_part = functools.partial(flip_clock, shape, coords)
    count_part = functools.partial(flip_count, shape, coords)
    speed_part = functools.partial(speed_up, shape, coords)
    while not(check_collision(shape)):
        game.onkeypress(right_part, 'Right')
        game.onkeypress(left_part, 'Left')
        game.onkeypress(speed_part, 'Down')
        game.onkeypress(clock_part, 'x')
        game.onkeypress(count_part, 'z')
        game.ontimer(fall_part(),score[3])

        game.listen()
    
    update_board(shape)
    score = check_row(coords, score)
    

game.clearscreen()
writer = turtle.Turtle()
writer.ht()
end = "Game Over\n You Lose\n Level: " + str(score[1]) + "\n Score: " + str(score[0])
writer.write(end, move=False, align= 'center', font =('Arial', 25, 'bold'))
   
