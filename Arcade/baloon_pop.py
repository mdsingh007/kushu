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

        arcade.set_background_color(arcade.color.ALICE_BLUE)
        self.set_mouse_visible(False)

    def create_random_baloon(self):
        balloon = arcade.Sprite('img/balloon.png')
        balloon.center_x = random.choice(range(0, 700))
        balloon.center_y = random.choice(range(0, 500))

        return balloon

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Setup global variables
        #self.x = random.choice(range(0, 700))
        #self.y = random.choice(range(0, 500))
        #self.ballX.append(x)
        #self.ballY.append(y)
        self.score = 0
        self.speed = 90
        self.balloon_list = arcade.SpriteList()
        self.mouse_loc = ''
        self.game_running = False
        self.message = " "
    

        self.game_over_sound = arcade.load_sound('sound/male/game_over.ogg')

        self.needle = arcade.Sprite('img/needle.png')


        self.balloon_list.append(self.create_random_baloon())


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.balloon_list.draw()
        arcade.draw_text( f"score: {self.score}", 20, 580, arcade.color.BLACK )
        self.needle.draw()
        #arcade.create_rectangle_filled(200, 200, 100, 100, arcade.color.BLACK)
        if self.game_running == False:
            arcade.draw_rectangle_filled(500, 300, 1000, 1000, arcade.color.WHITE)
            arcade.draw_text(self.message, 300, 400, arcade.color.BLACK, 25)
            arcade.draw_text("click on ballons to pop", 300, 300, arcade.color.BLACK)
            arcade.draw_text("press space to continue", 300, 280, arcade.color.BLACK)

            


    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse_loc = f'x: {x} y:{y}'
        for balloon in self.balloon_list:

            if arcade.check_for_collision(balloon, self.needle):
                self.balloon_list.remove(balloon)
                self.score += 1
                self.speed -= 2
    


    def on_mouse_motion(self, x, y, dx, dy):



        """ Called to update our objects. Happens approximately 60 times per second."""
        self.needle.center_x = x
        self.needle.center_y = y

    def update(self, delta_time):
        self.total_count += 1

        if self.total_count %self.speed == 0 and self.game_running == True:
            self.balloon_list.append( self.create_random_baloon() )
        
        if self.balloon_list.__len__() > 12 and self.game_running == True:
            arcade.play_sound(self.game_over_sound)
            self.game_running = False
            self.balloon_list = arcade.SpriteList()
            self.message = "Game Over"



    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.game_running = True



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()