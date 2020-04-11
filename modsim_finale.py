import csv

f=open('AreaExpressedInXY(1).csv', 'r')
reader=csv.reader(f)
XYpop=[]

for row in reader:
  XYpop.append([int(row[2]), int(row[3]), int(row[4])])

from random import *

'''legend for health status:
    0: healthy
    1: recovered
    2: dead
    3: hospitalised
    4: infected but not showing symptoms
'''
def close_enough(s, t):
    sq = (s[0]-t[0])**2 + (s[1]-t[1])**2
    distance = sq**0.5
    if distance <= 10.0:
        return True
    else:
        return False



nation_info = XYpop[:]
nation = []

for i in nation_info:
    population = [] # a !D array of humans
    l = i[0]   # x * y = total area of the state
    b = i[1]    # it is a random distribution
    pop = i[2] # total population

    health_status = 0 # index of health status

    for j in range(pop):
        a = [0, [randint(1, l), randint(1, b)], 0 , 0] # each element has 4 attributes: status, coordinates,
                                                       # days spent in suffering, day of death
        for m in range (1,13):  #predefine day of death
            c = random()
            if c <=0.05:
                break          # probability of dying
        if m<12:
            a[3]=m
        elif c<=0.05:
            a[3]=12
        population.append(a[:])

    I0 = sample(list(range(pop)), 10)       # randomly infecting 10 people
    for i in range(10):
        random_guy = population[I0[i]]
        infected = 4
        random_guy[health_status] = infected


    nation.append(population[:])

days = 5        # we can choose days for simulation
                # By default, this code runs till all infected either die or recover

for s in len(nation_info):
    population = nation[s]
    x = nation_info[s][0]   # x * y = total area of the state
    y = nation_info[s][1]    # it is a random distribution
    pop = nation_info[s][2]

    while True:
        all_done = True

        for i in range(pop):
            a = population[i]     # this where I am checking
                                    # and updating health status
            if a[health_status] > 2: # if human is sick
                all_done = False

                a[2] += 1               # first, we increase the days
                if a[2]==a[3]:
                    a[health_status] = 2
                elif a[2] == 5:         # if sick guy is on day5, hospitalise
                    a[health_status] = 3
                elif a[2] == 12:         # if he survives till day12, recover
                    a[health_status] = 1

        if all_done:
            break

        indices = sample(list(range(pop)), 24)
        # choosing 24 random people to move, last 4 people leave the state

        for i in range(20):
            a = population[indices[i]]              # internal movement
            a[1] = [randint(1, x), randint(1, y)]

        for k in range(20, 24):
            b = population.pop(indices[k])
            next_state = randint(1, 38)

            new_x = nation[next_state][10][1][0] + nation[next_state][90][1][0]
            new_x /= 2

            new_y = nation[next_state][14][1][0] + nation[next_state][70][1][1]
            new_y /= 2

            b[1] = [new_x, new_y]
            nation[next_state].append(b)


        for i in range(pop-1):                      # now, everybody in 10m radius of
            if population[i][0] != 4:               # sick people will get infected
                continue
            else:
                for j in range(1, pop):
                    v = population[i]
                    t = population[j]
                    if t[health_status] == 0 and close_enough(v[1], t[1]):
                        t[health_status] = 4


    fine = 0
    deadcount = 0
    immune = 0
    sick = 0
    hospitalised = 0

    for i in range(pop):
        person = population[i]

        if person[health_status] == 2:
            deadcount += 1
        elif person[health_status] ==1:
            immune += 1
        elif person[health_status] == 0:
            fine += 1
        elif person[health_status] == 3:
            hospitalised +=1
        else:
            sick += 1

    print(f"state no.{s+1}")
    print(f"dead: {deadcount}")
    print(f"immune: {immune}")
    print(f"sick: {sick}")
    print(f"fine: {fine}")
    print(f"admitted: {hospitalised}")
    print('')
