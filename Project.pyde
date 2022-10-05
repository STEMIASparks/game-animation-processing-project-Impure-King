# Overview: This game is similar to sinous and the goal is to avoid the ever spawning dots, while getting a high score through the time you survive. (There will be a timer.)

# Variables and lists:
x,y,r, num, loo = 0, 0, 0, 0, 0
time = 1000
lisx = []
lisy = []
lisr = []
lis = []
score = 0
siz = 600

def setup():
    global siz
    size(siz, siz)
    frameRate(4)

def draw():
    global time, x, y, z, num, loo, score, siz
    
    loo = int(random(1, 10)) # Number of circles to spawn for the next round
    
    background(0) # covers the unneeded circles before the loop.
    
    
    fill(200, 200, 200)
    # This loop will spawn multiple circles with different colors and different shapes
    
    lisx, lisy, lisr = [], [], []
    
    for i in range(loo):
    # The coordinates are kept random to spawn the circles randomly.
        r = int(random(siz/10, siz/5))
        x = int(random(1, siz))
        y = int(random(1, siz))
        circle(x, y, r) # Keeping the variables to easily manipulate the circle coordinates.
        lisx.append(x)
        lisy.append(y)
        lisr.append(r)
    
    for i in range(loo):
        ra = lisr[i]/2
        x0 = lisx[i] - ra
        x1 = lisx[i] + ra
        y0 = lisy[i] - ra
        y1 = lisy[i] + ra
        # if x0 <= mouseX <= x1 and y0 <= mouseY <= y1:
            textSize(32)
            text("GAME OVER", siz/2 - 100, siz/2 - 32)
            fill(255, 0, 0)
            textSize(32)
            text(score, siz/2 - 50, siz/2 + 10)
            fill(0, 255, 0)
            circle(x0 + ra, y0 + ra, 2 * ra)
            frameRate(0)
        else:
            score += 1
    print(score)
    cir = createShape(ELLIPSE, 5, 5, 5, 5)
    cir.setFill(color(120, 50, 30))
    cir.setStroke(False)
    shape(cir, mouseX, mouseY)
