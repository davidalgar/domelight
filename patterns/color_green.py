#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

import pattern_utils
numLEDs = 512
client = pattern_utils.connectToServer()


black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs

# Fade to white
client.put_pixels(black)
client.put_pixels(black)
time.sleep(0.5)
color = [ (0, 255, 0) ] * numLEDs
client.put_pixels(color)
