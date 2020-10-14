from time import sleep
import itertools


colors = 'Red Green Yellow'.split()
rotation = itertools.cycle(colors)


def traffic_light(traffic_lights):
    current_state = []
    for light in traffic_lights:
        current_state.append(light)
    while current_state:
        for light in current_state:
            sleep(4)
            print(light)


def light_sequence(rotation):
    for color in rotation:
        if color == 'Yellow':
            print('Caution')
            sleep(3)
        elif color == 'Red':
            print('Stop')
            sleep(3)
        elif color == 'Green':
            print('Go')
            sleep(3)


# traffic_light(['green', 'yellow', 'red'])
light_sequence(rotation)
