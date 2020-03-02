import random
import statistics
import sys


def l1Cost(vec1, vec2):
	dist = 0.0
	for i in range(len(vec1)):
		dist += abs(vec1[i] - vec2[i])
	return dist


def optimalResult(budgets):
	result = []
	for i in range(len(budgets[0])):
		median = statistics.median([budget[i] for budget in budgets])
		result.append(median)
	return result


def sequentialBargaining(budgets, numIters):
	c = random.choice(budgets)
	for i in range(numIters):
		[u, v] = random.sample(budgets, 2)
		median = []
		for i in range(len(budgets[0])):
			median.append(statistics.median([u[i], v[i], c[i]]))
		c = median
	return c


def generateRandomBudget(d):
	# Select each dimension from a Gaussian to ensure uniform direction
    vec = [random.gauss(0, 1) for i in range(d)]
    mag = sum(x**2 for x in vec)**0.5
    return [x / mag for x in vec]


def main():
	print("Welcome to the sequential bargaining simulator!")
	print("Please input d followed by odd N, separated by a space.")

	d = None
	N = None
	numIters = None
	toPrompt = True
	if len(sys.argv) > 1:
		toPrompt = False
		[d, N, numIters] = [int(v) for v in sys.argv[1:]]

	if toPrompt:
		d, N = input().split(" ")
		d = int(d)
		N = int(N)
	budgets = [generateRandomBudget(d) for i in range(N)]

	print(f"\nThe {str(N)} randomly generated preferred budgets are:\n")

	for i, budget in enumerate(budgets):
		rounded = [" " + str(round(n, 3)) if n > 0 else str(round(n, 3)) for n in budget]
		print("\t".join(rounded))

	print("\nPlease input the number of iterations of sequential bargaining you would like to simulate.")

	if toPrompt:
		numIters = int(input())

	result = sequentialBargaining(budgets, numIters)

	print(f"\nThe result of {str(numIters)} iterations of sequential bargaining is:")
	print("\t".join([" " + str(round(v, 3)) if v > 0 else str(round(v, 3)) for v in result]))

	optimum = optimalResult(budgets)
	resultCost = 0.0
	optimumCost = 0.0
	for budget in budgets:
		resultCost += l1Cost(result, budget)
		optimumCost += l1Cost(optimum, budget)
	distortion = resultCost / optimumCost

	print("\nDistortion:")
	print(round(distortion, 3))


if __name__ == '__main__':
	main()