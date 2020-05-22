# new game

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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Baloon Popper")
        self.total_count = 0
        # Don't show the mouse cursor
        # self.set_mouse_visible(False)


    def create_random_baloon(self):
        pass

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Setup global variables
        self.score = 0    
        self.game_over_sound = arcade.load_sound('sound/male/game_over.ogg')

        self.grid = arcade.Sprite('img/grid.png')
        self.grid.center_x = 400
        self.grid.center_y = 300

        self.x = arcade.Sprite('img/x.png')
        self.o = arcade.Sprite('img/o.png')



    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        arcade.set_background_color(arcade.color.ALICE_BLUE)
        self.grid.draw()
        self.x.draw()




    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass


    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""



    def on_key_press(self, key, modifiers):
        pass



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()