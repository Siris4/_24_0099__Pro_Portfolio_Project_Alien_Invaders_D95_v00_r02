import tkinter as tk

# Set up the main window
root = tk.Tk()
root.title("Space Invaders")
root.resizable(False, False)
root.geometry("800x600")

# Create the canvas for the game
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

# Spaceship properties
spaceship_width = 40
spaceship_height = 20
spaceship_x = 380  # starting x position of the spaceship
spaceship_y = 550  # fixed y position (near the bottom of the window)
spaceship_speed = 20

# Create the spaceship
spaceship = canvas.create_rectangle(spaceship_x, spaceship_y, spaceship_x + spaceship_width,
                                    spaceship_y + spaceship_height, fill="green")

# Variable to keep track of the active bullet
active_bullet = None


# Function to move the spaceship left
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(spaceship)
    if x1 > 0:
        canvas.move(spaceship, -spaceship_speed, 0)


# Function to move the spaceship right
def move_right(event):
    x1, y1, x2, y2 = canvas.coords(spaceship)
    if x2 < 800:  # Make sure spaceship doesn't move past the right edge of the screen
        canvas.move(spaceship, spaceship_speed, 0)


# Function to fire a bullet (only one active bullet at a time)
def fire_bullet(event):
    global active_bullet
    # If there's already an active bullet, do nothing
    if active_bullet is not None:
        return

    # Create a new bullet
    x1, y1, x2, y2 = canvas.coords(spaceship)
    active_bullet = canvas.create_rectangle((x1 + x2) / 2 - 2, y1 - 10, (x1 + x2) / 2 + 2, y1, fill="red")
    move_bullet()


# Function to move the active bullet
def move_bullet():
    global active_bullet
    if active_bullet is not None:
        canvas.move(active_bullet, 0, -10)
        bullet_coords = canvas.coords(active_bullet)

        # If the bullet goes off-screen, remove it
        if bullet_coords[1] < 0:
            canvas.delete(active_bullet)
            active_bullet = None  # Reset the active bullet variable

    # Continue moving the bullet until it goes off-screen or is deleted
    if active_bullet is not None:
        root.after(50, move_bullet)


# Bind key events to spaceship movement and firing
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", fire_bullet)

# Start the game loop
root.mainloop()
