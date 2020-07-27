#Faça um programa que abra e reproduza o audio
#de um arquivo MP3.

import pygame
print('Música: Theory of a Deadman - Santa Monica')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()