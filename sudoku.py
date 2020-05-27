import pyjokes
from time import time
#import time
#from random import choice
#from random import randint

class grid():
	def __init__(self,inp):
		self.rc = [[0 for col in range(int(inp))]for row in range(int(inp))]

def go_for_round(inp):

#	print(' I am in the function')
	a = 'd'
	b = 'n'

	for i in range(int(inp)):

		for j in range(int(inp)):

			if int(inp_array.rc[i][j]) == 0: 
				a = 'n'
				tmp_list=list(range(1,int(inp) + 1))

				for k in range(int(inp)):
					if (str(inp_array.rc[i][k]) > ' ') and (int(inp_array.rc[i][k]) in tmp_list): tmp_list.remove(int(inp_array.rc[i][k]))

				for k in range(int(inp)):
					if (str(inp_array.rc[k][j]) > ' ') and (int(inp_array.rc[k][j]) in tmp_list): tmp_list.remove(int(inp_array.rc[k][j]))

				if (int(inp) == 9) and (0 <= i <= 2) and (0 <= j <= 2):
					for x in range(0,3):
						for y in range(0,3):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (3 <= i <= 5) and (0 <= j <= 2):
					for x in range(3,6):
						for y in range(0,3):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (6 <= i <= 8) and (0 <= j <= 2):
					for x in range(6,9):
						for y in range(0,3):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (0 <= i <= 2) and (3 <= j <= 5):
					for x in range(0,3):
						for y in range(3,6):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (3 <= i <= 5) and (3 <= j <= 5):
					for x in range(3,6):
						for y in range(3,6):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (6 <= i <= 8) and (3 <= j <= 5):
					for x in range(6,9):
						for y in range(3,6):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (0 <= i <= 2) and (6 <= j <= 8):
					for x in range(0,3):
						for y in range(6,9):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (3 <= i <= 5) and (6 <= j <= 8):
					for x in range(3,6):
						for y in range(6,9):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (6 <= i <= 8) and (6 <= j <= 8):
					for x in range(6,9):
						for y in range(6,9):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in tmp_list): tmp_list.remove(int(inp_array.rc[x][y]))

				if len(tmp_list) == 1: inp_array.rc[i][j] = tmp_list[0]	
				if len(tmp_list) == 1: b='c'
	return a + b

def go_harder(inp):
	
	pos_num_list = [[' ' for col in range(int(inp))]for row in range(int(inp))]


	a = 'd'
	b = 'n'

	for i in range(int(inp)):
		for j in range(int(inp)):

			if int(inp_array.rc[i][j]) == 0: 
				a = 'n'
				pos_num_list[i][j] = list(range(1,int(inp) + 1))

				for k in range(int(inp)):
					if (str(inp_array.rc[i][k]) > ' ') and (int(inp_array.rc[i][k]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[i][k]))

				for k in range(int(inp)):
					if (str(inp_array.rc[k][j]) > ' ') and (int(inp_array.rc[k][j]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[k][j]))

				if (int(inp) == 9) and (0 <= i <= 2) and (0 <= j <= 2):
					for x in range(0,3):
						for y in range(0,3):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (3 <= i <= 5) and (0 <= j <= 2):
					for x in range(3,6):
						for y in range(0,3):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (6 <= i <= 8) and (0 <= j <= 2):
					for x in range(6,9):
						for y in range(0,3):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (0 <= i <= 2) and (3 <= j <= 5):
					for x in range(0,3):
						for y in range(3,6):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (3 <= i <= 5) and (3 <= j <= 5):
					for x in range(3,6):
						for y in range(3,6):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (6 <= i <= 8) and (3 <= j <= 5):
					for x in range(6,9):
						for y in range(3,6):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (0 <= i <= 2) and (6 <= j <= 8):
					for x in range(0,3):
						for y in range(6,9):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (3 <= i <= 5) and (6 <= j <= 8):
					for x in range(3,6):
						for y in range(6,9):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))
				if (int(inp) == 9) and (6 <= i <= 8) and (6 <= j <= 8):
					for x in range(6,9):
						for y in range(6,9):
							if (str(inp_array.rc[x][y]) > ' ') and (int(inp_array.rc[x][y]) in pos_num_list[i][j]): pos_num_list[i][j].remove(int(inp_array.rc[x][y]))

	for i in range(int(inp)):
		for j in range(int(inp)):

			if int(inp_array.rc[i][j]) == 0: 

				box_list = []
				set_list = []

				if (int(inp) == 9) and (0 <= i <= 2) and (0 <= j <= 2):
					for x in range(0,3):
						for y in range(0,3):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(0,3):
								for y in range(0,3):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (3 <= i <= 5) and (0 <= j <= 2):
					for x in range(3,6):
						for y in range(0,3):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(3,6):
								for y in range(0,3):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (6 <= i <= 8) and (0 <= j <= 2):
					for x in range(6,9):
						for y in range(0,3):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(6,9):
								for y in range(0,3):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (0 <= i <= 2) and (3 <= j <= 5):
					for x in range(0,3):
						for y in range(3,6):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(0,3):
								for y in range(3,6):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (3 <= i <= 5) and (3 <= j <= 5):
					for x in range(3,6):
						for y in range(3,6):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(3,6):
								for y in range(3,6):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (6 <= i <= 8) and (3 <= j <= 5):
					for x in range(6,9):
						for y in range(3,6):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(6,9):
								for y in range(3,6):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (0 <= i <= 2) and (6 <= j <= 8):
					for x in range(0,3):
						for y in range(6,9):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(0,3):
								for y in range(6,9):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (3 <= i <= 5) and (6 <= j <= 8):
					for x in range(3,6):
						for y in range(6,9):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(3,6):
								for y in range(6,9):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'

				if (int(inp) == 9) and (6 <= i <= 8) and (6 <= j <= 8):
					for x in range(6,9):
						for y in range(6,9):
							if (int(inp_array.rc[x][y]) == 0):
								for ele in pos_num_list[x][y]:
									box_list.append(ele)
				
					set_list = list(dict.fromkeys(box_list))
					for ele in set_list:
						if box_list.count(ele) == 1:
							for x in range(6,9):
								for y in range(6,9):
									if (int(inp_array.rc[x][y]) == 0) and (ele in pos_num_list[x][y]): 
										inp_array.rc[x][y] = ele
										b='c'
	return a + b






print(pyjokes.get_joke())

inp = 9
easy = 0
hard = 0
inp_array = grid(inp)

print('Enter the grid (empty as 0) :')
for i in range(inp):
	inp_data = input()
	for j in range(inp):
		inp_array.rc[i][j] = inp_data[j]

t1 = time()

for i in range(100):
	result = go_for_round(inp)
	easy += 1
	if result[0] == 'd': break
	if result[1] == 'n': break


for i in range(100):
	result = go_harder(inp)
	hard += 1
	if result[0] == 'd': break
	if result[1] == 'n': break

t2 = time()

print()

print('The Result is :')
for i in range(int(inp)):
	for j in range(int(inp)):
		print(f'{inp_array.rc[i][j]}',end='|')
		if j in [2,5,8]:
			print(' ', end=' ')

	if i in [2,5,8]:
		print() 
		print('------  ------  ------')
	else: 
		print()
print(f'It took {easy} Easy run and {hard} Hard run and took {(t2-t1)} sec')
