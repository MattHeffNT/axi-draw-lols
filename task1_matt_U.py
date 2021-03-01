# Matt's Comment... I really struggled with understanding the coordinate system and how to visualize what I wanted to do. Myrna helped me by first mapping the XY on paper then transposing into the code.
#after this, i rearranged my code to display sideways (to work with pyramid code)

import axi
# Set this variable to true when you wish to draw with the plotter.

A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds
# Set your paper bounds here, to either landscape or portrait
BOUNDS = A4_LAND

draw = True

# make global object so all functions can access it
t = axi.Turtle()

def draw_t():
    # sideways T
    t.pu()
    t.goto(2,3)
    t.pd()
    t.goto(3,3)
    t.pu()
    t.goto(3,2.5)
    t.pd()
    t.goto(3,3.5)
    t.pu()
    t.home()

def draw_u():
    # sideways u
    t.pu()
    t.goto(3,4)
    t.pd()
    t.goto(2,4)
    # t.circle()
    t.goto(2,5)
    t.goto(2,5)
    t.goto(3,5)
    # t.goto()
    t.pu()

def save_img(t, name = 'out'):
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    im = drawing.render(bounds=BOUNDS) # render drawing
    im.write_to_png(name + '.png') # save a image of your drawing in a file called name.png

def draw_img(t):
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    axi.draw(drawing)

if __name__ == '__main__':

    # draw_t()
    draw_u()
    output_img = 'task1_out'
    save_img(t, output_img)
    draw_img(t)