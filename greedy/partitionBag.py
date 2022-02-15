data = [(10,10),(15,12),(20,10),(25,8),(30,5)]

def get_max(datas,capacity):
    datas.sort(key = lambda x:x[1]/x[0], reverse=True)
    total = 0
    details = []

    for data in datas:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total += data[1]
            details.append([data[0],data[1],1])
        else:
            fraction = capacity/data[0]
            total += data[1]*fraction
            details.append([data[0],data[1],fraction])
            break
    return total,details

print(get_max(data,30))
