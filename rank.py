import operator

#x is an array of the  predicted gallons per week
def rank(x):
    appliance_avg = {'toilet': 33, 'shower': 28, 'faucet': 26, 'hose': 60}
    factor = {}
    for key in appliance_avg:
        factor[key] = x / appliance_avg[key]
    return factor

#dictionary with key as appliance and value as factor
#returns keyword with highest factor
def sort(dict):
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
    return sorted_x[sorted_x.length-1]

