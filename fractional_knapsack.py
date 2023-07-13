from sys import stdin

def optimal_value(capacity, weights, values):
    value = 0.
    price=[]
    n=len(weights)
    for i in range(n):
        price.append((values[i]/weights[i],weights[i]))
    price.sort()
    price.reverse()
    i=0
    while(capacity>0 and i<n):
        if capacity>price[i][1]:
            value+=price[i][0]*price[i][1]
            capacity-=price[i][1]
        else:
            value+=price[i][0]*capacity
            capacity=0
        i+=1
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
