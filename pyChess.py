## Importing the module for the on screen UI
import pygame

## Initialising the board, and all the positions
pygame.init()

## Big Screen
w = 1000
h = 900
screen = pygame.display.set_mode([w, h])

## Fonts
font = pygame.font.Font("BLKCHCRY.ttf", 20)
medium_font = pygame.font.Font("BLKCHCRY.ttf", 40)
big_font = pygame.font.Font("BLKCHCRY.ttf", 50)

## Misc
timer = pygame.time.Clock()
fps = 144
pygame.display.set_caption("IncogniChess")

## Game Coordinates
b_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
b_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

w_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
w_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

## Captured pieces
captured_pieces_white = []
captured_pieces_black = []

## 0: black no pieces selected, 1: black piece selected, 2: white no pieces selected, 3: white piece selected
turns = 2

## Piece selected
selection = 100

## The list of valid moves
valid_moves = []

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

## Image Deciding
w_images = [w_pawn, w_queen, w_king, w_knight, w_rook, w_bishop]
small_w_images = [w_pawn_small, w_queen_small, w_king_small, w_knight_small,
                      w_rook_small, w_bishop_small]
b_images = [b_pawn, b_queen, b_king, b_knight, b_rook, b_bishop]
small_b_images = [b_pawn_small, b_queen_small, b_king_small, b_knight_small,
                      b_rook_small, b_bishop_small]

## Pieces move status (mainly for castling and pawn double movements)
w_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]
b_moved = [False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False]

## Promotion options
w_promotions = ["bishop", "knight", "rook", "queen"]
b_promotions = ["bishop", "knight", "rook", "queen"]


## List of pieces for easier reference
piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]

## Flags/ Flashing for check
counter = 0
winner = ""
game_over = False
w_ep = (100, 100)
b_ep = (100, 100)
w_promote = False
b_promote = False
promo_index = 100
check = False
castling_moves = []

## Drawing the chessboard
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

        ## Promotion UI
        if w_promote or b_promote:
            pygame.draw.rect(screen, "orchid1", [0, 800, w - 200, 100])
            pygame.draw.rect(screen, "gold", [0, 800, w - 200, 100], 5)
            screen.blit(big_font.render("Select Piece to Promote Pawn", True, "black"), (20, 820))


## Draw pieces onto board
def draw_pieces():

    ## Drawing black pieces
    for i in range(len(b_pieces)):
        index = piece_list.index(b_pieces[i])
        if b_pieces[i] == "pawn":
            screen.blit(b_pawn, (b_locations[i][0] * 100 + 12, b_locations[i][1] * 100 + 16))
        else:
            screen.blit(b_images[index], (b_locations[i][0] * 100 + 10, b_locations[i][1] * 100 + 10))
        if turns < 2:
            if selection == i:
                pygame.draw.rect(screen, "red", [b_locations[i][0] * 100 + 1, b_locations[i][1] * 100 + 1, 100, 100], 2)

    ## Drawing white pieces
    for i in range(len(w_pieces)):
        index = piece_list.index(w_pieces[i])
        if w_pieces[i] == "pawn":
            screen.blit(w_pawn, (w_locations[i][0] * 100 + 12, w_locations[i][1] * 100 + 16))
        else:
            screen.blit(w_images[index], (w_locations[i][0] * 100 + 10, w_locations[i][1] * 100 + 10))
        if turns >= 2:
            if selection == i:
                pygame.draw.rect(screen, "red", [w_locations[i][0] * 100 + 1, w_locations[i][1] * 100 + 1, 100, 100], 5)


## function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    global castling_moves
    moves_list = []
    all_moves_list = []
    castling_moves = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == "pawn":
            moves_list = check_pawn(location, turn)
        elif piece == "rook":
            moves_list = check_rook(location, turn)
        elif piece == "knight":
            moves_list = check_knight(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop(location, turn)
        elif piece == "queen":
            moves_list = check_queen(location, turn)
        elif piece == "king":
            moves_list, castling_moves = check_king(location, turn)  ## Extra step to check for castling
        all_moves_list.append(moves_list)
    return all_moves_list


## Check king valid moves
def check_king(pos, colour):
    moves_list = []
    castle_moves = check_castling()
    if colour == "white":
        enemies_list = w_locations
        friends_list = b_locations
    else:
        friends_list = w_locations
        enemies_list = b_locations

    ## King can only move one square around him
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (pos[0] + targets[i][0], pos[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list, castle_moves


## Check queen valid moves
def check_queen(pos, colour):

    ## Using rook and bishop as check because it is the same logic
    moves_list = check_bishop(pos, colour)
    second_list = check_rook(pos, colour)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


## Check bishop moves
def check_bishop(pos, colour):
    moves_list = []
    if colour == "white":
        enemies_list = w_locations
        friends_list = b_locations
    else:
        friends_list = w_locations
        enemies_list = b_locations
    
    ## Checking for all diagonals until the path is blocked
    for i in range(4): 
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (pos[0] + (chain * x), pos[1] + (chain * y)) not in friends_list and \
                    0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                if (pos[0] + (chain * x), pos[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


## Check rook moves
def check_rook(pos, colour):
    moves_list = []
    if colour == "white":
        enemies_list = w_locations
        friends_list = b_locations
    else:
        friends_list = w_locations
        enemies_list = b_locations
    
    ## Checking for all vertical lines until the path is blocked
    for i in range(4): 
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (pos[0] + (chain * x), pos[1] + (chain * y)) not in friends_list and \
                    0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                if (pos[0] + (chain * x), pos[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


## Check valid pawn moves
def check_pawn(pos, colour):
    moves_list = []

    ## For white
    if colour == "white":

        ## Normal Pawn Move
        if (pos[0], pos[1] + 1) not in b_locations and \
                (pos[0], pos[1] + 1) not in w_locations and pos[1] < 7:
            moves_list.append((pos[0], pos[1] + 1))
            
            ## Checking two squares ahead if theyre still on the initial square
            if (pos[0], pos[1] + 2) not in b_locations and \
                    (pos[0], pos[1] + 2) not in w_locations and pos[1] == 1:
                moves_list.append((pos[0], pos[1] + 2))
        
        ## Attacking a piece
        if (pos[0] + 1, pos[1] + 1) in w_locations:
            moves_list.append((pos[0] + 1, pos[1] + 1))
        if (pos[0] - 1, pos[1] + 1) in w_locations:
            moves_list.append((pos[0] - 1, pos[1] + 1))
        
        ## Checking if en passant is playable
        if (pos[0] + 1, pos[1] + 1) == b_ep:
            moves_list.append((pos[0] + 1, pos[1] + 1))
        if (pos[0] - 1, pos[1] + 1) == b_ep:
            moves_list.append((pos[0] - 1, pos[1] + 1))
    
    ## For black
    else:

        ## Normal Pawn Move
        if (pos[0], pos[1] - 1) not in b_locations and \
                (pos[0], pos[1] - 1) not in w_locations and pos[1] > 0:
            moves_list.append((pos[0], pos[1] - 1))
            
            ## Checking two squares ahead if theyre still on the initial square
            if (pos[0], pos[1] - 2) not in b_locations and \
                    (pos[0], pos[1] - 2) not in w_locations and pos[1] == 6:
                moves_list.append((pos[0], pos[1] - 2))
        
        ## Attacking a piece
        if (pos[0] + 1, pos[1] - 1) in b_locations:
            moves_list.append((pos[0] + 1, pos[1] - 1))
        if (pos[0] - 1, pos[1] - 1) in b_locations:
            moves_list.append((pos[0] - 1, pos[1] - 1))
        
        ## Checking if en passant is playable
        if (pos[0] + 1, pos[1] - 1) == w_ep:
            moves_list.append((pos[0] + 1, pos[1] - 1))
        if (pos[0] - 1, pos[1] - 1) == w_ep:
            moves_list.append((pos[0] - 1, pos[1] - 1))
    return moves_list


## Check valid knight moves
def check_knight(pos, colour):
    moves_list = []
    if colour == "white":
        enemies_list = w_locations
        friends_list = b_locations
    else:
        friends_list = w_locations
        enemies_list = b_locations
    
    ## Squares Knights can moved are fixed unless it has a friendly target
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (pos[0] + targets[i][0], pos[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


## Check for valid moves for just selected piece
def check_valid_moves():
    if turns < 2:
        options = w_options
    else:
        options = b_options
    valid_options = options[selection]
    return valid_options


## Adding dots to indicate moves that are valid
def draw_valid(moves):
    for i in range(len(moves)):
        pygame.draw.circle(screen, "red", (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 10)


## Drawing the captured pieces that will appear on side of screen mimicking how it is like on an actual chess table
def draw_captured():

    ## For the white captured pieces 
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_w_images[index], (825, 5 + 50 * i))
    
    ## For the black captured pieces 
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_b_images[index], (925, 5 + 50 * i))


## Creating a flashing square around king if in check
def draw_check():
    global check
    check = False
    if turns < 2:
        if "king" in b_pieces:
            king_index = b_pieces.index("king")
            king_location = b_locations[king_index]
            for i in range(len(b_options)):
                if king_location in b_options[i]:
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, "dark red", [b_locations[king_index][0] * 100 + 1,
                                                              b_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if "king" in w_pieces:
            king_index = w_pieces.index("king")
            king_location = w_locations[king_index]
            for i in range(len(w_options)):
                if king_location in w_options[i]:
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, "dark red", [w_locations[king_index][0] * 100 + 1,
                                                               w_locations[king_index][1] * 100 + 1, 100, 100], 5)

## Once game is over, this pop up will appear!
def draw_game_over():
    pygame.draw.rect(screen, "purple", [200, 200, 400, 70])
    screen.blit(font.render(f"{winner} won the game!", True, "white"), (210, 210))
    screen.blit(font.render(f"Press ENTER to Restart!", True, "white"), (210, 240))


## Checking for a possiblilty for en passant which is a rule in chess not commonly known by beginners
def check_ep(old_coords, new_coords):
    if turns <= 1:
        index = b_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] - 1)
        piece = b_pieces[index]
    else:
        index = w_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = w_pieces[index]
    if piece == "pawn" and abs(old_coords[1] - new_coords[1]) > 1:
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords


## Castling for the king which involves very specific rules to follow
def check_castling():
    castle_moves = [] 
    rook_indexes = []
    rook_locations = []
    king_index = 0
    king_pos = (0, 0)
    if turns > 1:
        for i in range(len(b_pieces)):
            if b_pieces[i] == "rook":
                rook_indexes.append(w_moved[i])
                rook_locations.append(b_locations[i])
            if b_pieces[i] == "king":
                king_index = i
                king_pos = b_locations[i]
        if not w_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in b_locations or empty_squares[j] in w_locations or \
                            empty_squares[j] in b_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    else:
        for i in range(len(w_pieces)):
            if w_pieces[i] == "rook":
                rook_indexes.append(b_moved[i])
                rook_locations.append(w_locations[i])
            if w_pieces[i] == "king":
                king_index = i
                king_pos = w_locations[i]
        if not b_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in b_locations or empty_squares[j] in w_locations or \
                            empty_squares[j] in w_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    return castle_moves

## Having a seperate UDF for castling pieces as it is a very specific set of moves
def draw_castling(moves):
    if turns < 2:
        colour = "red"
    else:
        colour = "red"
    for i in range(len(moves)):
        pygame.draw.circle(screen, colour, (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70), 8)
        screen.blit(font.render("king", True, "black"), (moves[i][0][0] * 100 + 30, moves[i][0][1] * 100 + 70))
        pygame.draw.circle(screen, colour, (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 8)
        screen.blit(font.render("rook", True, "black"),
                    (moves[i][1][0] * 100 + 30, moves[i][1][1] * 100 + 70))
        pygame.draw.line(screen, colour, (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70),
                         (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 2)


## Pawn promoting!
def check_promotion():
    pawn_indexes = []
    w_promotion = False
    b_promotion = False
    promote_index = 100
    for i in range(len(b_pieces)):
        if b_pieces[i] == "pawn":
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if b_locations[pawn_indexes[i]][1] == 7:
            w_promotion = True
            promote_index = pawn_indexes[i]
    pawn_indexes = []
    for i in range(len(w_pieces)):
        if w_pieces[i] == "pawn":
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if w_locations[pawn_indexes[i]][1] == 0:
            b_promotion = True
            promote_index = pawn_indexes[i]
    return w_promotion, b_promotion, promote_index

## Having a seperate UDF for promotion as the player can select what pieces to promote to
def draw_promotion():
    pygame.draw.rect(screen, "dark gray", [800, 0, 200, 420])
    if w_promote:
        colour = "white"
        for i in range(len(w_promotions)):
            piece = w_promotions[i]
            index = piece_list.index(piece)
            screen.blit(w_images[index], (860, 5 + 100 * i))
    elif b_promote:
        colour = "black"
        for i in range(len(b_promotions)):
            piece = b_promotions[i]
            index = piece_list.index(piece)
            screen.blit(b_images[index], (860, 5 + 100 * i))
    pygame.draw.rect(screen, colour, [800, 0, 200, 420], 8)

## Promotion selecting
def check_promo_select():
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100
    y_pos = mouse_pos[1] // 100
    if w_promote and left_click and x_pos > 7 and y_pos < 4:
        b_pieces[promo_index] = w_promotions[y_pos]
    elif b_promote and left_click and x_pos > 7 and y_pos < 4:
        w_pieces[promo_index] = b_promotions[y_pos]


## Game
b_options = check_options(w_pieces, w_locations, "black")
w_options = check_options(b_pieces, b_locations, "white")
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill("mediumpurple1")
    
    ## Constant UDFs to run
    draw_ui()
    draw_pieces()
    draw_captured()
    draw_check()

    ## While game is still running
    if not game_over:

        ## Promoting sequence
        w_promote, b_promote, promo_index = check_promotion()
        if w_promote or b_promote:
            draw_promotion()
            check_promo_select()
    
    ## If a piece got selected
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

        ## Special case for king
        if selected_piece == "king":
            draw_castling(castling_moves)
    

    ## Events in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        ## Checking mouse location
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)

            ## Checking white's turn
            if turns > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = "White"
                if click_coords in w_locations:
                    selection = w_locations.index(click_coords)

                    ## Check what piece is selected, so you can only draw castling moves if king is selected
                    selected_piece = w_pieces[selection]
                    if turns == 2:
                        turns = 3
                
                ## Showing valid moves for white
                if click_coords in valid_moves and selection != 100:
                    b_ep = check_ep(w_locations[selection], click_coords)
                    w_locations[selection] = click_coords
                    b_moved[selection] = True
                    if click_coords in b_locations:
                        w_piece = b_locations.index(click_coords)
                        captured_pieces_black.append(b_pieces[w_piece])
                        if b_pieces[w_piece] == "king":
                            winner = "Black"
                        b_pieces.pop(w_piece)
                        b_locations.pop(w_piece)
                        w_moved.pop(w_piece)
                    if click_coords == w_ep:
                        w_piece = b_locations.index((w_ep[0], w_ep[1] + 1))
                        captured_pieces_black.append(b_pieces[w_piece])
                        b_pieces.pop(w_piece)
                        b_locations.pop(w_piece)
                        w_moved.pop(w_piece)
                    b_options = check_options(w_pieces, w_locations, "black")
                    w_options = check_options(b_pieces, b_locations, "white")

                    ## Resetting over to black
                    turns = 0
                    selection = 100
                    valid_moves = []
                
                ## Adding option to castle
                elif selection != 100 and selected_piece == "king":
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            w_locations[selection] = click_coords
                            b_moved[selection] = True
                            if click_coords == (1, 7):
                                rook_coords = (0, 7)
                            else:
                                rook_coords = (7, 7)
                            rook_index = w_locations.index(rook_coords)
                            w_locations[rook_index] = castling_moves[q][1]
                            b_options = check_options(w_pieces, w_locations, "black")
                            w_options = check_options(b_pieces, b_locations, "white")

                            ## Resetting over to black
                            turns = 0
                            selection = 100
                            valid_moves = []
            
            ## Checking if its black's turn
            if turns <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = "black"
                if click_coords in b_locations:
                    selection = b_locations.index(click_coords)

                    ## Check what piece is selected, so you can only draw castling moves if king is selected
                    selected_piece = b_pieces[selection]
                    if turns == 0:
                        turns = 1
                
                ## Showing valid moves for white
                if click_coords in valid_moves and selection != 100:
                    w_ep = check_ep(b_locations[selection], click_coords)
                    b_locations[selection] = click_coords
                    w_moved[selection] = True
                    if click_coords in w_locations:
                        b_piece = w_locations.index(click_coords)
                        captured_pieces_white.append(w_pieces[b_piece])
                        if w_pieces[b_piece] == "king":
                            winner = "White"
                        w_pieces.pop(b_piece)
                        w_locations.pop(b_piece)
                        b_moved.pop(b_piece)
                    if click_coords == b_ep:
                        b_piece = w_locations.index((b_ep[0], b_ep[1] - 1))
                        captured_pieces_white.append(w_pieces[b_piece])
                        w_pieces.pop(b_piece)
                        w_locations.pop(b_piece)
                        b_moved.pop(b_piece)
                    b_options = check_options(w_pieces, w_locations, "black")
                    w_options = check_options(b_pieces, b_locations, "white")

                     ## Resetting over to white
                    turns = 2
                    selection = 100
                    valid_moves = []

                ## Adding option to castle
                elif selection != 100 and selected_piece == "king":
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            b_locations[selection] = click_coords
                            w_moved[selection] = True
                            if click_coords == (1, 0):
                                rook_coords = (0, 0)
                            else:
                                rook_coords = (7, 0)
                            rook_index = b_locations.index(rook_coords)
                            b_locations[rook_index] = castling_moves[q][1]
                            b_options = check_options(w_pieces, w_locations, "black")
                            w_options = check_options(b_pieces, b_locations, "white")

                             ## Resetting over to white
                            turns = 2
                            selection = 100
                            valid_moves = []
        
        ## Resetting the game
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ""
                b_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                b_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                w_moved = [False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False]
                w_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                w_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                b_moved = [False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False]
                captured_pieces_white = []
                captured_pieces_black = []
                turns = 2
                selection = 100
                valid_moves = []
                b_options = check_options(w_pieces, w_locations, "black")
                w_options = check_options(b_pieces, b_locations, "white")

    if winner != "":
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()
