
# 기존 코드 방식
count = fresh_fruit.get('사과', 0)
if count >= 4:
	make_cider(count)
else:
	out_of_stock()
	

# 파이썬 스타일 코드 방식
if (count := fresh_fruit.get('사과', 0)) >= 4:
	make_cider(count)
else:
	out_of_stock()
	
#최솟값을 저장하는 변수에 아주 큰 값을 할당해야 할 때

min_val = 99999
min_val > 100000000 # 

min_val = float('inf')
min_val > 10000000000

# 음수 기회를 붙일 수도 있다.
min_val = float('-inf')

# 파일 입출력 코드

with open('myfile.txt') as file:
	for line in file.readlines():
		print(line.strip().split('\t'))


# 5진법으로 적힌 문자열 '3212'를 10진법으로 바꾸기

answer = int('3212', 5)
print(answer)	