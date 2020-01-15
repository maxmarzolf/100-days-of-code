import csv
from collections import namedtuple
from collections import defaultdict
from collections import deque


CarModel = namedtuple('Owners', 'ID, FirstName, LastName, Make, Model')
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())

for owner in map(CarModel._make, csv.reader(open('/Users/max/PycharmProjects/100-days-of-code/days 4-6/mock_data.csv', 'rt'))):
    print(owner.FirstName, owner.Make, owner.Model)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield lines, previous_lines
        previous_lines.append(line)


if __name__=='__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print(pline, end='')
                print('-'*20)
