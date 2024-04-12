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
    
## Castling validity
castling_moves = [] 


## Chess pieces pos settings

## White
w_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
w_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
w_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

## Black
b_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
b_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
b_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

## Captured pieces
cap_w = []
cap_b = []

## Flags and validation check
winner = ''
game_over = False

## Image Loading to the pieces

## Black pieces
b_queen = pygame.image.load("assets/bqueen.png")
b_queen = pygame.transform.scale(b_queen, (85, 85))
b_queen_small = pygame.transform.scale(b_queen, (50, 50))
b_king = pygame.image.load("assets/bking.png")
b_king = pygame.transform.scale(b_king, (85, 85))
b_king_small = pygame.transform.scale(b_king, (50, 50))
b_rook = pygame.image.load("assets/brook.png")
b_rook = pygame.transform.scale(b_rook, (85, 85))
b_rook_small = pygame.transform.scale(b_rook, (50, 50))
b_bishop = pygame.image.load("assets/bbishop.png")
b_bishop = pygame.transform.scale(b_bishop, (85, 85))
b_bishop_small = pygame.transform.scale(b_bishop, (50, 50))
b_knight = pygame.image.load("assets/bknight.png")
b_knight = pygame.transform.scale(b_knight, (85, 85))
b_knight_small = pygame.transform.scale(b_knight, (50, 50))
b_pawn = pygame.image.load("assets/bpawn.png")
b_pawn = pygame.transform.scale(b_pawn, (85, 85))
b_pawn_small = pygame.transform.scale(b_pawn, (50, 50))

## White pieces
w_queen = pygame.image.load("assets/wqueen.png")
w_queen = pygame.transform.scale(w_queen, (85, 85))
w_queen_small = pygame.transform.scale(w_queen, (50, 50))
w_king = pygame.image.load("assets/wking.png")
w_king = pygame.transform.scale(w_king, (85, 85))
w_king_small = pygame.transform.scale(w_king, (50, 50))
w_rook = pygame.image.load("assets/wrook.png")
w_rook = pygame.transform.scale(w_rook, (85, 85))
w_rook_small = pygame.transform.scale(w_rook, (50, 50))
w_bishop = pygame.image.load("assets/wbishop.png")
w_bishop = pygame.transform.scale(w_bishop, (85, 85))
w_bishop_small = pygame.transform.scale(w_bishop, (50, 50))
w_knight = pygame.image.load("assets/wknight.png")
w_knight = pygame.transform.scale(w_knight, (85, 85))
w_knight_small = pygame.transform.scale(w_knight, (50, 50))
w_pawn = pygame.image.load("assets/wpawn.png")
w_pawn = pygame.transform.scale(w_pawn, (85, 85))
w_pawn_small = pygame.transform.scale(w_pawn, (50, 50))

## Drawing reference for pieces on board
w_images = [w_pawn, w_queen, w_king, w_knight, w_rook, w_bishop]
small_w_images = [w_pawn_small, w_queen_small, w_king_small, w_knight_small, w_rook_small, w_bishop_small]
b_images = [b_pawn, b_queen, b_king, b_knight, b_rook, b_bishop]
small_b_images = [b_pawn_small, b_queen_small, b_king_small, b_knight_small, b_rook_small, b_bishop_small]

## Promoting pieces
white_promote = False
black_promote = False
w_promo = ["Queen", "Knight", "Rook", "Bishop"]
b_promo = ["Queen", "Knight", "Rook", "Bishop"]

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
    global check
    check = False

    ## White King in check
    if turns < 2:
        if "King" in w_pieces:
            king_index = w_pieces.index("King")
            king_pos = w_locations[king_index]
            for moves_list in b_options:
                if king_pos in moves_list:
                    check = True
                    pygame.draw.rect(screen, 'dark red', [w_locations[king_index][0] * 100 + 1, w_locations[king_index][1] * 100 + 1, 100, 100], 5)
    
    ## Black King in check
    else:
        if "King" in b_pieces:
            king_index = b_pieces.index("King")
            king_pos = b_locations[king_index]
            for moves_list in w_options:
                if king_pos in moves_list:
                    check = True
                    pygame.draw.rect(screen, 'dark red', [b_locations[king_index][0] * 100 + 1, b_locations[king_index][1] * 100 + 1, 100, 100], 5)

## Checking the options of moves
def check_options(pieces, locate, turn):
    global castling_moves
    moves_list = []
    valid_moves_list = []
    castling_moves = []
    
    ## Checking what piece to check for the specifics
    for e in range(len(pieces)):
        pos = locate[e]
        piece = pieces[e]
        if piece == "Pawn":
            moves_list = check_pawn(pos, turn)
        elif piece == "King":
            moves_list, castling_moves = check_king(pos, turn)
        elif piece == "Rook":
            moves_list = check_rook(pos, turn)
        elif piece == "Bishop":
            moves_list = check_bishop(pos, turn)
        elif piece == "Knight":
            moves_list = check_knight(pos, turn)
        elif piece == "Queen":
            moves_list = check_queen(pos, turn)
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

## En Passant
def check_ep(firststep, secondstep):
    if turns <= 1:
        index = w_locations.index(firststep)
        ep_coords = (secondstep[0], secondstep[1] - 1)
        piece = w_pieces[index]
    else:
        index = b_locations.index(firststep)
        ep_coords = (secondstep[0], secondstep[1] + 1)
        piece = b_pieces[index]
    if piece == 'pawn' and abs(firststep[1] - secondstep[1]) > 1:
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords

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
    castling_moves = check_castling()

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
    return  king_moves_list, castling_moves

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

## Castling

## Check for possiblity
def check_castling():
    check = False
    castle_moves = []
    rook_indexes = []
    rook_locations = []
    king_index = 0
    king_pos = (0, 0)
    if turns > 1:
        for w in range(len(w_pieces)):
            if w_pieces[w] == "Rook":
                rook_indexes.append(w_moved[w])
                rook_locations.append(w_locations[w])
            if w_pieces[w] == "King":
                king_index = w
                king_pos = w_locations[w]
        if not w_moved[king_index] and False in rook_indexes and not check:
            for x in range(len(rook_indexes)):
                castle = True
                if rook_locations[x][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                    (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for y in range(len(empty_squares)):
                    if empty_squares[y] in w_locations or empty_squares[y] in b_locations or empty_squares[y] in b_options or rook_indexes[x]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    else:
        for z in range(len(b_pieces)):
            if b_pieces[z] == "Rook":
                rook_indexes.append(b_moved[z])
                rook_locations.append(b_locations[z])
            if b_pieces[z] == "King":
                king_index = z
                king_pos = b_locations[z]
        if not b_moved[king_index] and False in rook_indexes and not check:
            for aa in range(len(rook_indexes)):
                castle = True
                if rook_locations[aa][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                    (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for ab in range(len(empty_squares)):
                    if empty_squares[ab] in w_locations or empty_squares[ab] in b_locations or empty_squares[ab] in w_options or rook_indexes[ab]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    return castle_moves

## Drawing the moves
def draw_castling(moves):
    colour = "red"
    for p in range(len(moves)):
        pygame.draw.circle(screen, colour, (moves[p][0][0] * 100 + 50, moves[p][0][1] * 100 + 70), 8)
        screen.blit(font.render("king", True, "black"), (moves[p][0][0] * 100 + 30, moves[p][0][1] * 100 + 70))
        pygame.draw.circle(screen, colour, (moves[p][1][0] * 100 + 50, moves[p][1][1] * 100 + 70), 8)
        screen.blit(font.render("rook", True, "black"),
                    (moves[p][1][0] * 100 + 30, moves[p][1][1] * 100 + 70))
        pygame.draw.line(screen, colour, (moves[p][0][0] * 100 + 50, moves[p][0][1] * 100 + 70),
                        (moves[p][1][0] * 100 + 50, moves[p][1][1] * 100 + 70), 2)

## Promoting

## Checking for possiblity
def check_promotion():
    pawn_indexes = []
    w_promotion = False
    b_promotion = False
    promote_index = 100
    for s in range(len(w_pieces)):
        if w_pieces[s] == 'pawn':
            pawn_indexes.append(s)
    for t in range(len(pawn_indexes)):
        if w_locations[pawn_indexes[t]][1] == 7:
            w_promotion = True
            promote_index = pawn_indexes[t]
    pawn_indexes = []
    for u in range(len(b_pieces)):
        if b_pieces[u] == 'pawn':
            pawn_indexes.append(u)
    for v in range(len(pawn_indexes)):
        if b_locations[pawn_indexes[v]][1] == 0:
            b_promotion = True
            promote_index = pawn_indexes[v]
    return w_promotion, b_promotion, promote_index

## Drawing the moves
def draw_promotion():
    pygame.draw.rect(screen, 'dark gray', [800, 0, 200, 420])
    if white_promote:
        colour = 'white'
        for i in range(len(w_promo)):
            piece = w_promo[i]
            index = pieces_list.index(piece)
            screen.blit(w_images[index], (860, 5 + 100 * i))
    elif black_promote:
        colour = 'black'
        for i in range(len(b_promo)):
            piece = b_promo[i]
            index = pieces_list.index(piece)
            screen.blit(b_images[index], (860, 5 + 100 * i))
    pygame.draw.rect(screen, colour, [800, 0, 200, 420], 8)


## Checking the piece it is promoting to
def check_promo_select():
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100
    y_pos = mouse_pos[1] // 100
    if white_promote and left_click and x_pos > 7 and y_pos < 4:
        w_pieces[promo_index] = b_promo[y_pos]
    elif black_promote and left_click and x_pos > 7 and y_pos < 4:
        b_pieces[promo_index] = b_promo[y_pos]


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
    check = draw_check()
    draw_pieces()
    draw_captured()
    if not game_over:
        white_promote, black_promote, promo_index = check_promotion()
        if white_promote or black_promote:
            draw_promotion()
            check_promo_select()
    if piece_select != 420:
        valid_moves = check_valid()
        draw_valid(valid_moves)
        if selected_piece == "King":
            draw_castling(castling_moves)


    ## Handling events
    for event in pygame.event.get():

        ## Ending the game
        if event.type == pygame.QUIT:
            run = False

        ## Detecting mouse click pos
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
                    selected_piece = w_pieces[piece_select]
                    if turns == 0:
                        turns = 1

                # White takes
                if click_coord in valid_moves and piece_select != 420:
                    w_locations[piece_select] = click_coord
                    w_ep = check_ep(w_locations[piece_select], click_coord)
                    if click_coord in b_locations:
                        b_piece = b_locations.index(click_coord)
                        cap_w.append(b_pieces[b_piece])
                        if b_pieces[b_piece] == "King":
                            winner = "w"
                        b_pieces.pop(b_piece)
                        b_locations.pop(b_piece)
                        b_moved.pop(b_piece)
                    b_options = check_options(b_pieces, b_locations, "b")
                    w_options = check_options(w_pieces, w_locations, "w")
                    turns = 2
                    piece_select = 420
                    valid_moves = []
                elif piece_select != 420 and selected_piece == "King":
                    for r in range(len(castling_moves)):
                        if click_coord == castling_moves[r][0]:
                            w_locations[piece_select] = click_coord
                            w_moved[piece_select] = True
                            if click_coord == (1, 7):
                                rook_coords = (0, 7)
                            else:
                                rook_coords = (7, 7)
                            rook_index = w_locations.index(rook_coords)
                            w_locations[rook_index] = castling_moves[r][1]
                            black_options = check_options(b_options, b_locations, "b")
                            white_options = check_options(w_pieces, w_locations, "w")
                            turns = 0
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
                    selected_piece = b_pieces[piece_select]
                    if turns == 2:
                        turns = 3

                # Black takes
                if click_coord in valid_moves and piece_select != 420:
                    b_locations[piece_select] = click_coord
                    b_ep = check_ep(b_locations[piece_select], click_coord)
                    if click_coord in w_locations:
                        w_piece = w_locations.index(click_coord)
                        cap_b.append(w_pieces[w_piece])
                        if w_pieces[w_piece] == "King":
                            winner = "b"
                        w_pieces.pop(w_piece)
                        w_locations.pop(w_piece)
                        w_moved.pop(w_piece)
                    b_options = check_options(b_pieces, b_locations, "b")
                    w_options = check_options(w_pieces, w_locations, "w")
                    turns = 0
                    piece_select = 420
                    valid_moves = []
                elif piece_select != 420 and piece_select == "king":
                    for r in range(len(castling_moves)):
                        if click_coord == castling_moves[r][0]:
                            b_locations[piece_select] = click_coord
                            b_moved[piece_select] = True
                            if click_coord == (1, 0):
                                rook_coords = (0, 0)
                            else:
                                rook_coords = (7, 0)
                            rook_index = b_locations.index(rook_coords)
                            b_locations[rook_index] = castling_moves[r][1]
                            black_options = check_options(b_options, b_locations, 'black')
                            white_options = check_options(w_pieces, w_locations, 'white')
                            turn_step = 0
                            piece_select = 420
                            valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:

                ## Resetting game results
                game_over = False
                winner = ''
                
                ## Resetting chess pieces pos

                ## White
                w_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
                w_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                w_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

                ## Black
                b_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
                b_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                b_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

                white_promote = False
                black_promote = False
                w_promo = ["Queen", "Knight", "Rook", "Bishop"]
                b_promo = ["Queen", "Knight", "Rook", "Bishop"]

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
