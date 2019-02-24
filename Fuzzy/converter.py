import json

NAME = 'name'
REPEATS = 'repeats'

def to_json(data, all_answ, answers):
    parsed = []
    index = 0
    for row in data:
        for elem in row:
            new_elem = find(elem, all_answ[index], answers, parsed)
            if not new_elem in parsed:
                parsed.append(new_elem)
        index += 1
    return parsed

def find(prop, answ, answers, List):
    prop, answ = str(prop), str(answ)
    for elem in List:
        try:
            x = str(elem[NAME])
            if prop == x:
                elem[REPEATS] += 1
                elem[answ] += 1
                return elem
        except (KeyError, TypeError) as error:
            pass
    new_json = loads(prop, answ, answers)
    #print new_json
    return json.loads(new_json)

def loads(prop, answ, answers):
    jprop = '{"' + NAME + '": "' + prop + '"'
    jrepe = ', "' + REPEATS + '": 1'
    jansw = ''
    for a in answers:
        x = '0'
        if a == answ:
            x = '1'
        jansw += ', "' + a + '": ' + x
    return str(jprop + jrepe + jansw + '}')

"""
def locate(elem, objs):
    elem = str(elem)
    for obj in objs:
        try:
            if str(obj["property"]) == elem:
                obj["repeats"] += 1
                return obj
        except (KeyError, TypeError) as error:
            pass
    new_elem = '{"property": "' + elem + '", "repeats": 1}'
    new_elem = json.loads(new_elem)
    return new_elem
"""