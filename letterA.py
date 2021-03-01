import axi
# Set this variable to true when you wish to draw with the plotter.
draw = False

def main():
    t = axi.Turtle()
    t.pd()
    t.goto(2, -5)
    t.goto(4, 0)
    t.pu()
    t.home()

    # YOUR CODE HERE

    # t.pu()
    # t.goto()

    # t.goto()

    # Scale letter to fit A4-sized paper
    drawing = t.drawing.rotate_and_scale_to_fit(8.25, 11.75, step=180, padding=0.25)
    # Render drawing
    im = drawing.render()
    # Create an image file of the drawing
    im.write_to_png('out.png')
    # Draw with the plotter if relevant
    if draw:
        axi.draw(drawing)

if __name__ == '__main__':
    main()
