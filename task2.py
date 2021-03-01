# Matt's Comment...I had to think more about how the letters are positioned for this task, then think about how to edit them as values inside the function. 

import axi

A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds
# Set your paper bounds here, to either landscape or portrait
BOUNDS = A4_PORT

def letter_T(t, x, y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x+4,y)
    t.pu()
    t.goto(x+2,y)
    t.pd()
    t.goto(x+2,y+2.5)
    t.pu()
    t.home()
    
def letter_U(t, x, y):

    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x,y+2.5)
    t.goto(x+2,y+2.5)
    t.goto(x+2,y)
    t.pu()
    t.home()

# combine code
def TUTU(t):
    # first letters
    letter_T(t,1,1.5)
    letter_U(t,5,1.5)

    # second letters
    letter_U(t,8,1.5)
    letter_T(t,10,1.5)
    
def save_img(t, name = 'out'):
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    im = drawing.render(bounds=BOUNDS) # render drawing
    im.write_to_png(name + '.png') # save a image of your drawing in a file called name.png
    
def draw_img(t):
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    axi.draw(drawing)

def main():
    t = axi.Turtle()
    # call combined function
    TUTU(t)
    output_img = 'task2_out'
    save_img(t, output_img)
    # draw_img(turtle) # Uncomment to draw your image
    
if __name__ == '__main__':
    main()