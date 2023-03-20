n = int(input())

one = 0
two = 0
tre = 0
four = 0
zero = 0

for i in range(n):
    p = []
    k = input().split()
    for i in k:
        p.append(int(i))
    if (p[0]) or (p[1]) != 0:

        if (p[0] < 0) and (p[1] > 0):
            two += 1
        if (p[0] > 0) and (p[1] > 0):
            one += 1
        if (p[0] < 0) and (p[1] < 0):
            tre += 1
        if (p[0] > 0) and (p[1] < 0):
            four += 1
    else:
        zero += 1

print('Первая четверть:', one)
print('Вторая четверть:', two)
print('Третья четверть:', tre)
print('Четвертая четверть:', four)
