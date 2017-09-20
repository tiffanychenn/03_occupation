import csv
import random


file = "occupations.csv"
"""
file = open(file, 'r')
text = file.read()
file.close()
"""
reader = csv.reader(open(file))
#contents = csv.reader(file)

jobs = {}
#print reader
def createDict(csv):
        for rows in csv:
                if rows[0] == "Job Class" or rows[0] == "Total":
                        continue
                else:
                        jobs[rows[0]] = float(rows[1])

def randomJob(dict):
        randNum = float(random.randint(1,998)/10)
        for keys in dict.keys():
                randNum = randNum - dict[keys]
                if randNum < 0:
                        print keys, dict[keys]
                        return keys

createDict(reader)
randomJob(jobs)