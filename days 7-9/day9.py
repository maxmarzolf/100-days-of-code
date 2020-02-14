import requests

link = 'https://raw.githubusercontent.com/talkpython/100daysofcode-with-python-course/master/days/07-09-data-structures/code/data.py'
f = requests.get(link)
print(f.text)
