# hoppin_goblin.py
# Goblin themed clone of 'jumping t-rex game'.
# Author: Jackie B / TheDataElemental


import pygame
import random
import math
import sys


# Player 'Goblin' character
class Goblin:
	def __init__(self, image_list, x_start, y_start):
		# Image list for player animations
		self.image_list = image_list 
		self.current_image = image_list[0]
		# Player starting coordinates
		self.x = x_start
		self.y = y_start

# Knight obstacles for player to jump over	
class Obstacle:
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y
		

# Start pygame window
pygame.init()
screen = pygame.display.set_mode((960, 480), \
	pygame.HWSURFACE | pygame.DOUBLEBUF, vsync = 1)
pygame.display.set_caption("HOPPIN GOBLIN")
# CCC_icon = pygame.image.load("Assets/Exports/CCC.ico")
# pygame.display.set_icon(CCC_icon)



# Import assets
background_img = pygame.image.load\
	("Assets/Exports/background.png").convert()
	
goblin_img_1 = pygame.image.load\
	("Assets/Exports/hoppin_goblin_1.png")
goblin_img_2 = pygame.image.load\
	("Assets/Exports/hoppin_goblin_2.png")
goblin_img_3 = pygame.image.load\
	("Assets/Exports/hoppin_goblin_3.png")
goblin_img_4 = pygame.image.load\
	("Assets/Exports/hoppin_goblin_4.png")
	
goblin_images = [goblin_img_1, goblin_img_2, goblin_img_3, goblin_img_4]

knight_image = pygame.image.load\
	("Assets/Exports/knight.png")

# Create goblin player and knight obstacles
player = Goblin(goblin_images, 120, 320)
knight_1 = Obstacle(knight_image, 1000, 368)
knight_2 = Obstacle(knight_image, 1200, 368)
knight_3 = Obstacle(knight_image, 1400, 368)
knights = [knight_1, knight_2, knight_3]

# Define starting conditions
score_counter = 0
frame_counter = 0
speed = 5
collision = False
clock = pygame.time.Clock()
jumping = False
jump_counter = -4

while collision == False:
	# Tell pygame not to freeze
	pygame.event.pump()
	
	# Cycle through goblin / player animation
	frame_counter += 1
	if frame_counter == 2:
		player.current_image = goblin_images[0]
	
	if frame_counter == 4:
		player.current_image = goblin_images[1]
	
	if frame_counter == 6:
		player.current_image = goblin_images[2]
		
	if frame_counter == 8:
		player.current_image = goblin_images[3]
		frame_counter = 0
		
	# Watch for player input 
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				jumping = True
					
		# Close game window when player closes window
		if event.type == pygame.QUIT:
			sys.exit()
	
	
	# WIP zone
##############################################################

	# Make goblin jump
	
	print(jumping)
	print(jump_counter) 
	
	if jumping == True:
		if (-4 <= jump_counter <= 6):
			jump_counter += 1
	if jump_counter >= 5:
		jumping = False
		jump_counter = -4
	
	player.y = 192 + (8 * (jump_counter * jump_counter))
	
	# Implement this without using the for loop:
#	for x in range (-4, 5):
#		player.y = -(x * x) + 16
#		print(y)

#############################################################
	
	
	# Render screen
	screen.blit(background_img, (0,0))
	screen.blit(player.current_image, (player.x, player.y))
	for knight in knights:
		knight.x -= speed
		if knight.x <= -80:
			knight.x = 1000
		screen.blit(knight.image, (knight.x, knight.y))
	pygame.display.flip()
	clock.tick(60)


