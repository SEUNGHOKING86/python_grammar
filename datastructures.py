from imghdr import what
from re import X
from tempfile import tempdir
from tkinter import N


-- 자료구조와 알고리즘 --  data structures

알고리즘(algorithm) = 어떤 문제를 해결하기 위한 절차, 방법, 명령어들의 집합(해결하고자 하는 문제에 따라 최적의 해법은 서로 다르다)

문자열(str) "This is a string"
리스트(list) [5, 9, 2, 7]
사전(dict) {'a': 6, 'b':4 }
순서쌍(tuple)
집합 (zip)



100개의 숫자 중
549를 찾아라.

입력으로 주어지는 리스트 x의 첫 원소와 마지막 원소의 합을 리턴하는 합

answer = x[0] + x.pop()
return answer


선형 배열 (Linear Arrays)

선형 배열 (Arrays) - 원소들을 순서대로 늘어놓은 것
리스트 (list)

데이터를 늘어놓은 모양새를 말할 때는 배열 (array), Python 의 데이터형을 가리킬 때에는 리스트 (list) 라는 용어를 사용
  
리스트 (list)
L = ['bob', 'cat', 'spam', 'progrmmers']

L.POP() == 'progrmmers' 

L = ['bob', 'cat', 'spam']
L.append('banana')
L = ['bob', 'cat', 'spam', 'banana']
L.index('spam') == spam 을 바로 찾음





 
리스트의 길이에 비례(선형시간)
O(n)
o(1)상수시간
리스트의 길이와 상관없음



원소 맨끝 덧붙이기 .append() 맨 마지막에 덫 붙여짐
원소 맨끝 하나를 꺼내기 .pop() 맨 나지막 원소를 하나 빼냄



ㅁ 원소 삽입하기 insert() 원소 삭제하기 del()
이런 연산들은 리스트의 길이가 길면 길수록 처리가 오래 걸리게 됨. 
구체적으로 말하면 리스트의 길이예 실행 시간이 비례. 
리스트 길이가 100 배가 되면, 위 연산들을 실행하는 데 걸리는 시간도 100 배 커짐

원소 탐색하기 .index()
L.POP(INDEX)

L.insert(3, 65)

3번째 원소를 삭제하라.
del(L[2])


 L = [20, 37, 65, 72, 91]
 L.POP(2)
 ==>65
 L = [20, 37, 72, 91]
 
 ㅁ 원소 탐색하기
 
 L = [20, 37, 72, 91]
 L.index(37)
 ==>1
 
 
 1 문제
 주어진 원소를 삽입할 위치를 찾는다.
 해당 위치에 원소를 삽입한다.
 insert()
 
def solution(L, x):
    index = len(L)
    for idx, value in enumerate(L):
        if value >= x:
            index = idx
            break
    L.insert(index, x)
    return L

def solution(L, x):
    L.append(x)
    L.sort()
    return L	

A = [i for i in range(len(L)) if x-L[i]>0]	

 2 문제 
 index() 매서드를 이용
 리스트 슬라이싱을 이용해서 반복해서 찾는다.
 
 



def solution(L, x):
    answer = [ idx for idx, value in enumerate(L) if value == x ]
    return answer if answer else [-1]

       
def solution(L, x):
	if x in L:
		return [i for i, v in enumerate(L) if v ==x]
	else:
		return [-1]

# 재귀 알고리즘  

# 재귀함수란(Recusive functions)?
# 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것

# 이진트리(이진탐색과 비슷한 구조)

# 자연수의 합 구하기 (재귀 함수를 호출할때는 반드시 종결 조건이 필요)
# 1 부터 n까지 모든 자연수의 합을 구하시오.


# recursive version
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

a = int(input("Number:"))
print(sum(a))

# iterative version (반복적인 버전)
def sum(n):
    s = 0
    while n >= 0:
        s += n
        n -= 1
        return s

# 효율적인 부분에서는 iterative version 낫다 (O(n)커질경우))


#n! 구하는 함수
def what(n):
    if n <= 1:
        return 1
    else:
        return n * what(n-1)


# 피보나치 수를 구하여라. recursive version, iterative version 2가지


# recursive version
def solution(x):
    if x < 2 :return x
    else:
        return solution(x-1) + solution(x-2)
# iterative version


def solution(x):
    answer = 0
    fa = 0
    fb = 1
    while x > 0:
        x -= 1
        fa, fb = fb, fa+fb
        answer = fa
    return answer


