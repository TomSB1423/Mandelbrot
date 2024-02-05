from PIL import Image, ImageDraw
from mandelbrot import mandelbrot
from stability import Stability

WIDTH = 500
HEIGHT = 500

im = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        t_x = (x - WIDTH / 1.4) / WIDTH * 2
        t_y = (y - HEIGHT / 2) / HEIGHT * 2
        stablilty = mandelbrot(t_x, t_y)
        if stablilty == Stability.Stable:
            color = 255
        else:
            color = 0
        draw.point([x, y], (color, color, color))


im.save("./output.png", "PNG")
