k = input('Введите числа через пробел').split()
p = []
count = 0
for i in k:
    p.append(int(i))
for j in range(1, len(p)):
    if p[j] > p[j - 1]:
        count += 1

print(count)

