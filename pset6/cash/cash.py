from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)
coins = 0

denominations = [25, 10, 5, 1]

for denom in denominations:
        coins += cents // denom
        cents %= denom


"""
OPTION 2
denominations = [25, 10, 5, 1]

for denom in denominations:
    while cents >= denom:
        cents -= denom
        coins += 1

"""

"""
OPTION 1
while cents >= 25:
    cents -= 25
    coins += 1

while cents >= 10:
    cents -= 10
    coins += 1

while cents >= 5:
    cents -= 5
    coins += 1

while cents >= 1:
    cents -= 1
    coins += 1
"""

print(coins)