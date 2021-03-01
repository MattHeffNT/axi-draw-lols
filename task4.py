import axi

A4_PORT = (0, 0, 8.25, 11.75) # A4 Portrait bounds
A4_LAND = (0, 0, 11.75, 8.25) # A4 Landscape bounds
# Set your paper bounds here, to either landscape or portrait
BOUNDS = A4_PORT

def art(t):

    # main rectangle
    rec(t,3,4)

def rec(t,x,y):
    # draw rectangle
    t.pu()

    # width (6)
    t.goto(2,1)
    t.pd()
    t.goto(8,1)



    # height
    t.goto(8,5)
    t.goto(2,5)
    t.goto(2,1)
    t.pu()
    t.home()

def save_img(t, name = 'out'):
    drawing = t.drawing
    im = drawing.render() # render drawing
    im.write_to_png(name + '.png') # save a image of your drawing in a file called name.png
   
def draw_img(t):
    drawing = t.drawing.rotate_and_scale_to_fit(11.75, 8.25, step=90) # scale letter to fit A4-sized paper
    axi.draw(drawing)

def main():
    t = axi.Turtle()

    # call the art function
    art(t)

    output_img = 'task4-out'
    save_img(t, output_img)
    # draw_img(t) # Uncomment to draw your image
     
if __name__ == '__main__':
    main()
