scores = input().split()

count = 0

for s in scores:
    if int(s) < 60:
        count=count+1

print(count)