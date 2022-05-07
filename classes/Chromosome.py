import numpy as np

class Chromosome:

    def __init__(self, gene_size, *, genes = None):
        if genes is None:
            rnd = np.random.default_rng()
            self.genes = np.arange(start = 0, stop = gene_size, dtype=int) 
            rnd.shuffle(self.genes)
        else:
            self.genes = genes
        self.gene_size = gene_size
        
    def mutate(self):
        rnd = np.random.default_rng()
        pos = rnd.integers(0, len(self.genes) - 1)
        self.genes[pos], self.genes[pos+1] = self.genes[pos+1], self.genes[pos] 

    def crossover(self, other_genes):
        rnd = np.random.default_rng()
        crosspoint = rnd.integers(0, self.gene_size - 1)
        offspring1 = np.concatenate((self.genes[:crosspoint], other_genes[crosspoint:]))
        offspring2 = np.concatenate((other_genes[:crosspoint], self.genes[crosspoint:]))
        aux1 = np.zeros(self.gene_size)
        aux2 = np.zeros(self.gene_size)
        duplicates1 = []
        duplicates2 = []
        for i in range(self.gene_size - 1, -1, -1):
            if aux1[offspring1[i]] == 1:
                duplicates1.append(i)
            if aux2[offspring2[i]] == 1:
                duplicates2.append(i)
            aux1[offspring1[i]] = 1
            aux2[offspring2[i]] = 1

        for index1, index2 in zip(duplicates1, duplicates2):
            offspring1[index1], offspring2[index2] = offspring2[index2], offspring1[index1]
        return offspring1, offspring2

        




    

