import pygame, sys


def writeFile(image, xoff, yoff):
    name = image
    image = pygame.image.load(image)
    colors = {}
    for x in range(image.get_width()):
        if x + xoff < 0 or x + xoff > 123:
            continue
        for y in range(img.get_height()):
            if y + yoff < 0 or y + yoff > 92:
                continue
            c = image.get_at((x, y))
            if c.a != 255:
                continue
            r = str(hex(c.r)[2:])
            if len(r) == 1:
                r = "0" + r
            g = str(hex(c.g)[2:])
            if len(g) == 1:
                g = "0" + g
            b = str(hex(c.b)[2:])
            if len(b) == 1:
                b = "0" + b
            col = "#" + r + g + b
            if col not in colors:
                colors[col] = [(x + xoff, y + yoff)]
            else:
                colors[col].append((x + xoff, y + yoff))

    f = open(name + ".txt", "w+")

    for key in colors.keys():
        s = key + " "
        for pix in colors[key]:
            s += str(pix[0]) + "," + str(pix[1]) + ";"
            if len(s) > 485 and pix != colors[key][-1]:
                if s.endswith(";"):
                    s = s[:-1]
                f.write(s)
                f.write("\n\n")
                s = key + " "
        if s.endswith(";"):
            s = s[:-1]
        f.write(s)
        f.write("\n\n")
    f.close()


if len(sys.argv) <= 1:
    print('Format: "png" x-offset y-offset')
    sys.exit()

pygame.init()
data = sys.argv[1:]
for i in range(0, len(data), 3):
    img = data[i]
    xOff, yOff = data[i + 1], data[i + 2]
    writeFile(img, xOff, yOff)
