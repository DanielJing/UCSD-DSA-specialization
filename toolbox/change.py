def change(money):
    coins = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        elif money >= 1:
            money -= 1
        coins = coins + 1
    return coins
if __name__ == '__main__':
    m = int(input())
    print(change(m))
