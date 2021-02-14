distance = int(input("insert distance here"))
score = 0
if distance < 100000:
    percentage = distance/100000
    score = round(100-percentage*100, 0)
else:
    score = 0
print(int(score))
