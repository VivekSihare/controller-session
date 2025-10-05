// �� Direction buttons
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    player1.say("Up!")
    controller.moveSprite(player1)
})
// �� B button press event (jump)
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    music.jumpUp.play()
    player1.vy = -100
    player1.setBounceOnWall(true)
})
// �� A button press event (shoot)
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
    projectile = sprites.createProjectileFromSprite(img`
        . 2 . 
        2 4 2 
        . 2 . 
        `, player1, 150, 0)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    player1.say("Left!")
    controller.moveSprite(player1)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    player1.say("Right!")
    controller.moveSprite(player1)
})
// �� Released events
controller.A.onEvent(ControllerButtonEvent.Released, function () {
    player1.say("A released")
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    player1.say("Down!")
    controller.moveSprite(player1)
})
// �� Menu button (pause)
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    game.showLongText("Menu button pressed! Game Paused.", DialogLayout.Center)
})
// �� Released events
controller.B.onEvent(ControllerButtonEvent.Released, function () {
    player2.say("B released")
})
let projectile: Sprite = null
let player2: Sprite = null
let player1: Sprite = null
// Controller Features Demo - Microbit Arcade Python
// Create two player sprites
player1 = sprites.create(img`
    . . . . f f f f f . . . . . 
    . . . f 2 2 2 2 2 f . . . . 
    . . f 2 2 2 2 2 2 2 f . . . 
    . . f 2 f f f f f 2 f . . . 
    . . f 2 f . . . f 2 f . . . 
    . . f 2 f f f f f 2 f . . . 
    . . . f 2 2 2 2 2 f . . . . 
    . . . . f f f f f . . . . . 
    `, SpriteKind.Player)
player1.setPosition(50, 60)
player2 = sprites.create(img`
    . . . . f f f f f . . . . . 
    . . . f 5 5 5 5 5 f . . . . 
    . . f 5 5 5 5 5 5 5 f . . . 
    . . f 5 f f f f f 5 f . . . 
    . . f 5 f . . . f 5 f . . . 
    . . f 5 f f f f f 5 f . . . 
    . . . f 5 5 5 5 5 f . . . . 
    . . . . f f f f f . . . . . 
    `, SpriteKind.Player)
player2.setPosition(110, 60)
