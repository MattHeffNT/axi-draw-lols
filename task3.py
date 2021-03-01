# Matt's Comment...This one was a good challenge, I really had to plan out how I wanted to approach it in the "simplest" way that I could.

import axi

A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds
# Set your paper bounds here, to either landscape or portrait
BOUNDS = A4_LAND

draw = True

def letter_T(t, x, y):

    # function to draw the letter 'X' starting at a specific starting point (x,y)
    
    t.pu()
    t.goto(2+x,3+y)
    t.pd()
    t.goto(3+x,3+y)
    t.pu()
    t.goto(3+x,2.5+y)
    t.pd()
    t.goto(3+x,3.5+y)
    t.pu()
    t.home()

def pyramid(t, width, height, levels):
    for i in range (levels):

        for j in range(levels-i):

            letter_T(t,j+1,levels-i)

        for j in range(levels-i):

            letter_T(t,j+1,levels+i)
            
def save_img(t, name = 'out'):
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    im = drawing.render(bounds=BOUNDS) # render drawing
    im.write_to_png(name + '.png') # save a image of your drawing in a file called name.png
    
def draw_img(t):
    drawing = t.drawing.rotate_and_scale_to_fit(BOUNDS[2], BOUNDS[3], step=90, padding=0.5) # scale letter to fit A4-sized paper
    axi.draw(drawing)

def main():
    t = axi.Turtle()
    width = int(input("please enter width: "))
    height = int(input("please enter height: "))
    levels = int(input("please enter levels: "))

    # pass values to pyramid builder function
    pyramid(t, width, height, levels)

    output_img = 'task3-out'
    save_img(t, output_img)
    draw_img(t)
 
if __name__ == '__main__':
    main()