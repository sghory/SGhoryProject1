import arcade


def main():
    #creates popup widnow
    arcade.open_window(500, 700, "shape project")
    #adds background color
    arcade.set_background_color(arcade.color.PURPLE_NAVY)
    #bottom of the snowman
    bottom = arcade.create_ellipse(250, 150, 300, 300, arcade.color.IVORY)
    #middle of the snowman
    middle = arcade.create_ellipse(250, 350, 260, 260, arcade.color.IVORY)
    #head of snowman
    top = arcade.create_ellipse(250, 520, 200, 200, arcade.color.IVORY)
    #nose of snowman
    nose = arcade.create_polygon([(250,520), (250, 490), (175, 520)], arcade.color.ORANGE)
    #first button
    button1 = arcade.create_ellipse(250, 400, 30, 30, arcade.color.SMOKY_BLACK)
    #second button
    button2 = arcade.create_ellipse(250, 300, 30, 30, arcade.color.SMOKY_BLACK)
    #third button
    button3 = arcade.create_ellipse(250, 200, 30, 30, arcade.color.SMOKY_BLACK)
    #left eye
    eye1 = arcade.create_ellipse(200, 550, 45, 45, arcade.color.SMOKY_BLACK)
    #right eye
    eye2 = arcade.create_ellipse(300, 550, 45, 45, arcade.color.SMOKY_BLACK)
    #top of the tophat
    tophat = arcade.create_rectangle(250, 640, 70, 70, arcade.color.BLACK_OLIVE)
    #bottom of the tophat
    tophat2 = arcade.create_rectangle(250, 600, 180, 40, arcade.color.BLACK_OLIVE)
    #scarf of snowman
    scarf = arcade.create_rectangle(250, 450, 200, 40, arcade.color.FIREBRICK)
    arcade.start_render()

    bottom.draw()
    middle.draw()
    top.draw()
    nose.draw()
    button1.draw()
    button2.draw()
    button3.draw()
    eye1.draw()
    eye2.draw()
    tophat.draw()
    tophat2.draw()
    scarf.draw()
    arcade.finish_render()
    arcade.run()


main()