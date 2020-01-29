colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple', 'pink', 'brown']
combos = perms = nums = 0

for a in colors:
    for b in colors:
        for c in colors:
            for d in colors:
                for e in colors:
                    print(a + ", " + b + ", " + c + ", " + d + ", " + e)
                    
for a in colors:
    for b in colors:
        if a is not b:
            for c in colors:
                if a is not c and b is not c:
                    for d in colors:
                        if a is not d and b is not d and c is not d:
                            for e in colors:
                                if a is not e and b is not e and c is not e and d is not e:
                                    combos += 1
                                    print(a + ", " + b + ", " + c + ", " + d + ", " + e)

for i in range(0, 5):
    for j in range(0, 5):
        if i is not j:
            for k in range(0, 5):
                if i is not k and j is not k:
                    for l in range(0, 5):
                        if i is not l and j is not l and k is not l:
                            for m in range(0, 5):
                                if i is not m and j is not m and k is not m and l is not m:
                                    nums += 1
                                    print(colors[i] + ", " + colors[j] + ", " + colors[k] + ", " + colors[l] + ", " + colors[m])

for i in range(0, len(colors)):
    for j in range(i + 1, len(colors)):
        for k in range(j + 1, len(colors)):
            for l in range(k + 1, len(colors)):
                for m in range(l + 1, len(colors)):
                    perms += 1
                    print(colors[i] + ", " + colors[j] + ", " + colors[k] + ", " + colors[l] + ", " + colors[m])

print(combos)
print(perms)
print(nums)