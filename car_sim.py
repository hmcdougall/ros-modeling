# importing libraries
import pygame
import time
import math

car_speed = 15
unit_vec = 2
theta = 0
angle_turn = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Car Simulation')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining car default position
car_position = [100, 50]

# car graphic
car_body = pygame.image.load('car.png').convert_alpha()
screen = pygame.display.set_mode([800,500])
# pygame.display.flip()

# setting default car direction towards right
direction = 'STATIONARY'
change_to = direction

key_events = {pygame.K_UP: 'UP', 
			  pygame.K_DOWN: 'DOWN',
			  pygame.K_LEFT: 'LEFT',
			  pygame.K_RIGHT: 'RIGHT',
			  pygame.K_SPACE: 'STATIONARY'}

# game over function
def game_over():
	# after 1 second, quit the program
	time.sleep(1)
	pygame.quit()
	quit()

# Main Function
while True:
	
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if key_events[event.key] == "STATIONARY":
				car_speed = 0
				print('stop')
			elif key_events[event.key] == change_to:
				car_speed += 15
				print('increasing the speed')
			else:
				car_speed = 15
				print('changing direction')
				change_to = key_events[event.key]		

	# If two keys pressed simultaneously
	# we don't want car to move into two
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the car
	if direction == 'UP':
		car_position[1] -= unit_vec * math.cos(math.radians(theta))
		car_position[0] += unit_vec * math.sin(math.radians(theta))
	if direction == 'DOWN':
		car_position[1] += unit_vec * math.cos(math.radians(theta))
		car_position[0] += unit_vec * math.sin(math.radians(theta))
	if direction == 'LEFT':
		theta -= angle_turn
	if direction == 'RIGHT':
		theta += angle_turn
	# if direction == 'STATIONARY':
	# 	car_position[0] += 0
	# 	car_position[1] +=0

	game_window.fill(black)
	screen.blit(car_body, (car_position[0],car_position[1]))
    
	pygame.display.flip()

	# Game Over conditions
	if car_position[0] < 0 or car_position[0] > window_x-10:
		game_over()
	if car_position[1] < 0 or car_position[1] > window_y-10:
		game_over()

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second / Refresh Rate
	fps.tick(car_speed)
