def fibonacci_number(n):
    if n <= 1:
        return n
    
    f = [0] * (n+1)
    f[0], f[1] = 0, 1
    
    for i in range(2, n+1):
        f[i] = f[i-2] + f[i-1]
    return f[i]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
