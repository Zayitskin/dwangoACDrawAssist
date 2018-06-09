import pygame, sys, glob

class Tool:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1108, 829))
        self.stack = [self.quit, self.loop, self.preloop]
        self.files = []
        for path in glob.glob("*.txt"):
            self.files.append(open(path))

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def run(self):
        self.eventHandler()
        self.stack[-1]()
        pygame.display.flip()

    def quit(self):
        for file in self.files:
            file.close()
            pygame.quit()
            sys.exit()

    def preloop(self):
        for x in range(0, 123 * 9, 9):
            pygame.draw.line(self.screen, (128, 128, 128), (x, 0), (x, 92 * 9))
        for y in range(0, 92 * 9, 9):
            pygame.draw.line(self.screen, (128, 128, 128), (0, y), (123 * 9, y))
        pygame.draw.line(self.screen, (128, 128, 128), (1107, 0), (1107, 828))
        pygame.draw.line(self.screen, (128, 128, 128), (0, 828), (1107, 828))
        self.draw()
        self.stack.pop()

    def fillBox(self, x, y, color):
        pygame.draw.rect(self.screen, color,
                         (1 + (x - 1) * 9, 1 + (y - 1) * 9, 8, 8))

    def draw(self):
        for file in self.files:
            for line in file:
                if line == "\n":
                    continue
                line = line.split(" ")
                color = pygame.color.Color(line[0])
                locs = line[1]
                locs = locs.split(";")
                for loc in locs:
                    loc = loc.split(",")
                    self.fillBox(int(loc[0]), int(loc[1]), color)

    def loop(self):
        pass

tool = Tool()
while True:
    tool.run()
