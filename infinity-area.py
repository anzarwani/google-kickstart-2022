t = int(input())
import math
pii = math.pi

for case in range(t):
    areas = []
    r, a, b = list(map(int, input().split()))
    area = pii * r * r
    areas.append(area)
    while r > 0:
#        area = 0
        z = 1
        r = r*a
        area = pii * r * r
        areas.append(area)
        r = r//b
        if r < 0:
            break
        else:
            
            area = pii * r * r
            areas.append(area)
    total = sum(areas)
    print("Case #{0}: {1}".format(case+1, total))
    total = 0
    

    
    
    
