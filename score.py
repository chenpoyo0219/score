scores = input().split()
nums = [int(s) for s in scores]   # 把字串轉成整數列表

count = 0
total = 0

for s in nums:
    total += s
    if s < 60:
        count += 1

average = total / len(nums)

print("不及格人數:", count)
print("最大值:", max(nums))
print("最小值:", min(nums))
print("平均分數:", average)