import arcade


def main():
    arcade.open_window(900, 600, "shape project")
    arcade.set_background_color(arcade.color.PURPLE_NAVY)
    arcade.start_render()
    moon = arcade.create_ellipse(120, 500, 150, 150, arcade.color.IVORY)
    bottom = arcade.create_rectangle(120, 200, 500, 400, arcade.color.BLUE)
    middle = arcade.create_ellipse(375, 400, 210, 210, arcade.color.IVORY)
    top = arcade.create_ellipse(375, 600, 100, 100, arcade.color.IVORY)


    moon.draw()
    bottom.draw()
    middle.draw()
    top.draw()
    arcade.finish_render()
    arcade.run()


main()