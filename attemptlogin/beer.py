#!/bin/usr/env python3
import time

print("*"*50)

dumb_song = input("Do you want to hear the most annoying song ever? (Y/N): ")

if dumb_song.lower() == "y":
    print("Sweet, here it is!")
    time.sleep(3)
else:
    print("Too bad!")
    time.sleep(3)


for num_bottles in range(99, 0, -1):
    if num_bottles == 1:
        bottle_word = "bottle"
    else:
        bottle_word = "bottles"

    print(f"{num_bottles} {bottle_word} of beer on the wall,")
    time.sleep(1)
    print(f"{num_bottles} {bottle_word} of beer,")
    time.sleep(1)
    print(f"You take one down, pass it around,")
    time.sleep(1)

    if num_bottles - 1 == 1:
        next_bottle_word = "bottle"
    else:
        next_bottle_word = "bottles"

    if num_bottles - 1 == 0:
        print("No more brottles of beer on the wall")
    else:
        print(f"{num_bottles - 1} {next_bottle_word} of beer on the wall!")

print("*"*50)
