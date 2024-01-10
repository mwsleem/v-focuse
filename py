from PIL import Image
 
im = Image.open("image.png")
pixels = im.load()
x, y = im.size
dr = pixels[0, 0]
t, d, le, r = y + 1, 0, x + 1, 0
for i in range(x):
    for i1 in range(y):
        if pixels[i, i1] != dr:
            if i1 < t:
                t = i1
            if i1 > d:
                d = i1
            if i > r:
                r = i
            if i < le:
                le = i
im2 = im.crop((le, t, r + 1, d + 1))
im2.save('res.png')
