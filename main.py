from sus import stochastic_universal_sampling


if __name__ == "__main__":

    population_fitness = [3, 2, 4, 1, 5, 2]
    num_parents = 3

    parents = stochastic_universal_sampling(population_fitness, num_parents)
    print(parents) # output: [2, 4, 0]