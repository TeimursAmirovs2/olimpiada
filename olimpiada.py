import random

n = 200000
numbers = [0] * n

for i in range(n):
    numbers[i] = random.randint(-1000000, 1000000)

limit = min(n, 3000)
count = {}

for i in range(limit):
    x = numbers[i]

    if x not in count:
        count[x] = 0

    count[x] += 1

answer = None
repeated = None

for x in count:
    if count[x] >= 4:
        answer = [x, x, x, x]
        break

    if count[x] >= 2:
        if repeated is not None:
            answer = [repeated, x, repeated, x]
            break

        repeated = x

if answer is None:
    different = list(count)
    sums = {}

    if repeated is not None:
        sums[repeated + repeated] = repeated

    for i in range(len(different)):
        for j in range(i + 1, len(different)):
            x = different[i]
            y = different[j]
            s = x + y

            if s in sums:
                a = sums[s]
                b = s - a
                answer = [a, b, x, y]
                break

            sums[s] = x

        if answer is not None:
            break

if answer is None:
    print(0)
else:
    print(1)
    print(answer[0], answer[1], answer[2], answer[3])