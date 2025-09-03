# 리스트에서 데이터 꺼내기

# 인덱스 번호를 사용해 값 꺼내기

lis = ['a', 'b', 'c']

# 첫 번째 요소 꺼내기
print(lis[0]) # a
print(lis[1]) # b
print(lis[2]) # c
# 마지막 요소
print(lis[-1]) # c

# 리스트 슬라이스
lis2 = ['a', 'b', 'c', 'd', 'e']
# 리스트[시작:끝]
# 끝은 포함 안됨
print(lis2[0:2]) #['a', 'b']
# 처음부터 끝까지
print(lis2[:2]) #['a', 'b']
# 2부터 마지막까지
print(lis2[2:]) #['c', 'd', 'e']