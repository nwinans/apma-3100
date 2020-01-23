count = 0
classes = ['calculus', 'physics', 'orgo', 'history', 'literature', 'french', 'astronomy']

for a in classes:
    for b in classes:
        if a is not b:
            for c in classes:
                if a is not c and b is not c:
                    for d in classes: 
                        if a is not d and b is not d and c is not d:
                            count = count + 1

print("There are " + count + " class schedule possibilities")