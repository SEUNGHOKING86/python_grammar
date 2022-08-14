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

import re
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


# 2022-08-15
# *solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성

#1 번째 방법
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
        return answer

#2 번쨰 방법 zip한수를 사용
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
        return answer

mylist = [83, 48, 13, 4, 71, 11]
print(solution(mylist))

# *문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수

def solution(mylist):
    
    list2 = list(map(int, mylist))
    return list2
mylist = ['1', '100', '33']
print(solution(mylist))
                

# * mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴

# 1번재 방법
def solution(mylist):
    answer = ''
    for i in mylist:
        answer += i
    return answer

# 2번째 방법
def solution(mylist):
    return ''.join(mylist)


# *'abc', 'abcabc', 'abcabcabc', 'abcabcabcabc ...' 과 같이 'abc'가 n번 반복되는 문자열 만들기

n = 'abc'
answer = 'abc' * n

# 입력값에 맞는 별 찍기
n = int(input().strip())
for i in range(n + 1):
    print('*' * i)