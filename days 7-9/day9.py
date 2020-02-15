# TODO: format
import requests
import data
import os


url = 'https://raw.githubusercontent.com/talkpython/100daysofcode-with-python-course/master/days/07-09-data-structures/code/data.py'
r = requests.get(url)
with open('/Users/max/PycharmProjects/100-days-of-code/days 7-9/data.py', 'w') as file:
    if os.stat("/Users/max/PycharmProjects/100-days-of-code/days 7-9/data.py").st_size == 0:
        file.write(r.text)
state_dictionary = data.us_state_abbrev
state_list = data.states_list
state_index = 0
for key in state_dictionary:
    state_index += 1
    if state_index == 10:
        print(key)