#!/usr/bin/env python

# Burn-in test: Keep LEDs at full brightness most of the time, but dim periodically
# so it's clear when there's a problem.

import opc, time, math

import pattern_utils

def main(parseOpts = False, looplimit=10):
    numLEDs = 512
    client = pattern_utils.connectToServer()


    t = 0

    for i in range(looplimit):
        t += 0.4
        brightness = int(min(1, 1.25 + math.sin(t)) * 255)
        frame = [ (brightness, brightness, brightness) ] * numLEDs
        client.put_pixels(frame)
        time.sleep(0.05)


if __name__ == "__main__":
    while True:
        main(True, 100000)