def checkConsecutivePowers(num):
	sum = 0
	numList=list(str(num)) # разбиваем число
	for power,val in enumerate(numList): # присваем каждому числу индекс
		sum+=pow(int(val),power+1) # находим сумму
	if sum==num: # проверяем
		return True
	else:
		return False

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    specialNums=[] # пустой список для вывода
    for num in range(a,b+1): # последнее число включительно
    	if checkConsecutivePowers(num):
    		specialNums.append(num)
    return specialNums

print(sum_dig_pow(15,15))