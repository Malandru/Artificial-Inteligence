import csv
import json

def readCSV(file, doc):
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            doc.append(row)

def getFields(doc):
    fields = doc[0]
    doc.remove(fields)
    return fields

def parse(data):
    parsed = []
    for row in data:
        newrow = []
        for elem in row:
            try:
                newrow.append(float(elem))
            except ValueError:
                newrow.append(elem)
        parsed.append(newrow)
    return parsed

def getInfo(file):
    doc = []
    readCSV(file, doc)
    fields = getFields(doc)
    return fields, doc

def parse(string, value):
    parsed = []
    string = str(string)
    beg, end = 0, -1
    while end != 0:
        end = string.find(value, beg) + 1
        parsed.append(string[beg:end])
        beg = end + 2
    return parsed

def getJSONs(file):
    csvfile = open (file,'r')
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        data.append(row)
    result = []
    for elem in data:
        elem = json.dumps(elem)
        JSON = json.loads(elem)
        result.append(JSON)
    return result