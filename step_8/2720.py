t = int(input())

for _ in range(t):
    c = int(input())

    quarters = c // 25
    c %= 25
    dimes = c // 10
    c %= 10
    nickels = c // 5
    pennies = c % 5
    
    print(quarters, dimes, nickels, pennies)
