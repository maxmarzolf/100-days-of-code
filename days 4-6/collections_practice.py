import csv
from collections import namedtuple
from collections import defaultdict
from collections import deque


CarModel = namedtuple('Owners', 'ID, FirstName, LastName, Make, Model')

for owner in map(CarModel._make, csv.reader(open('/Users/max/PycharmProjects/100-days-of-code/days 4-6/mock_data.csv', 'rt'))):
    print(owner.FirstName, owner.Make, owner.Model)
