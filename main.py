import pyxel


class App:

    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        pyxel.load
        
        
        

        # Set the initial position of the square
        self.x = 75
        self.y = 55
        self.score = 0

        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        # Simple interaction: Increase score when square reaches top-left corner
        
        #if self.x < 10 and self.y < 10:
            #self.score += 1

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        if abs(self.sprite_x - self.x) < 10 and abs(self.sprite_y - self.y) < 10:
            self.score = self.score + 1

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)
        

        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # Draws a 16x16 sprite from bank 0
        pyxel.blt(self.sprite_x, self.sprite_y, 1, 0, 0, 16, 16, 0)  # Draws a 16x16 sprite from bank 0




        # Draw a square (color 9)
        # pyxel.rect(self.x, self.y, 10, 10, 9)

        # Draw the moving sprite (color 11)
        #pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
        if self.score >= 5:
            pyxel.text(50, 50, "You’re doing great!", 8)
            
# Increase score if square touches the sprite
def update(self):
    if abs(self.x - self.sprite_x) < 10 and abs(self.y - self.sprite_y) < 10:
        self.score += 1  



# Run the game
App()
