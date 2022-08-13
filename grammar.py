###2022-08-12###

mylist = [[1, 2], [3, 4], [5]]

def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer


# map(function, iterable)
# map 함수 이용
# def add_one(n):
#     return n + 1
#result2 = list(map(add_one, myList))  # map반환을 list 로 변환


def solution2(mylist):
   
    return list(map(len , mylist))

print(solution(mylist))
print(solution2(mylist))


# 숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력

a, b = map(int, input().strip().split(' '))

# 몫은 a // b
# 나머지 a%b
print(a//b, a%b)
print(divmod(a,b))




# n진법으로 표기된 string을 10진법 숫자로 변환하기 - int 함수
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)

answer = int(num, base)

'가나다라               ' # 좌측정렬
'               가나다라' # 우측 정렬
'       가나다라        ' # 가운데 정렬

s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

import string 

num = int(input().strip())
# 입력값 num이 0 소문자 , 1이면 대문자 출력

import string
if num == 0:
    result = string.ascii_lowercase
else :
    result = string.ascii_uppercase
print(result)    

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789


# list 정렬하기

list1 = [3, 2, 5, 1]
list2 = sorted(list1)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))


# new_list = list(map(list, zip(*mylist)))
print(new_list)

animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer)