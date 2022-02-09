#  Pygame Project Template
#  By Sepandi 
#  www.github.com/Sepandi 
import os
Template = open("game.py","w+")

Template.writelines("import pygame\n")
Template.writelines("from pygame import *\n")
Template.writelines("pygame.init()\n")
Template.writelines("#----Window-Setting---------------------\n")
Template.writelines("win = pygame.display.set_mode((800,600))\n")
Template.writelines("pygame.display.set_caption(\'hello\')\n")
Template.writelines("#--On-Load------------------------------\n")
Template.writelines("clock = pygame.time.clock()\n")
Template.writelines("\n")
Template.writelines("\n")
Template.writelines("\n")
Template.writelines("#--Updates\n")
Template.writelines("while True:\n")
Template.writelines("    for event in pygame.event.get():\n")
Template.writelines("        if event.type == QUIT:\n")
Template.writelines("            pygame.quit()\n")
Template.writelines("\n")
Template.writelines("   #--Draws\n")
Template.writelines("    win.fill([255, 255, 255])\n")
Template.writelines("    pygame.display.update()\n")
Template.writelines("    clock.tick(60)\n")
Template.close()
Assets = 'Data/Assets'
Sounds = 'Data/Sounds'
Fonts = 'Data/Fonts'
os.makedirs(Assets)   
os.makedirs(Sounds)
os.makedirs(Fonts)
