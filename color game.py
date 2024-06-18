import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
player_size = 40
player_spaw_x = screen_width // 2
player_spaw_y = screen_height // 2
player_speed = 10
player_color = (255,255,255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("the box")

cubes = []

def generate_cube():
    cube_size = 40
    cube_x = random.randint(0, screen_width - cube_size)
    cube_y = random.randint(0, screen_height - cube_size)
    cube_color = random.choice([(255, 0, 0), (0, 0, 255), (0, 255, 0)])  # Red, blue, or green
    return cube_x, cube_y, cube_size, cube_color

for _ in range(3):
    cubes.append(generate_cube())


def get_random_color_name():
    colors = [
        ("Red", (255, 0, 0)),
        ("Green", (0, 255, 0)),
        ("Blue", (0, 0, 255)),
        ("Yellow", (255, 255, 0)),
        ("Cyan", (0, 255, 255)),
        ("Magenta", (255, 0, 255)),
        ("Orange", (255, 165, 0)),
        ("Purple", (128, 0, 128)),
        ("Pink", (255, 192, 203)),
        ("Brown", (165, 42, 42))
    ]
    return random.choice(colors)

# Generate a random color name and value at the start
color_name, color_value = get_random_color_name()
font = pygame.font.SysFont(None, 48)  # None means default font, 48 is the size
text_surface = font.render(color_name, True, color_value)


# Main game loop

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Change color on key press
            if event.key == pygame.K_SPACE:
                color_name, color_value = get_random_color_name()
                text_surface = font.render(color_name, True, color_value)
    player_rect = pygame.Rect(player_spaw_x, player_spaw_y, player_size, player_size)  
    for cube in cubes:
        cube_rect = pygame.Rect(cube[0], cube[1], cube[2], cube[2])
        if player_rect.colliderect(cube_rect):
            player_color = cube[3]  # Change player color
            cubes.remove(cube)  # Remove collided cube
            cubes.append(generate_cube())  # Generate new cube
            player_color = (0,100,0)
            

    # Fill the screen with a color (e.g., white)
    screen.fill((0, 0, 0))


    
    # Draw the text at the top center of the screen
    text_rect = text_surface.get_rect(center=(screen_width // 2, 50))
    screen.blit(text_surface, text_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_spaw_y -= player_speed
    if keys[pygame.K_s]:
        player_spaw_y += player_speed
    if keys[pygame.K_a]:
        player_spaw_x -= player_speed
    if keys[pygame.K_d]:
        player_spaw_x += player_speed

    pygame.draw.rect(screen, player_color, (player_spaw_x, player_spaw_y, player_size, player_size))
    for cube in cubes:
        pygame.draw.rect(screen, cube[3], (cube[0], cube[1], cube[2], cube[2]))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()