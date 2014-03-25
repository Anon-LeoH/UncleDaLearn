import math

def regularization(x):
    if not isinstance(x[0], list):
        mu = sum(x) / len(x)
        mx = max(x)
        rlt = [(item - mu) / mx for item in x]
        return rlt
    else:
        tmp = [ [] * len(x[0]) ]
        for item in x:
            for i in xrange(len(x)):
                tmp[i].append(item[i])
        for i in xrange(len(x)):
            tmp[i] = regularization(tmp[i])
            ptr = 0
            for item in x:
                item[i] = tmp[ptr]
                ptr += 1
        return x

        
