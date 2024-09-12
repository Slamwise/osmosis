from PIL import Image

im1 = Image.open(r'C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering\0r.png')

im = im1.convert('RGB')

im.save(r'C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering\0r.jpg')

