import pygame, sys, glob

class Tool():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 900))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 20, False, False)
        self.stack = [self.loop]
        self.inputs = {"up": False, "down": False, "left": False, "right": False, "enter": False}
        self.imgs = []
        self.images = {}
        for img in glob.glob("assets\\*.png"):
            image = pygame.image.load(img).convert_alpha()
            self.imgs.append(img)
            self.images[img] = image
        self.index = 0
        self.xoff = 1
        self.yoff = 1

    def eventManager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.inputs["up"] = True
                elif event.key == pygame.K_DOWN:
                    self.inputs["down"] = True
                elif event.key == pygame.K_LEFT:
                    self.inputs["left"] = True
                elif event.key == pygame.K_RIGHT:
                    self.inputs["right"] = True
                elif event.key == pygame.K_RETURN:
                    self.inputs["enter"] = True

    def loop(self):
        if self.inputs["up"]:
            self.inputs["up"] = False
            self.index += 1
            if self.index >= len(self.imgs):
                self.index = 0
        elif self.inputs["down"]:
            self.inputs["down"] = False
            self.index -= 1
            if self.index < 0:
                self.index = len(self.imgs) - 1
        elif self.inputs["enter"]:
            self.inputs["enter"] = False
            self.stack.append(self.build)

        self.screen.fill((0, 0, 0))
        text = self.font.render(self.imgs[self.index], False, (255, 255, 255))
        self.screen.blit(text, (0, 0))
        img = self.images[self.imgs[self.index]]
        self.screen.blit(pygame.transform.scale(img, (img.get_width() * 8, img.get_height() * 8)), (0, 32))

    def build(self):
        self.screen.fill((0, 0, 0))
        if self.inputs["up"]:
            self.inputs["up"] = False
            self.yoff -= 1
        elif self.inputs["down"]:
            self.inputs["down"] = False
            self.yoff += 1
        elif self.inputs["left"]:
            self.inputs["left"] = False
            self.xoff -= 1
        elif self.inputs["right"]:
            self.inputs["right"] = False
            self.xoff += 1
        elif self.inputs["enter"]:
            self.inputs["enter"] = False
            self.writeFile()
        xtext = self.font.render("X offset: " + str(self.xoff), False, (255, 255, 255))
        ytext = self.font.render("Y offset: " + str(self.yoff), False, (255, 255, 255))
        self.screen.blit(xtext, (0, 0))
        self.screen.blit(ytext, (0, 32))
        img = self.images[self.imgs[self.index]]
        self.screen.blit(pygame.transform.scale(img, (img.get_width() * 8, img.get_height() * 8)), (0, 64))

    def writeFile(self):
        img = self.images[self.imgs[self.index]]
        colors = {}
        for x in range(img.get_width()):
            if x + self.xoff < 0 or x + self.xoff > 123:
                continue
            for y in range(img.get_height()):
                if y + self.yoff < 0 or y + self.yoff > 92:
                    continue
                c = img.get_at((x, y))
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
                    colors[col] = [(x + self.xoff, y + self.yoff)]
                else:
                    colors[col].append((x + self.xoff, y + self.yoff))
        
        f = open(self.imgs[self.index] + ".txt", "w+")

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

        pygame.quit()
        sys.exit()

    def run(self):
        self.eventManager()
        self.stack[-1]()
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    tool = Tool()
    while True:
        tool.run()
