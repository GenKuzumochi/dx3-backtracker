
l = [1] * 10 + [0] * 500

def next(l):
    l2 = [0] * 510
    for k in range(500):
        l2[k + 1] +=  l[k]
        l2[k + 2] +=  l[k]
        l2[k + 3] +=  l[k]
        l2[k + 4] +=  l[k]
        l2[k + 5] +=  l[k]
        l2[k + 6] +=  l[k]
        l2[k + 7] +=  l[k]
        l2[k + 8] +=  l[k]
        l2[k + 9] +=  l[k]
        l2[k + 10] += l[k]
    return l2
print("[[],")
for i in range(50):
    sigma = [0] * 510
    for k in range(501):
        sigma[500 - k] = sigma[500 - k + 1] + l[500 - k]
    print("[100,")
    for k in range(500):
        print( "{:.0f}".format(sigma[k] * 10000 / pow(10,i+1)) , ",")
    print("],")
    
    l = next(l)
print("]")