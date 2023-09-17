import math
import sys
import time


def prints(text, delay):
    for i in text:
        time.sleep(delay)
        sys.stdout.write(i)
        sys.stdout.flush()


def duskinit():
    prints("Initializing Dusk...", 0.1)
    time.sleep(0.5)


duskinit()
