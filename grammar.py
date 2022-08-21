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
# 입력값에 맞는별 찍기
n = int(input().strip())
for i in range(n + 1):
    print('*' * i)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'


import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

print(list(itertools.product(iterable1, iterable2, iterable3)))

# [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'x', '3'), ('A', 'x', '4'), ('A', 'y', '1'), ('A', 'y', '2'), ('A', 'y', '3'), ('A', 'y', '4'), ('B', 'x', '1'), ('B', 'x', '2'), ('B', 'x', '3'), ('B', 'x', '4'), ('B', 'y', '1'), ('B', 'y', '2'), ('B', 'y', '3'), ('B', 'y', '4'), ('C', 'x', '1'), ('C', 'x', '2'), ('C', 'x', '3'), ('C', 'x', '4'), ('C', 'y', '1'), ('C', 'y', '2'), ('C', 'y', '3'), ('C', 'y', '4'), ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'x', '3'), ('D', 'x', '4'), ('D', 'y', '1'), ('D', 'y', '2'), ('D', 'y', '3'), ('D', 'y', '4')]
# > 

def solution(mylist):
    
    # answer = [] 
    # for i in mylist:
    #     answer += i
    answer = sum(mylist, [])
    
    return answer
    
    
pool = ['A', 'B', 'C']

list(map(''.join, itertools.permutations(%)))
print(list(map(''.join, itertools.permutations(%)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2))))    


['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
['AB', 'AC', 'BA', 'BC', 'CA', 'CB']

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1
print(answer[1]) # = 4
print(answer[3])  # = 3
# print(answer[100])

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0


# 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성
mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2) 
        
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]   

# 본 문제에서는 자연수 5개가 주어집니다.

# 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는 문제

import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')

#math.pow 함수란?  파이썬 제곱 함수 pow
# import math를 통해서 math 라이브러리를 임포트 
# 함수 모양 : math.pow(x, y)함수 설명 : math.pow(x, y) 함수는 x의 y 거듭제곱 (x의 y승)을 반환

# 파이썬 제곱근 함수 sqrt

# 함수 모양 : math.sqrt(x)함수 설명 : math.sqrt(x) 함수는 x의 제곱근을 반환합니다. (x에 루트를 씌운 값을 반환) 

#이 함수의 반환형 또한 float 타입입니다.2.math.sqrt(음수)가 들어오게 된다면 ERROR 가 발생합니다. 

# 두 변수의 값 바꾸기

#
a = 3
b ='abc'

a, b = b, a

# python 이진탐색

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 직접 반복문을 만들어, 이진 탐색 알고리즘을 구현합니다.

# 파이썬에서는
# 파이썬의 bisect.bisect 메소드를 사용하면 이 코드를 간략하게 만들 수 있습니다.

import bisect

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
