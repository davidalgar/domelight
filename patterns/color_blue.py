#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white


import time
import pattern_utils

numLEDs = 512
client = pattern_utils.connectToServer()

black = [ (0,0,0) ] * numLEDs
color = [ (0, 0, 255) ] * numLEDs
# Fade to white
client.put_pixels(black)
client.put_pixels(black)
time.sleep(0.5)
color = [ (0, 0, 255) ] * numLEDs
client.put_pixels(color)
