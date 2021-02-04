import arcade
from arcade.color import YELLOW_ORANGE

#set constants for the screen size
screen_width = 600
screen_height = 600

# Open the window. Window
arcade.open_window(screen_width, screen_height, "drawing trial")
# Set the background color
# For a list of named colors see:
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.

arcade.set_background_color(arcade.color.AO)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

#draw face
x = 300
y = 300
radius = 200
arcade.draw.circle(x, y, radius, arcade.color.YELLOW_ORANGE)

#draw the left eye
x = 230
y= 350
radius = 20
arcade.draw_circle_filled(x,y, radius, arcade.color.GOLDEN_BROWN)

#draw right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius,arcade.color.DONKEY_BROWN)

#draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x,y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# finish drawing
arcade.finish_render()

#keep the window open unti the user hits the 'close' button
arcade.run()
