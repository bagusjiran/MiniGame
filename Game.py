import turtle

# Mengatur layar
screen = turtle.Screen()
screen.title("Mario Bros-like Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Membuat pemain
player = turtle.Turtle()
player.shape("square")
player.color("red")
player.penup()
player.speed(0)
player.setposition(-350, -250)

# Membuat musuh
enemies = []
for i in range(3):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("green")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(350 - i * 200, -250)
    enemies.append(enemy)

# Membuat koin
coins = []
for i in range(5):
    coin = turtle.Turtle()
    coin.shape("circle")
    coin.color("yellow")
    coin.penup()
    coin.speed(0)
    coin.setposition(-200 + i * 100, -250)
    coins.append(coin)

# Menampilkan hati dan skor
lives_display = turtle.Turtle()
lives_display.hideturtle()
lives_display.penup()
lives_display.setposition(-380, 260)
lives_display.write("Hati: 3", font=("Arial", 16, "normal"))

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.setposition(280, 260)
score_display.write("Skor: 0", font=("Arial", 16, "normal"))

# Gerakan pemain
def move_left():
    x = player.xcor()
    x -= 20
    if x < -380:
        x = -380
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 380:
        x = 380
    player.setx(x)

# Lompat
is_jumping = False
jump_count = 10

def jump():
    global is_jumping, jump_count
    if not is_jumping:
        is_jumping = True
        jump_count = 10

# Pengaturan tombol
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(jump, "space")

# Gerakan musuh
def move_enemies():
    for enemy in enemies:
        x = enemy.xcor()
        if x > 350:
            enemy.setheading(180)
        elif x < -350:
            enemy.setheading(0)
        enemy.forward(5)

# Deteksi tabrakan
def check_collisions():
    global lives, score
    for enemy in enemies:
        if player.distance(enemy) < 20:
            lives -= 1
            player.setposition(-350, -250)
    to_remove = []
    for coin in coins:
        if player.distance(coin) < 20:
            score += 1
            coin.hideturtle()
            to_remove.append(coin)
    for coin in to_remove:
        coins.remove(coin)

# Loop permainan
lives = 3
score = 0

def game_loop():
    global lives, score, is_jumping, jump_count
    if lives > 0:
        move_enemies()
        if is_jumping:
            if jump_count >= -10:
                neg = 1 if jump_count > 0 else -1
                player.sety(player.ycor() + (jump_count ** 2) * 0.5 * neg)
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10
        check_collisions()
        # Memperbarui tampilan
        lives_display.clear()
        lives_display.write(f"Hati: {lives}", font=("Arial", 16, "normal"))
        score_display.clear()
        score_display.write(f"Skor: {score}", font=("Arial", 16, "normal"))
        screen.ontimer(game_loop, 50)
    else:
        # Game over
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.setposition(0, 0)
        game_over.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        game_over.setposition(0, -50)
        game_over.write(f"Skor Akhir: {score}", align="center", font=("Arial", 16, "normal"))

# Memulai loop permainan
game_loop()

screen.mainloop()