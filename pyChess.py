## Importing pygame
import pygame

## Initialise pygame and display
pygame.init()
w = 1000
h = 900
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("It's Chessing time.")
font = pygame.font.Font("blkchcry.ttf", 20)
medium_font = pygame.font.Font("blkchcry.ttf", 40)
big_font = pygame.font.Font("blkchcry.ttf", 50)
timer = pygame.time.Clock()
fps = 144

## Movements of chess pieces

## 0 - White's turn: 1 - White's turn piece selected: 2 - Black's turn: 3 - Black's turn piece selected 
turns = 0

## Move piece_select 
piece_select = 420

## Validity of piece movement
valid_moves = []


## Chess pieces location settings

## White
w_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
w_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

## Black
b_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
b_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

## Captured pieces
cap_w = []
cap_b = []

## Flags and validation check
winner = ''
game_over = False

## Image Loading to the pieces

## Black pieces
b_queen = pygame.image.load("assets/bq.png")
b_queen = pygame.transform.scale(b_queen, (80, 80))
b_queen_small = pygame.transform.scale(b_queen, (45, 45))
b_king = pygame.image.load("assets/bk.png")
b_king = pygame.transform.scale(b_king, (80, 80))
b_king_small = pygame.transform.scale(b_king, (45, 45))
b_rook = pygame.image.load("assets/br.png")
b_rook = pygame.transform.scale(b_rook, (80, 80))
b_rook_small = pygame.transform.scale(b_rook, (45, 45))
b_bishop = pygame.image.load("assets/bb.png")
b_bishop = pygame.transform.scale(b_bishop, (80, 80))
b_bishop_small = pygame.transform.scale(b_bishop, (45, 45))
b_knight = pygame.image.load("assets/bn.png")
b_knight = pygame.transform.scale(b_knight, (80, 80))
b_knight_small = pygame.transform.scale(b_knight, (45, 45))
b_pawn = pygame.image.load("assets/bp.png")
b_pawn = pygame.transform.scale(b_pawn, (65, 65))
b_pawn_small = pygame.transform.scale(b_pawn, (45, 45))

## White pieces
w_queen = pygame.image.load("assets/wq.png")
w_queen = pygame.transform.scale(w_queen, (80, 80))
w_queen_small = pygame.transform.scale(w_queen, (45, 45))
w_king = pygame.image.load("assets/wk.png")
w_king = pygame.transform.scale(w_king, (80, 80))
w_king_small = pygame.transform.scale(w_king, (45, 45))
w_rook = pygame.image.load("assets/wr.png")
w_rook = pygame.transform.scale(w_rook, (80, 80))
w_rook_small = pygame.transform.scale(w_rook, (45, 45))
w_bishop = pygame.image.load("assets/wb.png")
w_bishop = pygame.transform.scale(w_bishop, (80, 80))
w_bishop_small = pygame.transform.scale(w_bishop, (45, 45))
w_knight = pygame.image.load("assets/wn.png")
w_knight = pygame.transform.scale(w_knight, (80, 80))
w_knight_small = pygame.transform.scale(w_knight, (45, 45))
w_pawn = pygame.image.load("assets/wp.png")
w_pawn = pygame.transform.scale(w_pawn, (65, 65))
w_pawn_small = pygame.transform.scale(w_pawn, (45, 45))

## Drawing reference for pieces on board
w_images = [w_pawn, w_queen, w_king, w_knight, w_rook, w_bishop]
small_w_images = [w_pawn_small, w_queen_small, w_king_small, w_knight_small, w_rook_small, w_bishop_small]
b_images = [b_pawn, b_queen, b_king, b_knight, b_rook, b_bishop]
small_b_images = [b_pawn_small, b_queen_small, b_king_small, b_knight_small, b_rook_small, b_bishop_small]

## Index for the images
pieces_list = ["Pawn", "Queen", "King", "Knight", "Rook", "Bishop"]

## Drawing the chess board:
def draw_ui():

    ## Drawing chess board itself
    for a in range(int((8**2) * 0.5)):
        
        ## Drawing checkered pattern of chess board
        col = a % 4
        row = a // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "lightsteelblue", [600 - (col * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, "lightsteelblue", [700 - (col * 200), row * 100, 100, 100])
        
        ## Drawing thicker lines of chess board
        for b in range(9):
            pygame.draw.line(screen, "hotpink4", (0, 100 * b), (800, 100 * b), 3)
            pygame.draw.line(screen, "hotpink4", (100 * b, 0), (100 * b, 800), 3)
        
        ## Drawing the bottom UI and the Side of the table UI
        pygame.draw.rect(screen, "mediumorchid4", [0, 800, w, 100])
        pygame.draw.rect(screen, "gold", [0, 800, w, 100], 5)
        pygame.draw.rect(screen, "gold", [800, 0, 200, h], 5)

        ## Status texts
        status = ["White to move", "Click on a square to move the piece.", "Black to move", "Click on a square to move the piece."]
        screen.blit(big_font.render(status[turns], True, "black"), (20, 820))

        ## Resign button
        screen.blit(big_font.render("Resign", True, "black"), (825, 820))


## Drawing pieces onto the chess board
def draw_pieces():

    ## Finding and offsetting images for white
    for c in range(len(w_pieces)):
        index = pieces_list.index(w_pieces[c])
        if w_pieces[c] == "Pawn":
            screen.blit(w_pawn, (w_locations[c][0] * 100 + 17, w_locations[c][1] * 100 + 16))
        else:
            screen.blit(w_images[index], (w_locations[c][0] * 100 + 10, w_locations[c][1] * 100 + 10)) 
        if turns < 2:
            if piece_select == c:
                pygame.draw.rect(screen, "red", [w_locations[c][0] * 100 + 1, w_locations[c][1] * 100 + 1, 100, 100], 6)


    ## Finding and offsetting images for black
    for d in range(len(b_pieces)):
        index = pieces_list.index(b_pieces[d])
        if b_pieces[d] == "Pawn":
            screen.blit(b_pawn, (b_locations[d][0] * 100 + 17, b_locations[d][1] * 100 + 16))
        else:
            screen.blit(b_images[index], (b_locations[d][0] * 100 + 10, b_locations[d][1] * 100 + 10))
        if turns >= 2:
            if piece_select == d:
                pygame.draw.rect(screen, "red", [b_locations[d][0] * 100 + 1, b_locations[d][1] * 100 + 1, 100, 100], 6)

## Check and Mate
def draw_check():

    ## White King in check
    if turns < 2:
        if "King" in w_pieces:
            king_index = w_pieces.index("King")
            king_location = w_locations[king_index]
            for moves_list in b_options:
                if king_location in moves_list:
                    pygame.draw.rect(screen, 'dark red', [w_locations[king_index][0] * 100 + 1, w_locations[king_index][1] * 100 + 1, 100, 100], 5)
    
    ## Black King in check
    else:
        if "King" in b_pieces:
            king_index = b_pieces.index("King")
            king_location = b_locations[king_index]
            for moves_list in w_options:
                if king_location in moves_list:
                    pygame.draw.rect(screen, 'dark red', [b_locations[king_index][0] * 100 + 1, b_locations[king_index][1] * 100 + 1, 100, 100], 5)

## Checking the options of moves
def check_options(pieces, locate, turn):
    moves_list = []
    valid_moves_list = []
    
    ## Checking what piece to check for the specifics
    for e in range(len(pieces)):
        location = locate[e]
        piece = pieces[e]
        if piece == "Pawn":
            moves_list = check_pawn(location, turn)
        elif piece == "King":
            moves_list = check_king(location, turn)
        elif piece == "Rook":
            moves_list = check_rook(location, turn)
        elif piece == "Bishop":
            moves_list = check_bishop(location, turn)
        elif piece == "Knight":
            moves_list = check_knight(location, turn)
        elif piece == "Queen":
            moves_list = check_queen(location, turn)
        valid_moves_list.append(moves_list)
    return valid_moves_list

## INDIVIDUAL variety of moves by a piece checking

# Pawn
def check_pawn(pos, colour):
    pawn_moves_list = []

    ## For black pawn
    if colour == "b":

        ## Normal Pawn Move
        if (pos[0], pos[1] + 1) not in w_locations and (pos[0], pos[1] + 1) not in b_locations and pos[1] < 7:
            pawn_moves_list.append((pos[0], pos[1] + 1))

        ## First double pawn move
        if (pos[0], pos[1] + 2) not in w_locations and (pos[0], pos[1] + 2) not in b_locations and pos[1] == 1:
            pawn_moves_list.append((pos[0], pos[1] + 2))
        
        ## Attacking a piece
        if (pos[0] + 1, pos[1] + 1) in w_locations:
            pawn_moves_list.append((pos[0] + 1, pos[1] + 1))
        if (pos[0] - 1, pos[1] + 1) in w_locations:
            pawn_moves_list.append((pos[0] - 1, pos[1] + 1))

    ## For white pawn
    if colour == "w":

        ## Normal Pawn Move
        if (pos[0], pos[1] - 1) not in w_locations and (pos[0], pos[1] - 1) not in b_locations and pos[1] > 0:
            pawn_moves_list.append((pos[0], pos[1] - 1))

        ## First double pawn move
        if (pos[0], pos[1] - 2) not in w_locations and (pos[0], pos[1] - 2) not in b_locations and pos[1] == 6:
            pawn_moves_list.append((pos[0], pos[1] - 2))
        
        ## Attacking a piece
        if (pos[0] + 1, pos[1] - 1) in b_locations:
            pawn_moves_list.append((pos[0] + 1, pos[1] - 1))
        if (pos[0] - 1, pos[1] - 1) in b_locations:
            pawn_moves_list.append((pos[0] - 1, pos[1] - 1))
    return pawn_moves_list

# Queen
def check_queen(pos, colour):

    ## Queen diagonal moves
    queen_list_1 = check_bishop(pos, colour)
    
    ## Rook diagonal moves
    queen_list_2 = check_rook(pos, colour)

    ## Adding both moves sets together
    for j in range(len(queen_list_2)):
        queen_list_1.append(queen_list_2[j])
    return queen_list_1

# King
def check_king(pos, colour):
    king_moves_list = []

    ## Black king
    if colour == "b":
        good = b_locations
        bad = w_locations
    
    ## White king
    if colour == "w":
        good = w_locations
        bad = b_locations

    ## Only possible king directions and checking if he can go there
    possible = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (pos[0] + possible[i][0], pos[1] + possible[i][1])
        if target not in good and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            king_moves_list.append(target)
    return king_moves_list


# Rook
def check_rook(pos, colour):
    rook_moves_list = []

    ## Black rook
    if colour == "b":
        good = b_locations
        bad = w_locations
    
    ## White rook
    if colour == "w":
        good = w_locations
        bad = b_locations
    
    ## Checking all 4 direction of rook's movement
    for g in range(4):
        path = True
        chain = 1

        ## Downwards motion
        if g == 0:
            x = 0
            y = 1
        
        ## Upwards motion
        elif g == 1:
            x = 0
            y = -1
        
        ## Eastwards motion
        elif g == 2:
            x = 1
            y = 0
        
        ## Westwards motion
        elif g == 3:
            x = -1
            y = 0

        ## Checking for collision in a certain direction
        while path:
                if (pos[0] + (chain * x), pos[1] + (chain * y)) not in good and 0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                    rook_moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                    if (pos[0] + (chain * x), pos[1] + (chain * y)) in bad:
                        path = False
                    chain += 1
                else:
                    path = False
    return rook_moves_list

# Knight 
def check_knight(pos, colour):
    knight_moves_list = []

     ## Black Knight
    if colour == "b":
        good = b_locations
        bad = w_locations
    
    ## White Knight
    if colour == "w":
        good = w_locations
        bad = b_locations

    ## All possible knight direction moves
    possible = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    
    ## Checking each square if its out of range or have a friendly piece blocking it
    for h in range(8):
        target = (pos[0] + possible[h][0], pos[1] + possible[h][1])
        if target not in good and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            knight_moves_list.append(target)
    return knight_moves_list

# Bishop
def check_bishop(pos, colour):
    bishop_moves_list = []
    
    ## Black Bishop
    if colour == "b":
        good = b_locations
        bad = w_locations
    
    ## White Bishop
    if colour == "w":
        good = w_locations
        bad = b_locations

    ## Checking all 4 direction of Bishop's movement
    for i in range(4):
        path = True
        chain = 1

        ## Bottom Right motion
        if i == 0:
            x = 1
            y = 1
        
        ## Top Right motion
        elif i == 1:
            x = 1
            y = -1
        
        ## Top Left motion
        elif i == 2:
            x = -1
            y = -1
        
        ## Bottom Left motion
        elif i == 3:
            x = -1
            y = 1

        ## Checking for collision in a certain direction
        while path:
                if (pos[0] + (chain * x), pos[1] + (chain * y)) not in good and 0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                    bishop_moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                    if (pos[0] + (chain * x), pos[1] + (chain * y)) in bad:
                        path = False
                    chain += 1
                else:
                    path = False
    return bishop_moves_list

## Drawing captured pieces for table feel
def draw_captured():

    ## Captured black pieces
    for k in range(len(cap_w)):
        cap_piece = cap_w[k]
        index = pieces_list.index(cap_piece)
        screen.blit(small_b_images[index], (825, 5 + (50 * k)))
    
    ## Captured black pieces
    for l in range(len(cap_b)):
        cap_piece = cap_b[l]
        index = pieces_list.index(cap_piece)
        screen.blit(small_w_images[index], (925, 5 + (50 * l)))

## Check valid move for specific piece selected
def check_valid():
    if turns < 2:
        option = w_options
    else:
        option = b_options
    if 0 <= piece_select < len(option):
        valid_options = option[piece_select]
    else:
        valid_options = []
    return valid_options

## Drawing the valid moves
def draw_valid(moves):
    for f in range(len(moves)):
        pygame.draw.circle(screen, "red", (moves[f][0] * 100 + 50, moves[f][1] * 100 + 50), 10)

## Ending the game
def draw_ending():
    pygame.draw.rect(screen, "Black", [200, 200, 400, 70])
    if winner == "w":
        screen.blit(font.render(f"Congratulations! White won the game!", True, "White"), (210, 210))
    if winner == "b":
        screen.blit(font.render(f"Congratulations! Black won the game!", True, "White"), (210, 210))
    screen.blit(font.render(f"Press the Spacebar to play again.", True, "White"), (210, 240))

## While the game is active
b_options = check_options(b_pieces, b_locations, "b")
w_options = check_options(w_pieces, w_locations, "w")
run = True
while run:
    
    ## Main functions
    pygame.display.flip()
    timer.tick(fps)
    screen.fill("mediumpurple1")
    draw_ui()
    draw_check()
    draw_pieces()
    draw_captured()
    if piece_select != 420:
        valid_moves = check_valid()
        draw_valid(valid_moves)


    ## Handling events
    for event in pygame.event.get():

        ## Ending the game
        if event.type == pygame.QUIT:
            run = False

        ## Detecting mouse click location
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x = event.pos[0] // 100
            y = event.pos[1] // 100
            click_coord = (x, y)

            ## White piece moving
            if turns <= 1:

                ## Clicking resign button
                if click_coord == (8, 8) or click_coord == (9, 8): 
                    winner = "b"

                ## Clicking on white piece
                if click_coord in w_locations:
                    piece_select = w_locations.index(click_coord)
                    if turns == 0:
                        turns = 1

                # White takes
                if click_coord in valid_moves and piece_select != 420:
                    w_locations[piece_select] = click_coord
                    if click_coord in b_locations:
                        b_piece = b_locations.index(click_coord)
                        cap_w.append(b_pieces[b_piece])
                        if b_pieces[b_piece] == "King":
                            winner = "w"
                        b_pieces.pop(b_piece)
                        b_locations.pop(b_piece)
                    b_options = check_options(b_pieces, b_locations, "b")
                    w_options = check_options(w_pieces, w_locations, "w")
                    turns = 2
                    piece_select = 420
                    valid_moves = []

            ## Black piece moving
            if turns > 1:

                ## Clicking resign button
                if click_coord == (8, 8) or click_coord == (9, 8):
                    winner = "w"

                ## Clicking on black piece
                if click_coord in b_locations:
                    piece_select = b_locations.index(click_coord)
                    if turns == 2:
                        turns = 3

                # Black takes
                if click_coord in valid_moves and piece_select != 420:
                    b_locations[piece_select] = click_coord
                    if click_coord in w_locations:
                        w_piece = w_locations.index(click_coord)
                        cap_b.append(w_pieces[w_piece])
                        if w_pieces[w_piece] == "King":
                            winner = "b"
                        w_pieces.pop(w_piece)
                        w_locations.pop(w_piece)
                    b_options = check_options(b_pieces, b_locations, "b")
                    w_options = check_options(w_pieces, w_locations, "w")
                    turns = 0
                    piece_select = 420
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:

                ## Resetting game results
                game_over = False
                winner = ''
                
                ## Resetting chess pieces location

                ## White
                w_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
                w_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

                ## Black
                b_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
                b_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                cap_b = []
                cap_w = []
                turns = 0
                piece_select = 100
                valid_moves = []
                b_options = check_options(b_pieces, b_locations, "b")
                w_options = check_options(w_pieces, w_locations, "w")


    if winner != "":
        game_over = True
        draw_ending()

## Quitting the game
pygame.quit()