# NOTE: RETURNING MULTIPLE VALUES AND COLLECTING SINGLE VARIABLE

def get_sum_avg(x):
    s = 0
    for e in x:
        s = s+e
    return s, s/len(x)


y = [10, 20, 30, 40]
output = get_sum_avg(y)
print(output)

 27  class_examples/Functions_examples/fun12.py 
