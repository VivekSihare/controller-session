# �� Direction buttons

def on_up_pressed():
    player1.say("Up!")
    controller.move_sprite(player1)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

# �� B button press event (jump)

def on_b_pressed():
    music.jump_up.play()
    player1.vy = -100
    player1.set_bounce_on_wall(True)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# �� A button press event (shoot)

def on_a_pressed():
    global projectile
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.IN_BACKGROUND)
    projectile = sprites.create_projectile_from_sprite(img("""
            . 2 .
            2 4 2
            . 2 .
            """),
        player1,
        150,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    player1.say("Left!")
    controller.move_sprite(player1)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    player1.say("Right!")
    controller.move_sprite(player1)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

# �� Released events

def on_a_released():
    player1.say("A released")
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_down_pressed():
    player1.say("Down!")
    controller.move_sprite(player1)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

# �� Menu button (pause)

def on_menu_pressed():
    game.show_long_text("Menu button pressed! Game Paused.", DialogLayout.CENTER)
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

# �� Released events

def on_b_released():
    player2.say("B released")
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

projectile: Sprite = None
player2: Sprite = None
player1: Sprite = None
# Controller Features Demo - Microbit Arcade Python
# Create two player sprites
player1 = sprites.create(img("""
        . . . . f f f f f . . . . .
        . . . f 2 2 2 2 2 f . . . .
        . . f 2 2 2 2 2 2 2 f . . .
        . . f 2 f f f f f 2 f . . .
        . . f 2 f . . . f 2 f . . .
        . . f 2 f f f f f 2 f . . .
        . . . f 2 2 2 2 2 f . . . .
        . . . . f f f f f . . . . .
        """),
    SpriteKind.player)
player1.set_position(50, 60)
player2 = sprites.create(img("""
        . . . . f f f f f . . . . .
        . . . f 5 5 5 5 5 f . . . .
        . . f 5 5 5 5 5 5 5 f . . .
        . . f 5 f f f f f 5 f . . .
        . . f 5 f . . . f 5 f . . .
        . . f 5 f f f f f 5 f . . .
        . . . f 5 5 5 5 5 f . . . .
        . . . . f f f f f . . . . .
        """),
    SpriteKind.player)
player2.set_position(110, 60)