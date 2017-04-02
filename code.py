''' global variables '''

size = 8
initState = [0]*size
solution = []

''' start of func definitions '''

def suc(state):
	for i in range(size):
		if state[i] is 0:
			return [state[:i]+[x]+state[i+1:] for x in list(range(1,size+1))]

def checkViolation( state ):
	restrictedState = [x for x in state if x is not 0]
	if len(restrictedState) != len(set(restrictedState)):
		return True
	
	newElemIndex = len(restrictedState)-1
		
	return checkDiag(state, newElemIndex-1, restrictedState[newElemIndex]+1, restrictedState[newElemIndex]-1)

def checkDiag(state, elemNumber, checkNumber1, checkNumber2):
	if not(checkNumber1 > size or elemNumber < 0):
		if state[elemNumber] is checkNumber1:
			return True
			
	if not(checkNumber2 < 1 or elemNumber < 0):
		if state[elemNumber] is checkNumber2:
			return True	
		
	if checkNumber1 > size and checkNumber2 < 1 and elemNumber < 0:
		return False
	
	return checkDiag(state, elemNumber-1, checkNumber1+1, checkNumber2-1)

def solve(state):
	if suc(state) is not None:
		for x in suc(state):
			if not checkViolation(x):
				if len([y for y in x if y is not 0]) == size:
					solution.append(x)					
				else:
					solve(x)

''' end of func definitions '''

solve(initState)

print(len(solution))
