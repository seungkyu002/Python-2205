exam = [99,78,100,91,81,85,54,100,71,50]
for i in range(len(exam)):
    if exam[i] + 5 <= 100:
        exam[i] += 5
    else:
        exam[i] = 100
print(exam)
