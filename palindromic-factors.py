t = int(input())
count = 0
for case in range(t):
    num = int(input())
    
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    for num in factors:
        num = str(num)
        if str(num) == str(num[::-1]):
            count += 1
    print("Case #{0}: {1}".format(case+1, count))
    count = 0
