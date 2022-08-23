
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
	
