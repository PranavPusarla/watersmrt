import operator

#x is the predicted gallons per week and average gallons per week
def rank(x, avg):
    factor = x / avg
    return factor

#dictionary with key as appliance and value as factor
def sort(dict):
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
    return sorted_x

