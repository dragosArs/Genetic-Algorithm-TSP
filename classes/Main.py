import numpy as np
from Population import Population
from Chromosome import Chromosome

filename = input("Please give name of input file:")
dist_mat = np.loadtxt(filename, dtype='float', delimiter=' ')

population_size = 400
gene_size = len(dist_mat[1,])
crossover_rate = 0.7
mutation_rate = 0.002
max_iterations = 600
convergence_error = 0.001

rnd = np.random.default_rng()

population = Population(population_size, gene_size, dist_mat)
population.initialize()
last_avg_fit = float("inf")
sum_fit = 0

##this loop iterates over generations(epochs)
for i in range(0, max_iterations):
    min_length, avg_fit = population.create_fitness_ranges()
    avg_fit /= population_size
    next_gen = []
    ##this loop iterates over chromosomes in population
    for j in range(0, len(population.chromosomes) // 2):
        mut_val = rnd.uniform(0, 1)
        if mut_val < mutation_rate:
            pos_chr = rnd.integers(0, len(population.chromosomes))
            population.chromosomes[pos_chr].mutate()

        pos1, pos2 = population.select_parents()
        chr1 = population.chromosomes[pos1]
        chr2 = population.chromosomes[pos2]
        crossover_val = rnd.uniform(0, 1)
        #print(crossover_val)
        if crossover_val < crossover_rate:
            genes1, genes2 = chr1.crossover(chr2.genes)    
            chr1 = Chromosome(gene_size, genes = genes1)
            chr2 = Chromosome(gene_size, genes = genes2)
        next_gen.append(chr1)
        next_gen.append(chr2)

    population.chromosomes = next_gen
    last_avg_fit = avg_fit

print(min_length, population.best_chr + 1) 