# importing libraries
import pygame
import time
import math
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

# Window size
window_x = 900
window_y = 600

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Car Simulation')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining colors
black = pygame.Color(0, 0, 0)

# initialize directional variables
car_speed = 0
unit_vec = 2
theta = 0
angle_turn = 4

# defining car default position
car_position = [(window_x/2), (window_y/2)]

# car graphic
car_body = pygame.image.load('car.png').convert_alpha()
car = pygame.transform.rotate(car_body, theta)
screen = pygame.display.set_mode([800,500])
# offset point car turns around (back wheels)
offset = -20
center_position_x = window_x/2
center_position_y = window_y/2
offset_vector_x = 0
offset_vector_y = 20

# defining sliders
speed_slider = Slider(screen, 30, 30, 200, 10, min=0, max=99, step=1, initial=0)
speed_val = TextBox(screen, 35, 42, 25, 25, fontSize=20)
speed_val.disable()  # Act as label instead of textbox
angle_slider = Slider(screen, 270, 30, 200, 10, min=-75, max=75, step=1, initial=0)
angle_val = TextBox(screen, 275, 42, 25, 25, fontSize=20)
angle_val.disable()

# setting default car direction forward
direction = 'FORWARD'
change_to = direction

key_events = {pygame.K_UP: 'FORWARD', 
			  pygame.K_DOWN: 'BACKWARD',
			  pygame.K_LEFT: 'LEFT',
			  pygame.K_RIGHT: 'RIGHT',
			  pygame.K_SPACE: 'STATIONARY'} 

# game over function
def game_over():
	time.sleep(0.5)
	pygame.quit()
	quit()

def rotate():
	car = pygame.transform.rotate(car_body, theta)

	# calculate new offset vector so car continues to turn around back wheels
	offset_vector_x = offset * math.sin(math.radians(theta))
	offset_vector_y = offset * math.cos(math.radians(theta))
	return car

# Main Function
while True:
	
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if key_events[event.key] == "STATIONARY":
				car_speed = 0
				print('stop')
			elif key_events[event.key] == change_to:
				car_speed += 5
				print('increasing the speed: ', car_speed)
				direction = change_to
			else:
				print('changing direction, speed = ', car_speed, ' direction = ', change_to)
				change_to = key_events[event.key]
			speed_slider.setValue(car_speed)
			angle_slider.setValue(theta)

	if change_to == 'LEFT' or change_to == 'RIGHT':
		if change_to == 'LEFT':
			theta += angle_turn
		else:
			theta -= angle_turn
		change_to = "NONE"
		car = rotate()
	
	theta = -1 * angle_slider.getValue()	
	if (angle_slider.getValue() > 0):
		change_to = 'LEFT'
		car = rotate()
	if (angle_slider.getValue() < 0):
		change_to = 'RIGHT'	
		car = rotate()

	# Moving the car
	if direction == 'FORWARD':
		center_position_x -= unit_vec * math.sin(math.radians(theta)) * car_speed/5
		center_position_y -= unit_vec * math.cos(math.radians(theta)) * car_speed/5
		car_position[1] = offset_vector_y + center_position_y
		car_position[0] = offset_vector_x + center_position_x
	if direction == 'BACKWARD':
		center_position_x += unit_vec * math.sin(math.radians(theta)) * car_speed/5
		center_position_y += unit_vec * math.cos(math.radians(theta)) * car_speed/5
		car_position[1] = offset_vector_y + center_position_y
		car_position[0] = offset_vector_x + center_position_x

	# render
	game_window.fill(black)
	screen.blit(car, (car_position[0], car_position[1]))
	pygame_widgets.update(pygame.event.get())
	speed_val.setText(speed_slider.getValue())
	angle_val.setText(angle_slider.getValue())
	car_speed = speed_slider.getValue() 
    
	pygame.display.flip()

	# Game Over conditions
	if car_position[0] < 0 or car_position[0] > window_x-10:
		game_over()
	if car_position[1] < 0 or car_position[1] > window_y-10:
		game_over()

	# Refresh game screen
	pygame.display.update()

	# screen refresh rate
	fps.tick(20)
