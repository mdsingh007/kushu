
from distutils.log import debug
import arcade

SCREEN_WIDTH = 100*8
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Othello | Game of wits"

soundBadMove = arcade.load_sound("sounds/wall.wav")
soundConfirmMove = arcade.load_sound("sounds/valid.wav")
soundGameOver = arcade.load_sound("sounds/exit.wav")

board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]


cursor = [0,3]

animated_cir_rad = 30
animated_cir_rad_ch = 1
capture_positions = []
ai_move_to = []
ai_slow_factor = 10
game_over = False

players = [
    {   'name': 'Player 1',     'type':"AI",         'score':0,      'number': 0,        'color':1, 
        'anim':3,               'boardnums': [1, 3],    'coincolor': arcade.color.MOONSTONE_BLUE},
    {'name': 'Player 2', 'type':"AI", 'score':0, 'number': 1, 'color':2, 
        'anim':4, 'boardnums': [2, 4], 'coincolor': arcade.color.ORANGE_RED},
]

player = players[0]
oplayer = players[1]

def draw_board():
    global animated_cir_rad

    # Draw Grid
    # vertical lines
    for x in range(9):
        arcade.draw_line(x*100, 0, x*100, 100*8, arcade.color.BLACK, 4)
    # horizontal lines
    for x in range(9):
        arcade.draw_line(0, x*100, 100*8, x*100, arcade.color.BLACK, 4)

    for y, row in enumerate(board):
        for x, cellx in enumerate(row):
            
            cc = x*100 + 50, (8-y)*100 - 50 # cell center

            if cellx == 1:
                arcade.draw_circle_filled(cc[0],cc[1], 30, players[0]['coincolor'])
            if cellx == 2:
                arcade.draw_circle_filled(cc[0],cc[1], 30, players[1]['coincolor']	)
            if cellx == 3:
                arcade.draw_circle_filled(cc[0],cc[1], animated_cir_rad, players[0]['coincolor']	)
            if cellx == 4:
                arcade.draw_circle_filled(cc[0],cc[1], animated_cir_rad, players[1]['coincolor']	)

            #draw cursor
            if y == cursor[0] and x == cursor[1]:
                arcade.draw_rectangle_outline(cc[0], cc[1], 91, 91, player['coincolor'], 5)

def get_capture_positions(from_cursor):
    global player, oplayer

    row, col = from_cursor
    cap_pos = []

    if board[row][col]  == 0:
        # check up
        c_p_up = []
        move = 0
        while row - move > 0:
            move = move + 1
            if board[row-move][col] in oplayer['boardnums']:
                c_p_up.append( (row - move, col) )
            elif board[row-move][col] in player['boardnums']:
                cap_pos.extend(c_p_up)
                break
            else:
                break
        # check down
        c_p_dn = []
        move = 0
        while row + move < 7:
            move = move + 1
            if board[row+move][col] in oplayer['boardnums']:
                c_p_dn.append( (row + move, col) )
            elif board[row+move][col] in player['boardnums']:
                cap_pos.extend(c_p_dn)
                break
            else:
                break

        # check right
        c_p_rt = []
        move = 0
        while col + move < 7:
            move = move + 1
            if board[row][col+move] in oplayer['boardnums']:
                c_p_rt.append( (row, col+move) )
            elif board[row][col+move] in player['boardnums']:
                cap_pos.extend(c_p_rt)
                break
            else:
                break


        # check left
        c_p_lf = []
        move = 0
        while col - move > 0:
            move = move + 1
            if board[row][col-move] in oplayer['boardnums']:
                c_p_lf.append( (row, col-move) )
            elif board[row][col-move] in player['boardnums']:
                cap_pos.extend(c_p_lf)
                break
            else:
                break

        # check diag down right
        c_p_ddr = []
        move = 0
        while col + move < 7 and row + move < 7:
            move = move + 1
            nc = col + move
            nr = row + move

            if board[nr][nc] in oplayer['boardnums']:
                c_p_ddr.append( (nr, nc) )
            elif board[nr][nc] in player['boardnums']:
                cap_pos.extend(c_p_ddr)
                break
            else:
                break

        # check diag down left
        c_p_ddr = []
        move = 0
        while col - move > 0 and row + move < 7:
            move = move + 1
            nc = col - move
            nr = row + move

            if board[nr][nc] in oplayer['boardnums']:
                c_p_ddr.append( (nr, nc) )
            elif board[nr][nc] in player['boardnums']:
                cap_pos.extend(c_p_ddr)
                break
            else:
                break
            
        # check diag up left
        c_p_ddr = []
        move = 0
        while col - move > 0 and row - move > 0:
            move = move + 1
            nc = col - move
            nr = row - move

            if board[nr][nc] in oplayer['boardnums']:
                c_p_ddr.append( (nr, nc) )
            elif board[nr][nc] in player['boardnums']:
                cap_pos.extend(c_p_ddr)
                break
            else:
                break

        # check diag up right
        c_p_ddr = []
        move = 0
        while col + move < 7 and row - move > 0:
            move = move + 1
            nc = col + move
            nr = row - move

            if board[nr][nc] in oplayer['boardnums']:
                c_p_ddr.append( (nr, nc) )
            elif board[nr][nc] in player['boardnums']:
                cap_pos.extend(c_p_ddr)
                break
            else:
                break    

    return cap_pos

def get_best_move():
    best_move_loc = []
    best_move_pts = []
    # find best position to move
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if board[r][c] == 0:
                cc = get_capture_positions((r, c))
                if len(cc) > len(best_move_pts):
                    best_move_pts = cc
                    best_move_loc = (r, c)
    return best_move_loc

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)
        self.set_update_rate(1/20)
        arcade.set_background_color(arcade.color.ONYX	)

    def setup(self):
        """ Set up the game and initialize the variables. """

        pass

    def on_draw(self):
        """
        Render the screen.
        """
        global player
        # This command has to happen before we start drawing
        self.clear()

        # draw scores
        arcade.draw_text(str(players[0]['score']), 80, 100*8+30, arcade.color.WHITE, 40)
        arcade.draw_circle_filled(50,100*8+50, 20, players[0]['coincolor']	)

        arcade.draw_text(str(players[1]['score']), 360, 100*8+30, arcade.color.WHITE, 40)
        arcade.draw_circle_filled(330,100*8+50, 20, players[1]['coincolor']	)

        draw_board()

    def on_update(self, delta_time):
        """ Movement and game logic """
        global board, cursor, player, players, capture_positions, oplayer
        global animated_cir_rad, animated_cir_rad_ch, ai_move_to, ai_slow_factor, game_over

        if game_over:
            arcade.play_sound(soundGameOver)
            return

        # animation logic; change radius of animated coins
        animated_cir_rad += animated_cir_rad_ch
        if animated_cir_rad > 32:
            animated_cir_rad_ch = -1
        elif animated_cir_rad < 27:
            animated_cir_rad_ch = 1


        # get current cursor position value
        row, col = cursor[0], cursor[1]

        # which coins player can capture from this cursor location?
        capture_positions = get_capture_positions((row, col))

        # update board so possible capture positions can animate                                
        for r, c in capture_positions:
            if board[r][c] == 1:
                board[r][c] = 3
            elif board[r][c] == 2:
                board[r][c] = 4

        # move cursor if AI is moving
        if player['type'] == 'AI':
            ai_slow_factor += 1
            if ai_slow_factor > 0:
                ai_slow_factor = 0
                if ai_move_to:
                    if ai_move_to[0] == cursor[0] and ai_move_to[1] == cursor[1]:
                        self.on_key_press(arcade.key.ENTER, None)
                        ai_move_to = []
                        ai_slow_factor = 0
                    else:
                        if ai_move_to[0] > cursor[0]:
                            self.on_key_press(arcade.key.DOWN, None)
                        elif ai_move_to[0] < cursor[0]:
                            self.on_key_press(arcade.key.UP, None)
                        elif ai_move_to[1] > cursor[1]:
                            self.on_key_press(arcade.key.RIGHT, None)
                        elif ai_move_to[1] < cursor[1]:
                            self.on_key_press(arcade.key.LEFT, None)
                else:
                    ai_move_to = get_best_move()

    def on_key_press(self, key, modifiers):
        global cursor, board, capture_positions, player, oplayer, game_over

        # reset animation
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] == 3:
                    board[r][c] = 1
                if board[r][c] == 4:
                    board[r][c] = 2

        # move cursor
        if key == arcade.key.DOWN and cursor[0] < 7:
            cursor[0] += 1
        if key == arcade.key.UP and cursor[0] > 0:
            cursor[0] -= 1
        if key == arcade.key.RIGHT and cursor[1] < 7:
            cursor[1] += 1
        if key == arcade.key.LEFT and cursor[1] > 0:
            cursor[1] -= 1
        if key == arcade.key.ENTER:
            for r, c in capture_positions:
                board[r][c] = player['color']
            
            if capture_positions:
                # Only allow place to be captured if capture_positions are available
                board[cursor[0]][cursor[1]] = player['color']

                # count score
                players[0]['score'] = 0
                players[1]['score'] = 0
                for r, row in enumerate(board):
                    for c, col in enumerate(row):
                        if board[r][c] == 1 or board[r][c] == 3:
                            players[0]['score'] += 1
                        if board[r][c] == 2 or board[r][c] == 4:
                            players[1]['score'] += 1
                        
                arcade.play_sound(soundConfirmMove)

                # swap player and other player
                player, oplayer = oplayer, player

                # check if game is over
                print ('get_best_move', get_best_move())
                if not get_best_move():
                    game_over = True
            else:
                arcade.play_sound(soundBadMove)



    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()