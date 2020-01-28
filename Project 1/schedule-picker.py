orders = 0
books = ['calculus', 'physics', 'chemistry', 'history', 'literature','french', 'astronomy']

for i in range(0, len(books)):
    for j in range(i + 1, len(books)):
        for k in range(j + 1, len(books)):
            for l in range(k + 1, len(books)):
                for m in range(l + 1, len(books)):
                    orders += 1

print("There are " + str(orders) + " unique book orders")

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

print("There are " + str(count) + " class schedule possibilities")