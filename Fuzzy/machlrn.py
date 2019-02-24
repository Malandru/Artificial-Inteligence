from myreader import getInfo, getJSONs
from converter import NAME, REPEATS, to_json
import numpy

def get_column(cindx, matrix):
    return [row[cindx] for row in matrix]

def delete_column(cindx, matrix):
    row = 0
    while row < len(matrix):
        beg = matrix[row][:cindx]
        end = matrix[row][cindx + 1:]
        matrix[row] = beg + end
        row += 1

def get_nums(properties, answ, x):
    num =[]
    for prop in properties:
        name = str(prop[NAME])
        if name in x:
            num.append(prop[answ])
    return num

def main():
    #-----READ DATA-----#
    file = 'docu.csv'
    fields, data = getInfo(file)
    #-----Getting the answers column-----#
    lci = len(fields) - 1 #last column index
    all_answ = get_column(lci, data) #the whole column of answers
    t_answ = len(all_answ)
    delete_column(lci, data)
    answers = list(set(all_answ)) #posible answers
    #-----Formatting the data to jsons-----#
    properties = to_json(data, all_answ, answers)
    x = ['Sunny', 'Hot', 'Normal', 'False']
    #-----Getting the each answer probability-----
    all_prob = []
    for answ in answers:
        ta = all_answ.count(answ)
        nums = get_nums(properties, answ, x)
        num = numpy.prod(nums) * ta
        den = t_answ * (ta ** len(nums))
        prob_answ = float(num) / den
        all_prob.append(prob_answ)
    #-----Getting the 100%-----
    one = sum(all_prob)
    #print one
    for i in range(len(answers)):
        msg = 'P(' + answers[i] + ' '+ fields[-1] + ') ='
        print msg, all_prob[i] / one

main()