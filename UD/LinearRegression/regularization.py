import math

def regularization(x):
    if not isinstance(x[0], list):
        mu = float(sum(x)) / len(x)
        mx = float(max(x)) - min(x)
        if mx == 0:
            mx = 1
        rlt = [(item - mu) / mx for item in x]
        return ((mu, mx), rlt)
    else:
        tmp = []
        for i in xrange(len(x[0])):
            tmp.append([])
        print tmp
        for item in x:
            for i in xrange(len(item)):
                tmp[i].append(item[i])
        param = []
        for i in xrange(len(x[0])):
            tmp[i] = regularization(tmp[i])
            ptr = 0
            for item in x:
                item[i] = tmp[i][1][ptr]
                ptr += 1
            param.append(tmp[i][0])
        return (param, x)

        
