




def eight_queens(n):
	solutions = []
	rows = range(1, n+1)
	perm(n, rows, [], solutions, 1)
	return solutions

def perm(n, rows, perm_list, solutions, z):
	if len(perm_list) == n:
		if not_under_attack(perm_list):
			solutions.append(perm_list)
		return
	for i, row in enumerate(rows):
		perm(n, rows[:i] + rows[i+1:], perm_list+[[z, row]], solutions, z+1)
	return solutions

def not_under_attack(solution):
	for i, pos in enumerate(solution):
		for j in range(i+1, len(solution)):
			if abs(solution[j][0] - pos[0]) == abs(solution[j][1] - pos[1]):
				return False		
	return True
	
print eight_queens(8)	
