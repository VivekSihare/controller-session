# Lesson 1: Controller

Welcome to your second Micro:Bit Arcade Project!
In this lession, you'll be creating a simple program that shows the Controller for sprites and buttons

---

## Learning Objectives
By the end of this activity, you will be able to:
- ✅ Use all controller buttons (A, B, D-pad, Menu)
- ✅ Move sprites with the controller
- ✅ Create button press and release events
- ✅ Make sounds and projectiles
- ✅ Understand event-based coding

## Materials Needed
- Devices (computers or tablets) with internet access
- MakeCode Arcade account (no sign-in required)
- Optional: Micro:bit Arcade-compatible device for uploading

## Steps

### 1. Start a New Project
  Go to https://arcade.makecode.com/ in your browser
  
### 2. Start a New Project
  - Click on New Project
  - Name it something like "Controller Feature Demo"
    
### 3. Create the Player Sprites
  - From Sprites drawer → drag out “set mySprite to sprite of kind Player”
  - Rename it to player1
  - Click the image box to draw your own character (use color 2, e.g. red)
  - Add another “set mySprite to sprite of kind Player” block
  - Rename it to player2
  - Draw a second character (use a different color like blue)
  - From Sprites → set mySprite position to x y
  - For player1: set to (50, 60)
  - For player2: set to (110, 60)
  
### 4. Enable Movement
 - From Controller, drag out “move mySprite with buttons vx vy”
 - Select player1, set both speeds to (100, 100)
 - (Optional) To allow player2 to move:
 - Use controller player2 move mySprite with buttons vx vy
   
### 5. A Button - Shoot
- From Controller, drag “on A button pressed” event.
- Inside it: From Music, add “play sound pew pew”.
- From Sprites, add “projectile from mySprite with vx vy”.
- Choose player1.
- Draw a small bullet image.
- Set vx = 150, vy = 0.

### 6. B Button - Jump
  - From Controller, drag “on B button pressed”.
  - Inside it: From Music, add “play sound jump up”.
  - From Sprites, add “set mySprite vy to -100”
  - Add another block: “set mySprite bounce on wall to true”
  - Choose player1.

### 7. Direction Buttons — Say Messages
  - For each direction (Up, Down, Left, Right):
  - From Controller, drag “on up button pressed”
  - Inside it, from Sprites, use “mySprite say [text]”
  - Set text to “Up!”
  - Choose player1
  - Repeat for:
  - Left → “Left!”
  - Right → “Right!”
  - Down → “Down!”

### 8. Released Events
  - From Controller, drag “on A button released”
  - Inside, add player1 say "A released"
  - From Controller, drag “on B button released”
  - Inside, add player2 say "B released"

### 9. Menu Button — Pause Message
  - From Controller, drag “on menu button pressed”
  - Inside, from Game, use “show long text [text] in [layout]”
  - Text: "Menu button pressed! Game Paused."
  - Layout: center

### 10. Optional — Change Background When Any Button is Pressed
  - From Game, drag “on game update”
  - Inside: Add an if condition block
  - From Controller, drag “any button is pressed” into the if-test
  - Inside the if, use scene → set background color to blue
  - In the else, set background color to another color (like purple)

### 11. Download Your Program
  - Click **Download**
  - Select hardware as **Kitronik Arcade for micro:bit**
  - Save the .hex file
  - Drag the '.hex' file onto MICROBIT Drive
