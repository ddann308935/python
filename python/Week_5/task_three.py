# Reads an unspecified number of scores and determines how many scores are
# above, equal and below the average
# negative number signify the end of input and max number of scores is 100

scores = []
i = 0

while i < 100:
    score = int(input("Enter the score: "))
    if score < 0:
        break
    scores.append(score)
    i += 1

total = sum(scores)

av = round(float(total / i), 2)
print("The average score is: ", av)

scores.sort()

print("Below average scores are: ")

j = 0
for k in scores:
    if scores[j] < av:
        print(scores[j])
        j += 1

print("Above average scores are: ")

l = 0
for m in scores:
    if scores[l] > av:
        print(scores[l])
        l += 1