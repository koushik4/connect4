import pygame

pygame.init()
pygame.mixer.init()


board = [[0 for i in range(6)]for j in range(6)]
window = pygame.display.set_mode((700,600))
pygame.display.set_caption("Connect Four")
run = True
start= 127
end = 100
size = 75
player = 0
row = [5 for i in range(6)]
radius = size//2-5
padding = 5
RED = (255.0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
turn = True
def if_win(player):
    window.fill((0,0,0))
    font = pygame.font.Font("freesansbold.ttf",64)
    if player==0:
        text = font.render("Player"+str(player+1)+" Won",True, (255,0,0))
    if player==1:
        text = font.render("Player"+str(player+1)+" Won",True, (255,255,0))
    window.blit(text,(150,200))
def if_draw():
    window.fill((0, 0, 0))
    font = pygame.font.Font("freesansbold.ttf", 64)
    text = font.render("Draw", True, (255, 255, 255))
    window.blit(text, (300, 200))
def check_draw():
    for i in range(6):
        for j in range(6):
            if board[i][j]==0:
                return False
    return True
def check_win():
    for x in range(6):
        for y in range(6):
            if check_dia_left(x,y)!=0:return check_dia_left(x,y)
            if check_dia_right(x,y)!=0:return check_dia_right(x,y)
            if check_horizontal(x,y)!=0:return check_horizontal(x,y)
            if check_vertical(x,y)!=0:return check_vertical(x,y)
    return 0
def check_horizontal(x,y):
    if y>2 or board[x][y]==0:return 0
    val = board[x][y]
    count = 0
    for i in range(4):
        if board[x][y+i]==val:count +=1
        else: break
    if count==4:return val
    return 0
def check_vertical(x,y):
    if x>2 or board[x][y]==0:return 0
    val = board[x][y]
    count = 0
    for i in range(4):
        if board[x+i][y]==val:count +=1
        else: break
    if count==4:return val
    return 0
def check_dia_right(x,y):
    if board[x][y]==0:return 0
    val = board[x][y]
    count = 0
    for i in range(4):
        if x+i>5 or y+i>5:return 0
        if board[x+i][y+i]==val:count +=1
        else: break
    if count==4:return val
    return 0
def check_dia_left(x,y):
    if board[x][y] == 0: return 0
    if x<4 or board[x][y]==0 or y>2:return 0
    val = board[x][y]
    count = 0
    for i in range(4):
        if x-i<0 or y+i>5:return False
        if board[x-i][y-i]==val:count +=1
        else: break
    if count==4:return val
    return 0
def draw_board():
    window.fill((0,0,0))
    for i in range(6):
        for j in range(6):
            x = i * size + start
            y = j * size + end
            c_x = x + size // 2
            c_y = y + size // 2
            color = ()
            if board[i][j] == 0:
                color = WHITE
            elif board[i][j] == 1:
                color = (255,0,0)
            elif board[i][j] == 2:
                color = (255,255,0)
            pygame.draw.rect(window,(0,0,255),(x,y,size,size),0)
            pygame.draw.circle(window,color,(c_x,c_y),radius,0)

def get_col(x,y):
    (x1,y1) = ((x-start)//size,(y-end)//size)
    if x1<0: x1 = 0
    if x1>5: x1 = 5
    return (x1)
def game(player,red):
    music = pygame.mixer.music.load("1.ogg")
    pygame.mixer.music.play(-1)
    global run,turn
    while run:
        (x, y) = pygame.mouse.get_pos()
        col = get_col(x, y)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run=False
            if events.type == pygame.MOUSEBUTTONDOWN and turn:
                if row[col]>=0:
                    board[col][row[col]] = player+1
                    row[col] -= 1
                    red.send(str(col).encode())
                    turn = False
        x = check_win()
        if x!=0:
            if_win(x-1)
        elif check_draw():
            if_draw()
        else:
            draw_board()
            Y = end - size//2
            X = col*size + start + radius + 5
            if player%2==0:
                pygame.draw.circle(window, (255, 0, 0), (X, Y), radius, 0)
            else:
                pygame.draw.circle(window, (255, 255, 0), (X, Y), radius, 0)
        pygame.display.update()