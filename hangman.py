import random

def func(ls, ls1, x):
	idx = ls.index(x)
	ls1[idx] = x

word = ['king', 'code', 'monkey', 'computer']
sel_word = random.choice(word)
ls = list(sel_word)
base = []
base1 = 0
count = 10
for i in range(len(sel_word)):
	base.append('x')
print(base)
while True:
	if base1 == len(ls):
		print('You Won')
		break
	elif count == 0:
		print('You lose')
		break
	try1 = input('Enter the letter: ')
	if try1 in ls:
		func(ls, base, try1)
		print(base)
		print('Correct')
		base1 += 1
	else:
		count -= 1
		print('Wrong')