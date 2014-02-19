




def eight_queens(n):
	solutions = []
	rows = range(1, n+1)
	perm(n, rows, [], solutions, 1)
	new_solutions = not_under_attack(solutions)
	return len(new_solutions)

def perm(n, rows, perm_list, solutions, z):
	if len(perm_list) == n:
		solutions.append(perm_list)
		return
	for i, row in enumerate(rows):
		perm(n, rows[:i] + rows[i+1:], perm_list+[[z, row]], solutions, z+1)
	return solutions

def not_under_attack(solutions):
	new_solutions = []
	for solution in solutions:
		sol = True
		for i, pos in enumerate(solution):
			if sol == False:
				break
			for j in range(i+1, len(solution)):
				if abs(solution[j][0] - pos[0]) == abs(solution[j][1] - pos[1]):
					sol = False
					break		
		if sol == True:
			new_solutions.append(solution)
	return new_solutions		
	
print eight_queens(8)	
