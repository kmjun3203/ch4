shopping = ['우유', '빵', '달걀']
shopping.append('사과')
shopping[1] = '치즈'
del shopping[0]
print(shopping)

scores = [60,75,80,90]
scores.append(100)
scores[2] = 85
scores.pop()
print(scores)

animals = ['강아지', '고양이', '토끼', '햄스터']
animals[1] = '고슴도치'
del animals[0]
animals.pop()
print(animals)