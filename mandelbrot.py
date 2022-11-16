from PIL import Image

new_im = Image.effect_mandelbrot((500,500),(-3.0, -2.5, 2.0, 2.5), 100)
new_im.save("f.jpg")
