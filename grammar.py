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


