from tkinter import W
import pygame

pygame.int()


pygame.display.set_mode((480, 580))
pygame.display.set_caption("STRANGER SHOOTING GAME")

running = True
while running:
    for event in pygame.event_get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()