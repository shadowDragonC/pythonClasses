kilometers = int(input())
dayTime = input()
price = 0

if kilometers >= 100:
    if dayTime == 'day' or dayTime == 'night':
        price = 0.06 * kilometers
elif kilometers >= 20:
    if dayTime == 'day' or dayTime == 'night':
        price = 0.09 * kilometers
else:
    if dayTime == 'day':
        price =  0.70 + 0.79 * kilometers
    elif dayTime == 'night':
        price = 0.70 +  0.90 * kilometers

print(price)