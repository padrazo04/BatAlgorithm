import random 
import numpy as np

class BatAlgorithm():
    def __init__(self, D, NP, N_Gen, A, r, fMin, fMax, Lower, Upper, function):
        self.dimension = D  #dimension
        self.populationSize = NP  #population size 
        self.generations = N_Gen  #generations
        self.A = A  #loudness
        self.r = r  #pulse rate
        self.frequency = [0] * self.populationSize  #frequency
        self.fMin = fMin  #frequency min
        self.fMax = fMax  #frequency max
        self.Lower = Lower  #lower bound
        self.Upper = Upper  #upper bound

        self.Lb = [0] * self.dimension  #lower bound
        self.Ub = [0] * self.dimension  #upper bound

        self.v = [[0 for i in range(self.dimension)] for j in range(self.populationSize)]  #velocity
        self.Sol = [[0 for i in range(self.dimension)] for j in range(self.populationSize)]  #population of solutions
        self.Fitness = [0] * self.populationSize  #fitness
        self.best = [0] * self.dimension  #best solution
        self.bestFitness = 0.0  #minimum fitness

        self.Fun = function


    def best_bat(self):
        bestSolPosition = 0
        for i in range(self.populationSize):
            if self.Fitness[i] < self.Fitness[bestSolPosition]:
                bestSolPosition = i
        for i in range(self.dimension):
            self.best[i] = self.Sol[bestSolPosition][i]
        self.bestFitness = self.Fitness[bestSolPosition]

    def init_bat(self):
        for i in range(self.dimension):
            self.Lb[i] = self.Lower
            self.Ub[i] = self.Upper

        for i in range(self.populationSize):
            self.frequency[i] = 0
            for j in range(self.dimension):
                rnd = np.random.uniform(0, 1)
                self.v[i][j] = 0.0
                self.Sol[i][j] = self.Lb[j] + (self.Ub[j] - self.Lb[j]) * rnd
            self.Fitness[i] = self.Fun(self.dimension, self.Sol[i])
        self.best_bat()

    def simplebounds(self, val, lower, upper):
        if val < lower:
            val = lower
        if val > upper:
            val = upper
        return val

    def move_bat(self):
        S = [[0.0 for i in range(self.dimension)] for j in range(self.populationSize)]

        self.init_bat()

        for t in range(self.generations):
            for i in range(self.populationSize):
                rnd = np.random.uniform(0, 1)
                self.frequency[i] = self.fMin + (self.fMax - self.fMin) * rnd
                for j in range(self.dimension):
                    self.v[i][j] = self.v[i][j] + (self.Sol[i][j] -
                                                   self.best[j]) * self.frequency[i]
                    S[i][j] = self.Sol[i][j] + self.v[i][j]

                    S[i][j] = self.simplebounds(S[i][j], self.Lb[j],
                                                self.Ub[j])

                rnd = np.random.random_sample()
                # print(rnd)
                # input("continue")

                if rnd > self.r:
                    for j in range(self.dimension):
                        S[i][j] = self.best[j] + 0.001 * random.gauss(0, 1)
                        S[i][j] = self.simplebounds(S[i][j], self.Lb[j],
                                                self.Ub[j])
                        
                Fnew = self.Fun(self.dimension, S[i])

                rnd = np.random.random_sample()

                if (Fnew <= self.Fitness[i]) and (rnd < self.A):
                    for j in range(self.dimension):
                        self.Sol[i][j] = S[i][j]
                    self.Fitness[i] = Fnew

                if Fnew <= self.bestFitness:
                    for j in range(self.dimension):
                        self.best[j] = S[i][j]
                    self.bestFitness = Fnew

        print(self.bestFitness)
