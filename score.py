

scores = input().split()

count = 0

nums = [int(s) for s in scores]   # 把字串轉成整數列表

for s in nums:
    if s < 60:
        count += 1

print("不及格人數:", count)
print("最大值:", max(nums))
print("最小值:", min(nums))
=======
total = 0

for s in scores:
    score = int(s)
    total += score
    if score < 60:
        count += 1

average = total / len(scores)

print("不及格人數:", count)
print("平均分數:", average)

