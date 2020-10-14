import time


def traffic_light(traffic_lights):
    current_state = []
    for light in traffic_lights:
        current_state.append(light)
    while current_state:
        for light in current_state:
            time.sleep(4)
            print(light)


traffic_light(['green', 'yellow', 'red'])
