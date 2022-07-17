total = 0
for i in range(1000):
    total += i
    if total > 3000:
        break # break를 감싸고 있는 반복문 한개만 강제로 종료
print(total)