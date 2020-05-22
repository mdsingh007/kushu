import arcade

arcade.open_window(800, 600, '1+ k phone')
arcade.set_background_color(arcade.color.CELESTE)

arcade.start_render()

# Ground
arcade.draw_rectangle_filled(400, 100, 800, 200, arcade.color.GREEN)

# tractor grey body
arcade.draw_rectangle_filled(440, 70, 150, 50, arcade.color.GRAY)

# rear big wheels
arcade.draw_ellipse_filled(340, 60, 80, 80, arcade.color.BLACK)

# front small wheels
arcade.draw_ellipse_filled(490, 60, 45, 45, arcade.color.BLACK)

#draw_rectangle_filled(380, 120, 10, 50, arcade.color.BLACK)
#draw_rectangle_filled(430, 70, 65, 35, arcade.color.BLACK)

book = {
    'title': 'The Giver',
    'star': 4
}

# books = [ 
#     { title:"the giver", stars:4}, 
#     { title:"kushagra", stars:4}, 
#     { title:"manish", stars:4}, 
#     { title:"the", stars:4}, 
#     { title:"giver", stars:4}, 
#   ]

# first bookshelf
arcade.draw_rectangle_filled(400, 400, 800, 20, arcade.color.BISTRE_BROWN)

# first book
arcade.draw_rectangle_filled(100, 470, 100, 120, arcade.color.BITTERSWEET)
# book title
arcade.draw_text("The giver", 60, 510, arcade.color.SMALT)
for i in range(4):
    arcade.Sprite('img/bb.png', )

arcade.finish_render()
arcade.run()
