import random

class Population:
    def __init__(self, population_size, initialise):
        self._individuals = []
        self._population_size = population_size 
        self._initialise = initialise
        
        if(initialise):
            for i in range(population_size):
                new_individual = new Individual()
                new_individual.generate_individual()
                self._individuals.append(new_individual)
                

    def get_individual(self, index):
        return self._individuals[index]
    
    
    def get_fittest(self):
        fittest = self._individuals[0]
        for individual in self._indivuals:
            if(fittest.get_fitness() <= individual.get_fitness()):
                fittest = individual
        return fittest
    
    
    def size(self):
        return len(self._individuals)  
    
class Individual:
    def __init__(self):
        self._gene_length = 40
        self._genes = []
        self._fitness = 0
    
    
    def generate_individual(self):
        for i in range(self._gene_length):
            self._genes[i] = random.randint(0,1)
    
    
    def get_gene(self, index):
        return self._genes[index]
    
    
    def set_gene(self, index, number):
        self._genes[index] = number
        self._fitness = 0
    
    
    def get_fitness(self):
        if(fitness == 0 ):
            fitness = FitnessCalc.get_fitness(self)
        return fitness

        
    def gene_as_string(self):
        gene_string += (str(self.get_gene(i)) for i in range(self._gene_length))
        return gene_string 

class Algorithm:
    def __init__(self):
        pass

class FitnessCalc:
    def __init__(self):
        pass
    