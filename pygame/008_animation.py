# -*- coding: utf-8 -*-
"""
step008.py
animation & spritesheet
url: http://thepythongamebook.com/en:part2:pygame:step008
author: horst.jens@spielend-programmieren.at

spritesheet from
http://www.flyingyogi.com
"""
import pygame
import random
import os
pygame.init()
screen=pygame.display.set_mode((800,480)) # try out larger values and see what happens !
screenrect = screen.get_rect()
background = pygame.Surface((screen.get_size()))
backgroundrect = background.get_rect()
background.fill((255,255,255)) # fill white
background = background.convert()
screen.blit(background,(0,0))
# mypicture = pygame.image.load("picturefile.jpg") # simple method if picture in same folder
folder = "data" # replace with "." if pictures lay in the same folder as program
spritesheet = pygame.image.load(os.path.join(folder, "char9.bmp")).convert() # all in one line
lions = [] # a list for the lion images
# the spritesheet has lions, 128 x 64 pixels
for nbr in range(1,5,1): # first line contains 4 picutres of lions
   lions.append(spritesheet.subsurface((127*(nbr-1),64,127,127)))
for nbr in range(5,7,1): # second line contains 2 pictures of lions
   lions.append(spritesheet.subsurface((127*(nbr-5),262-64,127,127)))
print "len:",len(lions)

for nbr in range(len(lions)):
   lions[nbr].set_colorkey((0,0,0)) # black transparent
   lions[nbr] = lions[nbr].convert_alpha()
   print "converted nbr", nbr

for nbr in range(len(lions)):
    screen.blit(lions[nbr], (nbr*127, 0))  #blit the ball surface on the screen (on top of background)
    print "blitted nbr", nbr

screen.blit(lions[nbr], (nbr*127, 0))  #blit the ball surface on the screen (on top of background)
#screen.blit(lions[1], (x, 
clock = pygame.time.Clock()        #create pygame clock object
mainloop = True
FPS = 60                           # desired max. framerate in frames per second. 
playtime = 0
cycletime = 0 
newnr = 0 # index of the first lionimage to display
oldnr = 0 # needed to compare if image has changed
interval = .15 # how long one single images should be displayed in seconds 
while mainloop:
    milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
    playtime += seconds
    cycletime += seconds
    if cycletime > interval:
        cycletime = 0
        newnr += 1
    picnr = int(newnr % 5) # the remainder of a division by 5, because 6 pictures are present (0...5)
    mypicture = lions[picnr]
    if newnr > oldnr:
        #print "change to picture nr %i" % picnr
        # clean dirty rec (a bit larger than original rect):
        screen.blit(background.subsurface((300,300,128,66)),(300,300)) 
        # blit new lion picture:
        screen.blit(mypicture, (300,300)) 
    oldnr = newnr # save oldnr 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC
 
    pygame.display.set_caption("[FPS]: %.2f picture: %i" % (clock.get_fps(), picnr))
    #this would repaint the whole screen (secure, but slow)
    #screen.blit(background, (0,0))     #draw background on screen (overwriting all)

    pygame.display.flip()          # flip the screen 30 times a second
print "This 'game' was played for %.2f seconds" % playtime