
# 4.8 자료형 : 변수(variable)
# 변수는 데이터가 저장되는 메모리 공간으로 볼 수 있습니다.
# a는 변수 이름으로써 2라는 정수형 객체가 저장된 메모리 위치를 가리키게 됩니다.
# 변수는 a가 '1이 저장된 메모리 공간을 a라고 이름을 붙입니다'의 의미가 됩니다.
# a라는 변수와 b라는 변수의 값이 1일 경우에 a,b 모두 1이라는 결과값이 저장된 공간과 같습니다.
# 다만, 변수의 이름을 지을 때, 주의사항이 있습니다.
# 1) 첫글자에 숫자가 오면 안됩니다.
# 특수문자는 언더바(_)만 사용해아 합니다. 이미 존재하는 함수나 모듈명으로 지어지면 안됩니다.
# 변수는 객체를 가리키는 것입니다. 바로 자료형을 포함한 파이썬에서 사용되는 모든 것을 뜻합니다.
# 변수는 메모리가 저장되는 공간에 객체를 대입하는 것이 아니라 객체를 가르키는 레퍼런스(reference)입니다. a = 2
# 변수를 만들 때에는 '='(assignment) 기호를 사용합니다.

a = 2
b = "python"
c = [1,2,3]

# a라는 변수는 2라는 정수형 객체를 가리킵니다.

a = 2
b = 2
# c = "str"
# a = 2를 입력하는 순간, 2라는 정수형 객체가 생성되며, 변수a는 2란 객체의 메모리를 가리킵니다.

print(a is b)
print(a==b)
True

# 변수 없애기 / del(변수)
a = 2
b = 2
del(a)
del(b)

# a, b 값을 지우는 부분
# 객체를 가르키는 값을 레퍼런스 카운트라고 합니다.
# 레퍼런스 카운트 값이 0이면 가르키는 변수가 존재하지 않을때를 말합니다. 그러므로 그 객체는 의미가 없으므로 메모리에서 사라집니다.

# 변수 만드는 방법
# 방법1) 터플로 a,b에 값을 대입할 수 있습니다.(터플은 괄호 생략이 가능합니다)
a, b = 'today', 'tomorrow'
(a, b) = ('today', 'tomorrow')
print(a, b) # 완료값 : today tomorrow
# 방법2) 리스트로 a,b에 값을 대입할 수 있습니다.
[a, b] = ['today', 'tomorrow']
print(a, b) # 완료값 : today tomorrow
# 방법3) 여러개의 변수에 같은 값을 대입할 수 있습니다.
a = b = 'today'
print(a,b) # 완료값 : today today

# 방법4) 변수 스왑하는 방법입니다.
a, b = 'today', 213
# 완료값 : today 213
# 오늘은 2월 13일입니다.
# 단, '0213'의 경우, 숫자 0으로 시작할 경우, 에러가 뜹니다.
print(a, b)

a = 2
b = 4
a, b = b, a
print(a)
print(b)

tmp = a  # tmp: 임시변수(원래값이 없어지니 바꿔줘야함)
a = b;
b = tmp; # 파이썬에서는 tmp라는 중재자 없이 가능합니다.

# 리스트 복사
a = [1, 2, 3]
b = a
c = a[:]
a[0] = 'Yesterday'
a[2] = 'Tomorrow'
# a[] 안에 들어간 위치의 값은 0부터 시작됩니다.
# a[0]은 숫자 1의 위치입니다.
# 그 값은 문자열로도 a[0]형태로 바꿀 수 있습니다.
print(a) # 완료값 : ['Yesterday', 2, 'Tomorrow']
print(b) # 완료값 : ['Yesterday', 2, 'Tomorrow']
print(c) # 완료값 : [1, 2, 3]
# ['',2,3] ''안에 들어가는 값의 경우, a[0(1,2)] 위치에 따라 값이 변합니다.


# b라는 변수에 a가 가리키는 리스트를 대입합니다.
# a리스트의 a[1]을 가리키는 값을 4로 바꾸었을 때, a리스트만 바뀌는 것이 아니라 b리스트도 함께 바뀌는 동일한 리스트를 가리키고 있는 변수입니다.
# 리스트 전체를 가리키는 [:]이용합니다.
# a리스트값을 변형하더라도 b리스트에는 영향을 끼치지 않음을 볼 수 있습니다.

# copy모듈을 이용하는 방법이 있습니다.

# 함수를 이용해 새로운 객체를 생성합니다.

from copy import copy # from 패키지, import 함수
a = copy
b = copy(a)
# b = copy(a) = a[:] 동일합니다

print(b is a) # 완료값 : True / b is a = True
True # 값들만 복사할 경우, 새로운 값만 복사됨
# Value값을 그대로 복사하겠다는 뜻임

# 응용심화
# 심화예제) 모린은 지갑에 현금이 10,000원 있습니다.
# 점심시간에 회사 사람들과 함께 식사장소로 이동하여 7,000원짜리 제육볶음을 1개 주문했습니다.
# 식사를 다 한 후에 개별적으로 주문한 메뉴 1개를 개별적으로 계산했습니다.
# 일하러 가는 길에 편의점에 들려 커피를 구입하려고 보니
# 정가 2,000원에서 프로모션으로 50% 할인된 가격인 1,000원에 구입했습니다.
# 현재 모린에게 남은 잔액은 얼마일까요?

money = 10000 # 총 금액
lunch = 7000 # 점심값
coffee = 2000 # 커피값
sale = 50/100.0 # 커피 50% 세일 프로모션 가격
today_price = lunch + (coffee * sale) # 현재 남은 잔액 = 점심값 + (커피값 * 50% 프로모션가)
A = money - today_price # 총 금액 - 오늘 사용한 금액
print(A) # 현재 남은 잔액
# 완료값 : 2000.0