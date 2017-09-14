import csv
import random

file = "occupations.csv"
file = open(file, 'r')
contents = csv.reader(file)

jobs = {}

for i in contents[1:len(contents) - 1]:
    jobs[i[0]] = float(i[1])

def randomoccupation():
    keys = jobs.keys().sort()

randomoccupation()