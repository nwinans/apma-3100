combos = perms = 0
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple', 'brown', 'black', 'white']

for i in range(0, len(colors)):
    for j in range(i + 1, len(colors)):
        for k in range(j + 1, len(colors)):
            for l in range(k + 1, len(colors)):
                for m in range(l + 1, len(colors)):
                    combos = combos + 1

for a in colors:
    for b in colors:
        if a is not b:
            for c in colors:
                if a is not c and b is not c:
                    for d in colors:
                        if a is not d and b is not d and c is not d:
                            for e in colors:
                                if a is not e and b is not e and c is not e and d is not e:
                                    perms = perms + 1

print("There are " + str(combos) + " combinations of the colors over 5 trains")
print("There are " + str(perms) + " permutations of the colors over 5 trains")