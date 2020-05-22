""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING_DINO = 1
FLOOR = 200


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Don't show the mouse cursor
        # self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ALICE_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Setup global variables
        self.game_over = False
        self.going_up = False
        self.score = 0

        self.jump_sound = arcade.load_sound('sound/jump.wav')
        self.game_over_sound = arcade.load_sound('sound/male/game_over.ogg')
        self.level_up_sound = arcade.load_sound('sound/female/level_up.ogg')

        self.dino_up_speed = 20
        self.dino_down_speed = 2

        self.dino = arcade.Sprite('img/dino.png', SPRITE_SCALING_DINO)
        self.dino.center_x = 100
        self.dino.bottom = FLOOR

        self.cactus_speed = 2
        self.cactus_list = arcade.SpriteList()

        cactus = arcade.Sprite('img/cactus2.png', SPRITE_SCALING_DINO)
        cactus.bottom = FLOOR
        cactus.left = SCREEN_WIDTH
        self.cactus_list.append(cactus)

        cactus = arcade.Sprite('img/cactus.png', SPRITE_SCALING_DINO)
        cactus.bottom = FLOOR
        cactus.left = SCREEN_WIDTH
        self.cactus_list.append(cactus)

        cactus = arcade.Sprite('img/cactus3.png', SPRITE_SCALING_DINO)
        cactus.bottom = FLOOR
        cactus.left = SCREEN_WIDTH
        self.cactus_list.append(cactus)

        self.cactus = random.choice(self.cactus_list)

        self.score = 0

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 200, 0, arcade.color.PALE_GOLD)
        self.dino.draw()
        self.cactus_list.draw()
        arcade.draw_text( f"score: {self.score}  Level: {self.cactus_speed}", 20, 580, arcade.color.BLACK )



        if self.game_over:
            arcade.draw_text("game over", 300, 350, arcade.color.BLACK, 50)


    def update(self, delta_time):
        """ Movement and game logic """
        if self.game_over:
            return

        if arcade.check_for_collision(self.cactus, self.dino):
            arcade.play_sound(self.game_over_sound)
            self.game_over = True

        if self.going_up:
            self.dino.bottom += self.dino_up_speed
            if self.dino.bottom > 400: # This controls how high dino would jump
                self.going_up = False
                
        elif self.dino.bottom > 200:
            self.dino.bottom -= self.dino_down_speed
            if self.dino.bottom < 200: 
                self.dino.bottom = 200
        
        if self.cactus.right > 0:
            self.cactus.left -= self.cactus_speed
        else:
            self.score += 1
            if self.score % 2  == 0 :
                self.dino_down_speed += 1 
                self.dino_up_speed += 5
                self.cactus_speed += 1
                arcade.play_sound(self.level_up_sound)
            self.cactus = random.choice(self.cactus_list)
            self.cactus.left = SCREEN_WIDTH

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.dino.bottom == 200:
            self.going_up = True
            arcade.play_sound(self.jump_sound)
        if key == arcade.key.K and self.game_over:
            self.game_over = False
            self.cactus.left = SCREEN_WIDTH


            #self.dino.bottom = 400

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()