import arcade
from arcade import *

open_window(800, 600, '1+ k phone')
set_background_color(arcade.color.CELESTE)

start_render()
draw_rectangle_filled(250, 50, 800, 200, arcade.color.GREEN)
draw_rectangle_filled(410, 70, 200, 50, arcade.color.GRAY)
draw_ellipse_filled(340, 60, 80, 80, arcade.color.BLACK)
draw_ellipse_filled(490, 60, 65, 65, arcade.color.BLACK)
draw_rectangle_filled(380, 120, 10, 50, arcade.color.BLACK)
draw_rectangle_filled(430, 70, 65, 35, arcade.color.BLACK)








finish_render()
run()
