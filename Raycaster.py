# import numpy as np
# from matplotlib import pyplot as plt
# import keyboard
#
# mapa = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1],
# ]
#
# posx, posy = (1, 1)
# exitx,  exity = (3, 3)
# rot = np.pi/4
#
# while True:
#     for i in range(60):
#         rot_1 = rot +np.deg2rad(1 - 30)

def fizzBuzz(n):
    for i in n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzBuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
if __name__ == "__main__":
    fizzBuzz(range(1, 16))
