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
		self.collided = False
		
# Decorative plants on the ground
class Plant:
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

knight_image = pygame.image.load("Assets/Exports/knight.png")

collision_img = pygame.image.load("Assets/Exports/collision.png")

flower_img = pygame.image.load("Assets/Exports/flower.png")



# Create goblin player and knight obstacles
player = Goblin(goblin_images, 120, 320)
knight_1 = Obstacle(knight_image, 1000, 368)
knight_2 = Obstacle(knight_image, 2000, 368)
knight_3 = Obstacle(knight_image, 2500, 368)
knights = [knight_1, knight_2, knight_3]

# Create decorative plants
flower = Plant(flower_img, 1100, 400)
plants = [flower,]

# Define starting conditions
text_font = pygame.font.Font("Assets/NESfont.ttf", 28)
WHITE = (255, 255, 255)
score_counter = 0
frame_counter = 0
speed = 5
collision = False
clock = pygame.time.Clock()
jumping = False
jump_counter = -4


# Main game loop
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
			# Player hits jump button
			if event.key == pygame.K_SPACE:
				jumping = True
					
		# Close game window when player closes window
		if event.type == pygame.QUIT:
			sys.exit()
	
	
	# Make goblin jump #
	# Track jump's intended path
	if jumping == True:
		if (-4 <= jump_counter <= 4):
			jump_counter += 0.2
			
	if jump_counter >= 4:
		jumping = False
		jump_counter = -4
	
	# Change goblin's height
	player.y = 128 + (12 * (jump_counter * jump_counter))
	
#	The above code implements this without using the for loop:
#	for x in range (-4, 5):
#		player.y = 128 + (12 * (x * x))

	
	# Render screen
	screen.blit(background_img, (0,0))
	screen.blit(player.current_image, (player.x, player.y))
	
	# Move enemy knights
	for knight in knights:
		knight.x -= speed
		
	# Check for collision beween goblin and knights
	for knight in knights:
		if (((abs((player.x) - knight.x) < 64)) and \
			((abs((player.y + 48) - knight.y)) < 8)):
				screen.blit(collision_img, (250, 200))
				score_counter = 0
				knight.collided = True
		
		# Reset knights at right side of screen after passing thru
		if knight.x <= -80:
			knight.x = 2500
			if knight.collided == False:
				score_counter += 1
			else:
				knight.collided = False
			print(score_counter)
		screen.blit(knight.image, (knight.x, knight.y))
	
#	# Move and draw decorative plants
#	for plant in plants:
#		plant.x -= speed
#		if plant.x <= -80:
#			plant.x = 1200
#		screen.blit(plant.image, (plant.x, plant.y))
				
	score_display = text_font.render("SCORE: " + str(score_counter), True, WHITE)
	screen.blit(score_display, (400, 200))
		
	pygame.display.flip()
	clock.tick(60)

# TODO:
# Randomize guard spawns.
# Fix running animation.
# Add more detail to the ground.

# Guard spawn randomization:
# Determine guard spawning location based on the spawn loc of prev guard.
# Distance from previous guard is randomized within a min and max value.
# The range of possible distance shrinks as the Score increases.
# Distance should always be at least 200 units.







