import pygame
import math
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = WIDTH // 2 - 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Analog Clock')

def draw_hand(angle, length, color, width):
    end_x = CENTER[0] + length * math.cos(math.radians(angle))
    end_y = CENTER[1] + length * math.sin(math.radians(angle))  # Notice the addition instead of subtraction
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)

def draw_clock():
    # Draw clock face
    pygame.draw.circle(screen, BLACK, CENTER, RADIUS, 5)
    for i in range(12):
        angle = math.radians(360 / 12 * i)
        x = CENTER[0] + (RADIUS - 20) * math.cos(angle)
        y = CENTER[1] + (RADIUS - 20) * math.sin(angle)  # Notice the addition instead of subtraction
        pygame.draw.circle(screen, BLACK, (int(x), int(y)), 5)

def get_time_angles():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    second_angle = 360 / 60 * seconds
    minute_angle = 360 / 60 * minutes + second_angle / 60
    hour_angle = 360 / 12 * hours + minute_angle / 12

    return hour_angle, minute_angle, second_angle

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_clock()

    hour_angle, minute_angle, second_angle = get_time_angles()

    # Adjust angles to start from the top (12 o'clock) and move clockwise
    draw_hand((270 + hour_angle) % 360, RADIUS - 80, BLACK, 8)   # Hour hand
    draw_hand((270 + minute_angle) % 360, RADIUS - 50, BLACK, 6) # Minute hand
    draw_hand((270 + second_angle) % 360, RADIUS - 30, RED, 2)   # Second hand

    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
