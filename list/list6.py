# 객체 비교하기 (is ==)

# 리스트 생성
a = [1,2,3]
# a를 복사
b = a
c = [1,2,3]
# is : 두 변수가 같은 객체를 가리키는지
print(a is b) #True
print(a is c) #False
# == : 두 변수가 같은 내용을 가지고 있는지
print(a == b) #True
print(a == c) #True