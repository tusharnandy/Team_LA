import random
from matplotlib import pyplot as plt
import numpy as np
import scipy.signal

iterations = []

population = []
time = []
# making a matrix for population and another one to keep track of the time

for i in range(200):
    population.append([0]*200)
    time.append([0]*200)
# a population of 40,000 = 200X200

c_rand, r_rand = [list(random.sample(range(200), 10))]*2

for i in range(10):
    population[r_rand[i]][c_rand[i]] = 1
# randomly assigning '1' to 10 elements

iteration = 1

while True:
    all_done = True  # The loop shall run until all elements are infected once

    r1 = [] # this keeps track of the row no. of infected people
    c1 = [] # this keeps track of the column no. of infected people

    for i in range(200):  ## extracting 1s and zeros
        for j in range(200):
            if population[i][j] == 0:
                all_done = False
            elif population[i][j] == 1: # we take note of the infected ones
                c1.append(j)
                r1.append(i)

    if all_done:
        break

    for k in range(len(r1)): # this loop assigns 1 to the nearest neighbors

        for q in [r1[k]-1, r1[k]+1]:
            for f in list(range(c1[k]-1, c1[k]+2)):
                if q < 200 and f < 200 and population[q][f]==0:
                    population[q][f] = 1

        for p in [c1[k]-1, c1[k]+1]:
            if p < 200 and population[r1[k]][p]==0:
                population[r1[k]][p] = 1

    r_swap = random.sample(list(range(200)), 20)
    c_swap = random.sample(list(range(200)), 20)

    for i in range(10): ## swapping 10 elements by another 10 elements
        population[r_swap[i]][c_swap[i]], population[r_swap[i+10]][c_swap[i+ 10 ]] = population[r_swap[i+10]][c_swap[i+10]], population[r_swap[i]][c_swap[i]]

    for i in range(200): # Now this is an important loop
        for j in range(200):
            if population[i][j] ==1: # I am selectively keeping track of the infected people
                time[i][j] += 1      # no. of iterations = no.of days
            if time[i][j] == 7:      # When no. of days is 7, we set a probability
                prob = random.random()
                if prob < 0.05:      # this is the input mortality rate
                    population[i][j] = -1  # -1 for dead
                else:
                    population[i][j] = 2   # 2 for recovered

    iterations.append(iteration)

    iteration += 1

print(len(iterations))
still_infected = 0
recovered = 0
dead = 0
for i in range(200):
    print(population[i])
    for j in population[i]:
        if j == 1:
            still_infected += 1
        elif j == 2:
            recovered += 1
        elif j == -1:
            dead += 1
# It is important to note why still_infected is not 0
print(f"still infected: {still_infected/400}")
print(f"mortality rate: {dead/400}")
print(f"recovery rate: {recovered/400}")
