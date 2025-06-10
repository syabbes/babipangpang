import RPi.GPIO as GPIO
import time
from cs50 import SQL
import pygame

db = cs50.SQL("sqlite:///highscores.db")
GPIO.setmode(GPIO.BCM)  # Use bcm

#initialiseer pygame
pygame.init()
screen = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("Hello, Pygame")
# main

# cleanup pins
GPIO.cleanup()