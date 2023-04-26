import random

def stochastic_universal_sampling(population_fitness, num_parents):

    F = sum(population_fitness) # calculate the sum of fitness values
    N = num_parents 
    P = F / float(N) # calculate the spacing between selection points
    start_point = random.uniform(0, P) # choose a random starting point within the spacing
    
    parents = []
    cumulative_fitness = population_fitness[0]
    parent_idx = 0

    for i in range(N):
        while start_point > cumulative_fitness:
            parent_idx += 1
            cumulative_fitness += population_fitness[parent_idx]
        parents.append(parent_idx)
        start_point += P

    return parents