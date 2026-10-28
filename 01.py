prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def dis_calc(prices):
    return prices * .8


d = map(dis_calc , prices)

print(list(d))