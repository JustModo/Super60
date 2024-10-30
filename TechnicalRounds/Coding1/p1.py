a = []

increment = 1
series = 1
for i in range(100):
    a.append(series*-1 if series % 2 == 0 else series)
    series += increment
    increment += 2

print(*a, sep=" ")
print(f"Sum {sum(a)}\n")

b = []

for ele in a:
    for digit in str(abs(ele)):
        if int(digit) == 0:
            b.append(ele)
            break

print(*b, sep=" ")
print(f"Sum {sum(b)}\n")

c = []

for ele in a:
    prev = -1
    f = True
    for digit in str(abs(ele)):
        if int(digit) <= prev:
            f = False
            break
        prev = int(digit)
    if (f):
        c.append(ele)

print(*c, sep=" ")
print(f"Sum {sum(c)}\n")
