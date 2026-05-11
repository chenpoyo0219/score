

scores = input().split()

count = 0
total = 0

for s in scores:
    score = int(s)
    total += score
    if score < 60:
        count += 1

average = total / len(scores)

print("不及格人數:", count)
print("平均分數:", average)