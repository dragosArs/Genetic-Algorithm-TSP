import numpy as np
from Chromosome import Chromosome

class Population:

    def __init__(self, population_size, chr_size,  dist_mat):
        self.population_size = population_size
        self.chr_size = chr_size
        self.dist_mat = dist_mat
        self.chromosomes = []
    
    def initialize(self):
        for i in range(0, self.population_size):
            self.chromosomes.append(Chromosome(self.chr_size))
    
    ##returns an array that makes it easy to select two parents for crossover
    ##the biger the fitness of the parents the bigger the chance to get selected
    def create_fitness_ranges(self):
        ##self.chromosomes.sort(key = lambda x: x.fitness())
        self.fitness_ranges = np.zeros(self.population_size)
        min_length = float("inf")
        sum = 0
        for i in range(1, self.population_size):
            fitness = 1 / self.length_of_route(i)
            self.fitness_ranges[i] = self.fitness_ranges[i-1] + fitness
            sum += fitness
            if self.length_of_route(i) < min_length:
                min_length = self.length_of_route(i)
                self.best_chr = self.chromosomes[i].genes
        return min_length, sum
    
    ##returns the positions of the two selected parents in the population
    def select_parents(self):
        max_val = self.fitness_ranges[-1]
        rnd = np.random.default_rng()
        val1 = rnd.uniform(0, max_val)
        val2 = rnd.uniform(0, max_val)
        pos1 = np.searchsorted(self.fitness_ranges, val1, side = 'right')
        pos2 = np.searchsorted(self.fitness_ranges, val2, side = 'right')
        return pos1, pos2

    
    def length_of_route(self, pos):
        sum = 0
        chr = self.chromosomes[pos]
        for i in range(0, self.chr_size):
            sum += self.dist_mat[chr.genes[i]][chr.genes[i-1]]
        return sum




    